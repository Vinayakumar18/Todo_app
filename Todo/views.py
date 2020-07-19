from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
    Todolist=Todo.objects.order_by('id')
    form = TodoForm()
    context={'Todolist' : Todolist , 'form' : form}
    return render(request,'index.html',context)


def add(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = Todo(text=request.POST['text'])
        todo.save()

    return redirect('index')


def check(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def uncheck(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()

    return redirect('index')

def deletecomplete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteall(request):
    Todo.objects.all().delete()

    return redirect('index')
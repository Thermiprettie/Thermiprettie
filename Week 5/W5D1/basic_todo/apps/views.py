from asyncio import all_tasks
from django.shortcuts import render,redirect
from django.views import generic
from .models import TodoData
from django.http import HttpResponseRedirect
from .forms import Todo_Task_form
# Create your views here.
#CRUD CREATE, READ, UPDATE, DELETE

# read

def  ListTask(request):#this returns all the task you have created in your app
    context = {}#context here is a set. It is an empty set. A set will appear mainly with values. It won't appear
    all_tasks = TodoData.objects.all()#This is a query set. all_tasks is a variable
    context['all_tasks'] = all_tasks#store all_tasks as one of the sets in context
    return render(request, 'homepage.html', context)#return it to the homepage

# create
def  CreateTask(request):
    if request.method == 'POST':
        forms = Todo_Task_form(request.POST)
        if forms.is_valid():
            new_todo = forms.save(commit=false)
            new_todo.save()
            return redirect ('listtask')
        else:
            forms = Todo_Task_form()
    else:
        forms = Todo_Task_form()
    
    return render(request, 'create.html', {'forms':forms})

# delete
def  DeleteTask(request, pk):
    tod_task = TodoData.objects.all().filter(pk = pk)
    tod_task.delete()
    return redirect('/')


# update
def  UpdateTask(request, pk):
    #create a function to update our task
    todoapp_in_question = TodoData.objects.get(pk=pk)#get the object from database using id
    formUpdate = Todo_Task_form(request.POST, instance = todoapp_in_question)
    
    
    if request.method == "post":
        if formUpdate.is_valid():
            formUpdate.save()
            return redirect("/")
        else:
            
            return render (request, "update.html", {formUpdate: "formUpdate"})
    return render(request, "update.html", {"formUpdate": formUpdate})
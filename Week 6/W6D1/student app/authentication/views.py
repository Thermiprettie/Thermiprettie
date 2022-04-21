from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.

# CRUD - Create, Read, Update, Delete

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegisterForm
        return render(request, 'registration/register.html', {'form':form})
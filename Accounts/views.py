from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUPForm, SignInForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = SignUPForm()
    elif request.method == 'POST':
        form = SignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request, 'accounts/signup.html',{'form': form})

def signin(request):
    if request.method == 'GET':
        form = SignInForm()
    elif request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')
            else:
                messages.error(request)
    return render(request, 'accounts/signin.html', {'form':form})

def signout(reqest):
    logout(reqest)
    return redirect('signin')
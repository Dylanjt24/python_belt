from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(req):
    return render(req, 'users/index.html')

def register(req):
    errors = User.objects.validate_registration(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:index')
    user = User.objects.create_user(req.POST)
    req.session['name'] = user.first_name
    req.session['user_id'] = user.id
    return redirect('users:home')

def login(req):
    errors = User.objects.validate_login(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:index')
    user = User.objects.get(email=req.POST['email'])
    req.session['name'] = user.first_name
    req.session['user_id'] = user.id
    return redirect('users:home')

def home(req):
    if 'user_id' not in req.session:
        return redirect('users:index')
    return render(req, 'users/home.html')

def logout(req):
    req.session.clear()
    return redirect('users:index')
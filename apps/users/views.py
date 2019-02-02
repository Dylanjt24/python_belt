from django.shortcuts import render, redirect
from .models import User, Job
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
    return redirect('users:dashboard')

def login(req):
    errors = User.objects.validate_login(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:index')
    user = User.objects.get(email=req.POST['email'])
    req.session['name'] = user.first_name
    req.session['user_id'] = user.id
    return redirect('users:dashboard')

def dashboard(req):
    if 'user_id' not in req.session:
        return redirect('users:index')
    context = {
        'jobs': Job.objects.all(),
        'user_jobs': Job.objects.filter(holder=req.session['user_id']),
        'user': User.objects.get(id=req.session['user_id'])
    }
    return render(req, 'users/dashboard.html', context)

def add_job(req):
    return render(req, 'users/add_job.html')

def create_job(req):
    errors = Job.objects.validate_job(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:add_job')
    user = User.objects.get(id=req.session['user_id'])
    Job.objects.create_job(req.POST, user)
    return redirect('users:dashboard')

def user_job(req, job_id):
    job = Job.objects.get(id=job_id)
    user = User.objects.get(id=req.session['user_id'])
    job.holder = user
    job.save()
    return redirect('users:dashboard')

def view(req, job_id):
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(req, 'users/view.html', context)

def edit(req, job_id):
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(req, 'users/edit.html', context)

def confirm(req, job_id):
    job = Job.objects.get(id=job_id)
    job.title = req.POST['title']
    job.description = req.POST['description']
    job.location = req.POST['location']
    job.save()
    return redirect('users:dashboard')

def delete(req, job_id):
    job = Job.objects.filter(id=job_id)
    job.delete()
    return redirect('users:dashboard')

def logout(req):
    req.session.clear()
    return redirect('users:index')
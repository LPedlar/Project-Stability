from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Employer, Job
from .forms import JobForm, EmployerForm, EmployerSignInForm, EmployerSignUpForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from ProjectStability.backends import EmployerAuthBackend

def employer_signup(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to employer home page after successful sign-up
            return redirect('../employer_home')
    else:
        form = EmployerSignUpForm()
    return render(request, 'employer/employer_signup.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'employer/job_list.html', context)

def index(request):
    return render(request, 'index.html')

def employer_home(request):
    print("Home view called") # Add this line
    employers = Employer.objects.all()
    context = {'employers': employers}
    return render(request, 'employer/employer_home.html', context)

def employer_profile(request, employer_id):
    employer = Employer.objects.get(id=employer_id)
    context = {'employers': employer}
    return render(request, 'employer/employer_profile.html', context)

def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../job_list')
    else:
        form = JobForm()
    return render(request, 'employer/job_post.html', {'form': form})

def employer_signin(request):
    if request.method == 'POST':
        form = EmployerSignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password, backend='ProjectStability.backends.EmployerAuthBackend')
            if user is not None and user.is_employer:
                login(request, user)
                return redirect('../employer_home')
            else:
                form.add_error('email', 'Invalid email or password.')
    else:
        form = EmployerSignInForm()
    return render(request, 'employer/employer_signin.html', {'form': form})





from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Employer, Job
from .forms import JobForm, EmployerForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Employer
from .forms import EmployerSignUpForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Employer
from .forms import EmployerSignUpForm

class EmployerSignUpView(CreateView):
    model = Employer
    form_class = EmployerSignUpForm
    template_name = 'EmployerTemplates/employer_signup.html'

    def form_valid(self, form):
        # save the employer form
        response = super().form_valid(form)
        # redirect to the employer home page
        return redirect('employer_home')



def employer_signup(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to employer home page after successful sign-up
            return redirect('employer_home')
    else:
        form = EmployerForm()
    return render(request, 'employer_signup.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)

def index(request):
    return render(request, 'index.html')

def employer_home(request):
    print("Home view called") # Add this line
    employers = Employer.objects.all()
    context = {'employers': employers}
    return render(request, 'employer_home.html', context)

def employer_profile(request, employer_id):
    employer = Employer.objects.get(id=employer_id)
    context = {'employers': employer}
    return render(request, 'employer_profile.html', context)

def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_post.html', {'form': form})



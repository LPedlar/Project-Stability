from django.shortcuts import render, redirect
from .models import Employer, Job, Applicant, ApplicationStatus, Application
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from ProjectStability.backends import EmployerAuthBackend
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import EmployerSignUpForm, CandidateSignUpForm, CandidateSignInForm, EmployerSignInForm, JobForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages

class EmployerCandidateSignUpView(TemplateView):
    template_name = 'ProjectStability/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employer_signup_form'] = EmployerSignUpForm()
        context['candidate_signup_form'] = CandidateSignUpForm()
        context['employer_signin_form'] = EmployerSignInForm()
        context['candidate_signin_form'] = CandidateSignInForm()
        return context

    def post(self, request):
        if 'employer_signup' in request.POST:
            form = EmployerSignUpForm(request.POST)
            if form.is_valid():
                employer = form.save()
                login(request, employer, backend='ProjectStability.backends.EmployerAuthBackend')
                return redirect('../employer/employer_home')
            else:
                context = self.get_context_data()
                context['employer_signup_form'] = form
                return self.render_to_response(context)

        elif 'candidate_signup' in request.POST:
            form = CandidateSignUpForm(request.POST)
            if form.is_valid():
                applicant = form.save()
                login(request, applicant, backend='ProjectStability.backends.ApplicantAuthBackend')
                return redirect('../candidate/candidate_home')
            else:
                context = self.get_context_data()
                context['candidate_signup_form'] = form
                return self.render_to_response(context)

        elif 'employer_signin' in request.POST:
            form = EmployerSignInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password, backend='ProjectStability.backends.EmployerAuthBackend')
                if user is not None and user.is_employer:
                    login(request, user)
                    return redirect('../employer/employer_home')
                else:
                    form.add_error('email', 'Invalid email or password.')
                    context = self.get_context_data()
                    context['employer_signin_form'] = form
                    return self.render_to_response(context)
            else:
                context = self.get_context_data()
                context['employer_signin_form'] = form
                return self.render_to_response(context)

        elif 'candidate_signin' in request.POST:
            form = CandidateSignInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password, backend='ProjectStability.backends.ApplicantAuthBackend')
                if user is not None and user.is_applicant:
                    login(request, user)
                    return redirect('../candidate/candidate_home')
                else:
                    form.add_error('email', 'Invalid email or password.')
                    context = self.get_context_data()
                    context['candidate_signin_form'] = form
                    return self.render_to_response(context)
            else:
                context = self.get_context_data()
                context['candidate_signin_form'] = form
                return self.render_to_response(context)

        else:
            return HttpResponseBadRequest("Invalid POST request")

class HomeView(TemplateView):
    template_name = 'ProjectStability/home.html'

class EmployerSignUpView(CreateView):
    model = Employer
    form_class = EmployerSignUpForm
    template_name = 'employer/employer_signup.html'

    def form_valid(self, form):
        # save the candidate form and redirect to the candidate home page
        employer = form.save()
        login(self.request, employer, backend='ProjectStability.backends.EmployerAuthBackend')
        return redirect('../employer_home')

def job_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'employer/job_list.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, JobID=job_id)
    context = {'job': job}
    return render(request, 'employer/job_detail.html', context)

def delete_job(request, job_id):
    job = get_object_or_404(Job, JobID=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('employer:job_list')
    context = {'job': job}
    return render(request, 'employer/delete_job.html', context)

def index(request):
    return render(request, 'index.html')

def employer_home(request):
    statuses = [
        ApplicationStatus.INTERESTED,
        ApplicationStatus.IN_REVIEW,
        ApplicationStatus.INTERVIEW,
        ApplicationStatus.ACCEPTED,
        ApplicationStatus.REQUEST,
        ApplicationStatus.HIRED,
        ApplicationStatus.DORMANT,
        ApplicationStatus.DECLINED,
    ]

    for status in statuses:
        obj, created = ApplicationStatus.objects.get_or_create(StatusName=status)
        if created:
            obj.save()
    print("Home view called") # Add this line
    employers = Employer.objects.all()
    context = {'employers': employers}
    return render(request, 'employer/employer_home.html', context)

def employer_profile(request):
    employer = Employer.objects.get(EmployerID=request.user.EmployerID)
    context = {'employers': employer}
    return render(request, 'employer/employer_profile.html', context)

@login_required
def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.EmployerID = Employer.objects.get(EmployerID=request.user.EmployerID)
            job.save()
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

def employer_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))

def user_pipeline(request):
        return render(request, 'employer/user_pipeline.html')
    
@login_required
def applications(request):
    employer = request.user.EmployerID
    applications = Application.objects.filter(JobID__EmployerID=employer, StatusID__StatusName='In Review')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'employer/applications.html', context)

@login_required
def interview(request):
    employer = request.user.EmployerID
    applications = Application.objects.filter(JobID__EmployerID=employer, StatusID__StatusName='Interview')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'employer/interview.html', context)

@login_required
def approved(request):
    employer = request.user.EmployerID
    applications = Application.objects.filter(JobID__EmployerID=employer, StatusID__StatusName='Accepted')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'employer/approved.html', context)

@login_required
def position_request(request):
    employer = request.user.EmployerID
    applications = Application.objects.filter(JobID__EmployerID=employer, StatusID__StatusName='Request')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'employer/position_requests.html', context)

@login_required
def hired(request):
    employer = request.user.EmployerID
    applications = Application.objects.filter(JobID__EmployerID=employer, StatusID__StatusName='Hired')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'employer/hired.html', context)

def update1(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Interview')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Redirect to interview page
    return redirect(request.META.get('HTTP_REFERER'))

def update2(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Accepted')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Redirect to interview page
    return redirect(request.META.get('HTTP_REFERER'))

def hire(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)
    job = application.JobID
    job_title = job.JobTitle
    
    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Hired')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Retrieve the applicant using the ApplicantID on the application
    applicant = application.ApplicantID
    applicant.Profession = job_title
    applicant.save()
    
    # Redirect to interview page
    return redirect(request.META.get('HTTP_REFERER'))

def decline(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Declined')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Redirect to previous page
    return redirect(request.META.get('HTTP_REFERER'))

def fire(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Update the application's status to 'Interview'
    application.delete()
    messages.success(request, "Application removed successfully.")

    # Retrieve the applicant using the ApplicantID on the application
    applicant = application.ApplicantID
    applicant.Profession = 'Unemployed'
    applicant.save()
    
    # Redirect to interview page
    return redirect(request.META.get('HTTP_REFERER'))
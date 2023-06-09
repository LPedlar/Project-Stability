from employer.forms import ApplicantForm, CandidateSignUpForm, CandidateSignInForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from employer.models import Applicant, Job
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from employer.models import Application, ApplicationStatus
from django.utils import timezone
from django.contrib import messages

class CandidateSignUpView(CreateView):
    model = Applicant
    form_class = CandidateSignUpForm
    template_name = 'candidate/candidate_signup.html'

    def form_valid(self, form):
        # save the candidate form and redirect to the candidate home page
        applicant = form.save()
        login(self.request, applicant, backend='ProjectStability.backends.ApplicantAuthBackend')
        return redirect('../candidate_home')

@login_required
def candidate_home(request):
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
    try:
        applicant = Applicant.objects.get(ApplicantID=request.user.ApplicantID)
    except Applicant.DoesNotExist:
        applicant = None
    context = {'applicant': applicant}
    return render(request, 'candidate/candidate_home.html', context)

def candidate_profile(request):
    applicant = Applicant.objects.get(ApplicantID=request.user.ApplicantID)
    context = {'applicant': applicant}
    return render(request, 'candidate/candidate_profile.html', context)

def candidate_signin(request):
    if request.method == 'POST':
        form = CandidateSignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password, backend='ProjectStability.backends.ApplicantAuthBackend')
            if user is not None and user.is_applicant:
                login(request, user)
                return redirect('../candidate_home')
            else:
                form.add_error('email', 'Invalid email or password.')
    else:
        form = CandidateSignInForm()
    return render(request, 'candidate/candidate_signin.html', {'form': form})

def candidate_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))

def job_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'candidate/job_list.html', context)

def job_pipeline(request):
    return render(request, 'candidate/job_pipeline.html')

def job_detail(request, job_id):
    job = get_object_or_404(Job, JobID=job_id)
    context = {'job': job}
    return render(request, 'candidate/job_detail.html', context)

def int_detail(request, job_id):
    job = get_object_or_404(Job, JobID=job_id)
    context = {'job': job}
    return render(request, 'candidate/interested_detail.html', context)

def apply(request, job_id):
    job = get_object_or_404(Job, JobID=job_id)
    context = {'job': job}
    return render(request, 'candidate/apply.html', context)

def apply_interested(request, job_id):
    job = get_object_or_404(Job, JobID=job_id)
    context = {'job': job}
    return render(request, 'candidate/apply_interested.html', context)

def save(request, job_id):
    # Get the job and the logged-in user
    job = get_object_or_404(Job, JobID=job_id)
    applicant = Applicant.objects.get(ApplicantID=request.user.ApplicantID)
    status_interested = ApplicationStatus.objects.get(StatusName='Interested')

    # Check if the applicant has already applied to the job
    if Application.objects.filter(JobID=job, ApplicantID=applicant, StatusID=status_interested).exists():
        messages.error(request, "You have already applied to this job.")
    # Check if the applicant has already applied to the job
    elif Application.objects.filter(JobID=job, ApplicantID=applicant).exists():
        messages.error(request, "You have already applied to this job.")
    else:
        # Create a new application with the necessary fields
        application = Application(
            JobID=job,
            ApplicantID=applicant,
            DateApplied=timezone.now(),
            StatusID=ApplicationStatus.objects.filter(StatusName='Interested').first()
        )

        # Save the new application
        application.save()
        messages.success(request, "Application saved successfully.")

    # Redirect back to the job details page
    return redirect('candidate:job_detail', job_id=job.JobID)

def save_interested(request, job_id):
    # Get the job and the logged-in user
    job = get_object_or_404(Job, JobID=job_id)
    applicant = Applicant.objects.get(ApplicantID=request.user.ApplicantID)
    status_interested = ApplicationStatus.objects.get(StatusName='Interested')

    # Check if the applicant has already applied to the job
    if Application.objects.filter(JobID=job, ApplicantID=applicant, StatusID=status_interested).exists():
        messages.error(request, "You have already applied to this job.")
    # Check if the applicant has already applied to the job
    if Application.objects.filter(JobID=job, ApplicantID=applicant).exists():
        messages.error(request, "You have already applied to this job.")
    else:
        # Create a new application with the necessary fields
        application = Application(
            JobID=job,
            ApplicantID=applicant,
            DateApplied=timezone.now(),
            StatusID=ApplicationStatus.objects.filter(StatusName='Interested').first()
        )

        # Save the new application
        application.save()
        messages.success(request, "Application saved successfully.")

    # Redirect back to the job details page
    return redirect('candidate:interested_detail', job_id=job.JobID)


@login_required
def interested(request):
    candidate = request.user
    applications = Application.objects.filter(ApplicantID=candidate, StatusID__StatusName='Interested')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'candidate/interested.html', context)

@login_required
def in_review(request):
    candidate = request.user
    applications = Application.objects.filter(ApplicantID=candidate, StatusID__StatusName='In Review')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'candidate/in_review.html', context)

@login_required
def approved(request):
    candidate = request.user
    applications = Application.objects.filter(ApplicantID=candidate, StatusID__StatusName='Accepted')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'candidate/approved.html', context)

@login_required
def dormant(request):
    candidate = request.user
    applications = Application.objects.filter(ApplicantID=candidate, StatusID__StatusName='Dormant')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'candidate/dormant.html', context)

@login_required
def declined(request):
    candidate = request.user
    applications = Application.objects.filter(ApplicantID=candidate, StatusID__StatusName='Declined')
    jobs = []
    for app in applications:
        jobs.append(app.JobID)
    context = {
        'jobs': jobs,
    }
    return render(request, 'candidate/declined.html', context)

def apply_confirm(request, job_id):
    # Get the job and the logged-in user
    job = get_object_or_404(Job, JobID=job_id)
    applicant = Applicant.objects.get(ApplicantID=request.user.ApplicantID)

    # Get the 'In Review' status object
    status_in_review = ApplicationStatus.objects.get(StatusName='In Review')
    status_interested = ApplicationStatus.objects.get(StatusName='Interested')

    # Check if the applicant has already applied to the job
    if Application.objects.filter(JobID=job, ApplicantID=applicant, StatusID=status_in_review).exists():
        messages.error(request, "You have already applied to this job.")
    elif Application.objects.filter(JobID=job, ApplicantID=applicant, StatusID=status_interested).exists():
        # Update the existing application's status to 'In Review'
        application = Application.objects.get(JobID=job, ApplicantID=applicant, StatusID=status_interested)
        application.StatusID = status_in_review
        application.save()
        messages.success(request, "Application updated to In Review successfully.")
    else:
        # Create a new application with the necessary fields
        application = Application(
            JobID=job,
            ApplicantID=applicant,
            DateApplied=timezone.now(),
            StatusID=status_in_review
        )

        # Save the new application
        application.save()
        messages.success(request, "Application saved successfully.")

    # Redirect back to the job details page
    return redirect('candidate:in_review')

def update0(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Update the application's status to 'Interview'
    application.delete()
    messages.success(request, "Application removed successfully.")

    # Redirect to interview page
    return redirect('candidate:interested')

def update1(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Dormant')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Redirect to interview page
    return redirect('candidate:approved')

def update2(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Request')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Redirect to interview page
    return redirect('candidate:approved')

def update3(request, application_id):
    # Get the application using the inputted ID
    application = get_object_or_404(Application, ApplicationID=application_id)

    # Get the 'Interview' status objects
    interview_status = ApplicationStatus.objects.get(StatusName='Accepted')

    # Update the application's status to 'Interview'
    application.StatusID = interview_status
    application.save()
    messages.success(request, "Application saved successfully.")

    # Redirect to interview page
    return redirect('candidate:dormant')
from django.shortcuts import render
from django.http import HttpResponse
from employer.forms import ApplicantForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import CreateView
from employer.models import Applicant
from employer.forms import CandidateSignUpForm

class CandidateSignUpView(CreateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'CandidateTemplates/candidate_signup.html'

    def form_valid(self, form):
        # save the candidate form and redirect to the candidate home page
        return redirect('candidate/candidate_home')

def candidate_signup(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to candidate home page after successful sign-up
            return redirect('../candidate_home')
    else:
        form = ApplicantForm()
    return render(request, 'candidate/candidate_signup.html', {'form': form})

def candidate_home(request):
    Applicant = None  # Define the variable before trying to access its attributes
    if request.user.is_authenticated and request.user.is_candidate:
        Applicant = Applicant.objects.get(user=request.user)
    context = {'Applicant': Applicant}
    return render(request, 'candidate/candidate_home.html', context)

def candidate_profile(request, candidate_id):
    Applicant = Applicant.objects.get(id=candidate_id)
    context = {'Applicant': Applicant}
    return render(request, 'candidate/candidate_profile.html', context)
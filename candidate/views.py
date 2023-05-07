from employer.forms import ApplicantForm, CandidateSignUpForm, CandidateSignInForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from employer.models import Applicant
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

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

from django import forms
from .models import Job, Employer, Applicant
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class EmployerSignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password, backend='ProjectStability.backends.EmployerAuthBackend')
            if not user:
                raise forms.ValidationError('Invalid email or password')
        return cleaned_data

class EmployerSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = Employer
        fields = ['CompanyName', 'Industry', 'Email']
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    @transaction.atomic
    def save(self, commit=True):
        employer = super().save(commit=False)
        employer.set_password(self.cleaned_data.get('password1'))
        if commit:
            employer.save()
        return employer
    
class CandidateSignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password, backend='ProjectStability.backends.CandidateAuthBackend')
            if not user:
                raise forms.ValidationError('Invalid email or password')
        return cleaned_data

class CandidateSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Applicant
        fields = ['FirstName', 'LastName', 'Email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    @transaction.atomic
    def save(self, commit=True):
        applicant = super().save(commit=False)
        applicant.Password = make_password(self.cleaned_data.get('password1'))
        if commit:
            applicant.save()
        return applicant




class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('CompanyName', 'Industry', 'Email', 'Password')
        widgets = {
            'Password': forms.PasswordInput(),
        }

class ApplicantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Applicant
        fields = ['FirstName', 'LastName', 'Email', 'password']
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['JobTitle', 'JobDescription', 'Salary', 'Location', 'DatePosted', 'EmployerID']

from django import forms
from employer.models import Job
from django import forms
from employer.models import Applicant
from django import forms
from employer.models import Employer

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

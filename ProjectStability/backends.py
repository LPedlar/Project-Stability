from django.contrib.auth.backends import BaseBackend
from employer.models import Employer, Applicant
import pdb;
from django.contrib.auth.hashers import check_password

class ApplicantAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            applicant = Applicant.objects.get(Email=email)
        except Applicant.DoesNotExist:
            return None

        if check_password(password, applicant.Password):
            return applicant
        else:
            return None

    def get_user(self, user_id):
        try:
            return Applicant.objects.get(pk=user_id)
        except Applicant.DoesNotExist:
            return None


class EmployerAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            employer = Employer.objects.get(Email=email)
        except Employer.DoesNotExist:
            return None

        if check_password(password, employer.Password):
            return employer
        else:
            return None

    def get_user(self, user_id):
        try:
            return Employer.objects.get(pk=user_id)
        except Employer.DoesNotExist:
            return None

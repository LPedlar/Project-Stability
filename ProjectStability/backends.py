from django.contrib.auth.backends import BaseBackend
from employer.models import Employer, Applicant
import pdb;

class ApplicantAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            applicant = Applicant.objects.get(Email=email)
        except Applicant.DoesNotExist:
            return None

        if applicant.Password == password:
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
            if employer.Password == password:
                return employer
        except Employer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employer.objects.get(pk=user_id)
        except Employer.DoesNotExist:
            return None

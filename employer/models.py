from datetime import date
from django.db import models

# # Create your models here.
class Employer(models.Model):
    EmployerID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    Industry = models.CharField(max_length=255, blank=True, null=True)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    is_employer = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.CompanyName
    
    def is_authenticated(self):
        return True


class Job(models.Model):
    JobID = models.AutoField(primary_key=True)
    JobTitle = models.CharField(max_length=255, verbose_name= "Job Title")
    JobDescription = models.TextField(blank=True, null=True, verbose_name="Job Description")
    Salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Location = models.CharField(max_length=255, blank=True, null=True)
    DatePosted = models.DateField(verbose_name= "Date Posted")
    EmployerID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    def __str__(self):
        return self.JobTitle

class Applicant(models.Model):
    ApplicantID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Profession = models.CharField(max_length=255, default='Unemployed')
    is_applicant = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    def is_authenticated(self):
        """
        Return True if the user is authenticated, False otherwise.
        """
        return True

class ApplicationStatus(models.Model):
    INTERESTED = 'Interested'
    IN_REVIEW = 'In Review'
    INTERVIEW = 'Interview'
    ACCEPTED = 'Accepted'
    REQUEST = 'Request'
    HIRED = 'Hired'
    DORMANT = 'Dormant'
    DECLINED = 'Declined'
    STATUS_CHOICES = [
        (INTERESTED, 'Interested'),
        (IN_REVIEW, 'In Review'),
        (INTERVIEW, 'Interview'),
        (ACCEPTED, 'Accepted'),
        (REQUEST, 'Request'),
        (HIRED, 'Hired'),
        (DORMANT, 'Dormant'),
        (DECLINED, 'Declined'),
    ]
    id = models.AutoField(primary_key=True)
    StatusName = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.StatusName


class Application(models.Model):
    ApplicationID = models.AutoField(primary_key=True)
    ApplicantID = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    JobID = models.ForeignKey(Job, on_delete=models.CASCADE)
    DateApplied = models.DateField()
    StatusID = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ApplicantID} applied for {self.JobID} on {self.DateApplied}"
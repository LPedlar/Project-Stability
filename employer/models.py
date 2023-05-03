from datetime import date
from django.db import models

# # Create your models here.
class Employer(models.Model):
    EmployerID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    Industry = models.CharField(max_length=255, blank=True, null=True)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)

class Job(models.Model):
    JobID = models.AutoField(primary_key=True)
    JobTitle = models.CharField(max_length=255)
    JobDescription = models.TextField(blank=True, null=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Location = models.CharField(max_length=255, blank=True, null=True)
    DatePosted = models.DateField()
    EmployerID = models.ForeignKey(Employer, on_delete=models.CASCADE)

class Applicant(models.Model):
    ApplicantID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)

class ApplicationStatus(models.Model):
    StatusID = models.AutoField(primary_key=True)
    StatusName = models.CharField(max_length=255)

class Application(models.Model):
    ApplicationID = models.AutoField(primary_key=True)
    ApplicantID = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    JobID = models.ForeignKey(Job, on_delete=models.CASCADE)
    DateApplied = models.DateField()
    StatusID = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE)

# class Course(models.Model):
#     course_id = models.AutoField(primary_key=True)
#     course_title = models.CharField(max_length=100)
#     course_description = models.TextField()
#     credits = models.IntegerField()
#     instructor = models.CharField(max_length=100)
#     start_date = models.DateField(default = date(2022,1,1))
    
#     def __str__(self):
#         return self.course_title


class JobPost(models.Model):
    job_id = models.AutoField(primary_key = True)
    job_title  = models.CharField(max_length=100)
    job_description = models.TextField()
    
    def __str__(self):
         return self.job_title
from datetime import date
from django.db import models

# # Create your models here.
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
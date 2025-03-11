from django.db import models

# Create your models here.
class JobPosition(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=100)
    job_description = models.TextField()
    
class Departments(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_id = models.ForeignKey(JobPosition, on_delete=models.SET_NULL, null=True, blank=True)
    dept_id = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    

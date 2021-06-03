from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'department'

from django.db import models  
class Employee(models.Model):  
    eid = models.AutoField(primary_key=True, null=False)  
    name = models.CharField(max_length=100, null=False)  
    email = models.EmailField()  
    cnic = models.CharField(max_length=15, null=False)  
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=False
    )
    class Meta:  
        db_table = "employee"  

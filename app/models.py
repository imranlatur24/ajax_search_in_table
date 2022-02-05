from django.db import models
from matplotlib.pyplot import cla

# Create your models here.
class EmployeeModel(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_email=models.EmailField()
    emp_salary=models.IntegerField()
    class meta:
        db_table="employee"
    def __str__(self) -> str:
        return self.emp_name

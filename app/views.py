from django.shortcuts import render
from .models import EmployeeModel
# Create your views here.
def search_view(request):
    emp_data = EmployeeModel.objects.all()
    context={
        'emp_data':emp_data
    }
    return render(request,'index.html',context)
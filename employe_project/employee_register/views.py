from django.shortcuts import render,redirect    
from .forms import EmployeeForm
from . models import Employee
# Create your views here.


# retrive and disply all of the employee recordes
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,'employe_list.html',context)

# get and post request for insert and update opration

# if  handle the GET request ========================
def employee_form(request,id=0):
    if request.method =='GET':
            if id == 0:
              form = EmployeeForm()
            else: 
               employeee = Employee.objects.get(pk=id)  #pk  primarykey
               form = EmployeeForm(instance = employeee)
            
            emp_form={
               'form':form
                }
    
            return render(request,'employee_form.html',emp_form)
    
   # else  handle the POST request  =========================
    else:
        # insert opration
        if id == 0:
            form = EmployeeForm(request.POST)
            # update opration
        else:   
            employeee = Employee.objects.get(pk=id)  
            form = EmployeeForm(request.POST,instance =  employeee)
        if form.is_valid():
             form.save()
        return redirect('employe_list')

# it used delecting employee record 
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employe_list')

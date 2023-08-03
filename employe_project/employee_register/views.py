from django.shortcuts import render,redirect    
from .forms import EmployeeForm
from . models import Employee
# Create your views here.



def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,'employe_list.html',context)




def employee_form(request,id=0):
    
    # print(id)
    if request.method =='GET':
            if id == 0:
              form = EmployeeForm()
            else: 
               employeee = Employee.objects.get(pk=id)  
               form = EmployeeForm(instance = employeee)
            
            emp_form={
               'form':form
                }
    
            return render(request,'employee_form.html',emp_form)
    
    else:
   
        if id == 0:
            form = EmployeeForm(request.POST)
            # print(form)u
            
            
        else:   
            employeee = Employee.objects.get(pk=id)  
            form = EmployeeForm(request.POST,instance =  employeee)
            # print(form)
            
        if form.is_valid():
             form.save()
          
        return redirect('employe_list')


def employee_delete(request, id):
    # print(id)
    employee = Employee.objects.get(pk=id) 
    # print(employee)
    employee.delete()
    return redirect('employe_list')


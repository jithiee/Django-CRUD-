
from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_form, name='employee_insert' ),  # get and post request for insert opration
    path('<int:id>/',views.employee_form,name='employee_Update'), # get and request post for update opration 
    path('list/',views.employee_list,name='employee_list'), # get request retrive and display all records 
    
]

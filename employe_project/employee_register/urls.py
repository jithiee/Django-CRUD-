from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),                         # get and post request for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'),                # get and request post for update operation
    path('list/', views.employee_list, name='employe_list'),                       # get request retrieve and display all records
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),       # delete operation
]

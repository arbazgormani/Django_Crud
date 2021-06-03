from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('show_departments/', views.show_departments, name='department'),
    path('add_department/', views.add_department, name='add department'),
    path(
        'edit_department/<int:department_id>/',
        views.edit_department,
        name='department edit'
    ),
    path(
        'update_department/<int:department_id>',
        views.update_department,
        name='department update'
    ),
    path(
        'delete_department/<int:department_id>/',
        views.delete_department,
        name='department delete'
    ),
    path('show_employees/', views.show_employees, name='show employees'),
    path('add_employee/', views.add_employee, name='add employee'),
       path(
        'delete_employee/<int:employee_id>/',
        views.delete_employee,
        name='employee delete'
    ),
    path(
        'edit_employee/<int:employee_id>/',
        views.edit_employee,
        name='edit employee'
    ),
    path(
        'update_employee/<int:employee_id>',
        views.update_employee,
        name='update department'
    ),
]
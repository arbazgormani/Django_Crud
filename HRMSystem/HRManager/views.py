from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm, DepartmentForm  
from employee.models import Employee, Department
# Create your views here.  
def index(request):
    return render(request, 'index.html')


def show_departments(request):
    department_list = Department.objects.all()
    return render(
        request, 'show_departments.html', {'departments': department_list})


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_departments')
            except:
                pass
    else:
        form = DepartmentForm()
    return render(
        request, 'add_department.html')


def edit_department(request, department_id):
    department = Department.objects.get(department_id=department_id)
    return render(
        request, 'edit_department.html', {'department': department})

def update_department(request, department_id):
    department = Department.objects.get(department_id=department_id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect('/show_departments')
    return render(
        request, 'department_edit.html', {'department': department})

def delete_department(request, department_id):
    department = Department.objects.get(department_id=department_id)
    department.delete()
    return redirect('/show_departments')

def show_employees(request):
    employee_list = Employee.objects.all()
    return render(
        request, 'show_employees.html', {'employees': employee_list})

def add_employee(request):
    department_list = Department.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_employees')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(
        request, 'add_employee.html',
        {'departments': department_list})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(eid=employee_id)
    employee.delete()
    return redirect('/show_employees')


def edit_employee(request, employee_id):
    department_list = Department.objects.all()
    employee = Employee.objects.get(eid=employee_id)
    return render(
        request, 'edit_employee.html',
        {'employee': employee,
         'departments': department_list})


def update_employee(request, employee_id):
    department_list = Department.objects.all()
    employee = Employee.objects.get(eid=employee_id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show_employees')
    return render(
        request, 'edit_employee.html',
        {'employee': employee,
         'departments': department_list})




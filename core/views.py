from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, DepartmentForm, CompanyForm
from django.contrib import messages
from .models import Company, Department, Employee


def home(request):
    return redirect('/company')
def employee(request):
    if request.method == 'POST':   
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Employee registrada com sucesso')
            return redirect('/company/employee')
    else:
        form = EmployeeForm()
    return render (request, 'core/user_form.html', {'form':form})

def department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Department registrada com sucesso')
            return redirect('/company/department')
    else:
        form = DepartmentForm()
    return render (request, 'core/department_form.html', {'form':form})


def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Company registrada com sucesso')
            return redirect('/company')
    else:
        form = CompanyForm()
    return render (request, 'core/company_form.html', {'form':form})
    
def show(request):  
    employees = Employee.objects.all()  
    departments = Department.objects.all()
    companys = Company.objects.all()
    return render(request,"core/show.html",{'employees':employees,'departments':departments, 'companys':companys})

def edit(request, id):  
    employee = Employee.objects.get(id=id)
    return render(request,'core/edit.html', {'employee':employee})

def editdepart(request, id):  
    department = Department.objects.get(id=id)
    return render(request,'core/edit.html', {'department':department})

def editcompany(request, id):  
    company = Company.objects.get(id=id)
    return render(request,'core/edit.html', {'company':company})


def updateEmployee(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee) 
    if form.is_valid():  
        form.save()  
        return redirect("company")  
    return render(request, 'core/edit.html', {'employee': employee})  

def updateDepartment(request, id):
    department = Department.objects.get(id=id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect('company')
    return render (request, 'edit_department.html', {'department':department})

def updateCompany(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST, instance=Company)
    if form.is_valid():
        form.save()
        return redirect('company')
    return render (request, 'edit_company.html', {'company':company})


def destroyEmployee(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

def destroyDepartment(request, id):  
    department = Department.objects.get(id=id)  
    department.delete()  
    return redirect("/show")  

def destroyCompany(request, id):  
    company = Company.objects.get(id=id)  
    company.delete()  
    return redirect("/show")  


#Tentei fazer usando classes, pois sei que a repitição de funçoes iguais, não sào boas praticas
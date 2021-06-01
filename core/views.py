from django.shortcuts import render, redirect
from .forms import EmployeeForm, DepartmentForm, CompanyForm


def employee(request):
    if request.method == 'POST':   
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render (request, 'core/user_form.html', {'form':form})

def department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DepartmentForm()
    return render (request, 'core/department_form.html', {'form':form})


def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/company')
    else:
        form = CompanyForm()
    return render (request, 'core/company_form.html', {'form':form})
    

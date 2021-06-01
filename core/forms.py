from django import forms
from django.db.models import fields
from .models import Employee, Department, Company


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'gender','department','phone','salary','age', 'user')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'company', 'status','admin')
    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('logo', 'name', 'legal_number')
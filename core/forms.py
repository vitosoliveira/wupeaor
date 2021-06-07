from django import forms
from django.contrib.auth.models import User
from django.forms.fields import CharField
from .models import Employee, Department, Company
from django.contrib.auth.forms import UserCreationForm


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username',)

class EmployeeForm(forms.ModelForm):
    user = CharField()
    class Meta:
        model = Employee
        fields = ['name', 'lastname', 'gender','department','phone','salary','age', 'user', 'role']

class DepartmentForm(forms.ModelForm):
    # admin = CharField()
    class Meta:
        model = Department
        fields = ('name', 'company', 'status','admin')
    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('logo', 'name', 'legal_number')


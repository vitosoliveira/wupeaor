import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField




# Create your models here.
class ModelsUiuu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        abstract = True


class Company(ModelsUiuu):
    # This is auto created and updated date
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=False)
    legal_number = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return str(self.name)



class Department(ModelsUiuu):
    name = models.CharField(max_length=255, blank=True, null=False)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)
    status = models.BooleanField(blank=True, null=False) 
    admin = models.ForeignKey(User, null=False,on_delete=models.PROTECT )
    # This is auto created and updated date
    def __str__(self):
        return str(self.name)



class Employee(ModelsUiuu):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')

    )
    gender = models.CharField(max_length=1, choices=GENDER)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=False)
    # company = models.ForeignKey(Company, on_delete=models.PROTECT)
    phone = models.CharField(max_length=14, default='Sem Telefone')
    role = models.CharField(max_length=50, default='Sem Atribuição')
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    # This is auto created and updated date



    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.name)

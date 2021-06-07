from django.urls import path
from .views import (employee, 
                     department, 
                     company, 
                     show, 
                     edit,
                     updateEmployee, 
                     destroyEmployee,
                     destroyDepartment,
                     destroyCompany,
                     updateDepartment,
                     updateCompany,
                     home)

app_name = 'core'

urlpatterns = [
   path('',home),
   path('company', company),
   path('company/employee', employee),
   path('company/department', department),
   path('show', show),  
   path('edit/<id>/', edit),
   path('updateEmployee/<id>', updateEmployee),
   path('updateDepart/<id>', updateDepartment),
   path('updateCompany/<id>', updateCompany),
   path('deleteemp/<id>', destroyEmployee),
   path('deletedep/<id>',destroyDepartment),  
   path('deletecomp/<id>',destroyCompany)  


   # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   # path('process-create', ProcessCreate.as_view(), name='process-create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
   # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


]
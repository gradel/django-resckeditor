from django.urls import path
from .views import resources, resource_output

app_name = 'resckeditor'
urlpatterns = [
    path('', resources, name='dialog-data'),
    path('output/', resource_output, name='output'),
]

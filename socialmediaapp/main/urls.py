from django.urls import path

# views from the main application
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
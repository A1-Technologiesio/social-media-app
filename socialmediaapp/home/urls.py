from django.urls import path

# views from the home application
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index, name='index'),
    path('regsitration/', views.registration, name='registration-login')
    
]
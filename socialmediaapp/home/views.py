from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

# Authentication
def registration(request):
    return render(request, 'home/register.html')



import os
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employee(request):
    return render(request, 'happ/employee.html', {})

def employer(request):
    return render(request, 'happ/employer.html', {})
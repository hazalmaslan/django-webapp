from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def search(request):
    return render(request, 'z_lab_engine/search_in_virustotal.html')


def dashboard(request):
    return render(request, 'z_lab_engine/dashboard.html')


def upload(request):
    return render(request, 'z_lab_engine/upload.html')

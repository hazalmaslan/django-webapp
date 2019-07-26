from django.shortcuts import render
from django.views.generic import CreateView
from .models import Hash, SearchTag

# Create your views here.


def search(request):
    return render(request, 'z_lab_engine/search_in_virustotal.html')


def dashboard(request):
    return render(request, 'z_lab_engine/dashboard.html')


def upload(request):
    return render(request, 'z_lab_engine/upload.html')


class HashCreateView(CreateView):
    model = Hash
    fields = ('md5', 'sha1', 'sha256', 'update_tags')


class SearchTagCreateView(CreateView):
    model = SearchTag
    fields = ('tags', 'count')

# TODO: search a way to get the text from the htmls

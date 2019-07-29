from django.shortcuts import render
from django.views.generic import CreateView
from .models import Hash, SearchTag
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout, authenticate
from django.utils.http import is_safe_url
from .forms import UserForm
# Create your views here.


def search(request):
    return render(request, 'z_lab_engine/search_in_virustotal.html')


def dashboard(request):
    data = Hash.objects.all()
    count = Hash.objects.count()

    return render(request, 'z_lab_engine/dashboard.html', {'data': data,
                                                           'count': count})


def upload(request):
    return render(request, 'z_lab_engine/upload.html')


class HashCreateView(CreateView):
    model = Hash
    fields = ('md5', 'sha1', 'sha256', 'update_tags')


class SearchTagCreateView(CreateView):
    model = SearchTag
    fields = ('tags', 'count')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'z_lab_engine/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'z_lab_engine/dashboard.html')
            else:
                return render(request, 'z_lab_engine/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'z_lab_engine/login.html', {'error_message': 'Invalid login'})
    return render(request, 'z_lab_engine/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'z_lab_engine/dashboard.html')
    context = {
        "form": form,
    }
    return render(request, 'z_lab_engine/register.html', context)
# TODO: search a way to get the text from the htmls

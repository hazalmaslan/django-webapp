from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Hash, SearchTag, File
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, SearchTagForm, HashForm, FileForm
from taggit.models import Tag
import time
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
from .utils import helpers, api


class BasicUploadView(View):

    def get(self, request):
        file_list = File.objects.get_queryset()[:10]
        sample_tags_list = Tag.objects.get_queryset()[:5]
        return render(self.request, 'z_lab_engine/upload_file.html', {'files': file_list,})

    def post(self, request):
        form = FileForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            file = form.save(commit=False)
            file_hash = Hash()
            file_hash.sha256 = helpers.sha256(file.file.name)
            file_hash.sha1 = helpers.sha1(file.file.name)
            file_hash.md5 = helpers.md5(file.file.name)
            check_if_hash_exists(file_hash)
            file_hash.save()
            file.file.name = helpers.sha256(file.file.name)
            file.save()

            data = {'is_valid': True, 'name': file.file.name, 'url': file.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def dashboard(request):
    data = Hash.objects.get_queryset()
    count = Hash.objects.count()
    d = dict()
    status = dict()
    status["Malware"] = 0
    status["Benign"] = 0
    status["Not Scanned"] = 0
    for h in data:
        stat = 0
        for tag in h.get_tags():
            if tag in d:
                d[tag] += 1
            else:
                d[tag] = 1

            if tag.lower() == "malware":
                stat = 1
            elif tag.lower() == "benign":
                stat = -1

        if stat == 1:
            status["Malware"] += 1
        elif stat == -1:
            status["Benign"] += 1
        else:
            status["Not Scanned"] += 1

    sorted(d.values(), reverse=False)

    return render(request, 'z_lab_engine/dashboard.html', {'data': data,
                                                           'tags': list(d),
                                                           'values': list(d.values()),
                                                           'status': list(status),
                                                           'stat_num': list(status.values())})


def upload(request):
    sample_tags_list = Tag.objects.get_queryset()[:5]
    form = HashForm(request.POST or None)
    if form.is_valid():
        hash_save = form.save(commit=False)
        hash_lines = request.POST.get('hash_list')
        hash_list = hash_lines.splitlines()
        upload_tags = request.POST.get('upload_tags').split(", ")
        checked_values = request.POST.get('1')
        for h in hash_list:
            if len(h) == 32:
                if Hash.objects.filter(md5=h).exists():
                    hash_obj = Hash.objects.get(md5=h)
                    for tag in upload_tags:
                        hash_obj.upload_tags.add(tag)
                    hash_obj.save()
                else:
                    hash_save.md5 = h
                    hash_save.save()
                    for tag in upload_tags:
                        hash_save.upload_tags.add(tag)
                    hash_save.save()

            elif len(h) == 40:
                if Hash.objects.filter(sha1=h).exists():
                    hash_obj = Hash.objects.get(sha1=h)
                    for tag in upload_tags:
                        hash_obj.upload_tags.add(tag)
                    hash_obj.save()
                else:
                    hash_save.sha1 = h
                    hash_save.save()
                    for tag in upload_tags:
                        hash_save.upload_tags.add(tag)

                    hash_save.save()

            elif len(h) == 64:
                if Hash.objects.filter(sha256=h).exists():
                    hash_obj = Hash.objects.get(sha256=h)
                    for tag in upload_tags:
                        hash_obj.upload_tags.add(tag)
                    hash_obj.save()
                else:
                    hash_save.sha256 = h
                    hash_save.save()
                    for tag in upload_tags:
                        hash_save.upload_tags.add(tag)
                    hash_save.save()
            return render(request, 'z_lab_engine/detail_hash.html', {'tag': checked_values})
    return render(request, 'z_lab_engine/upload.html', {'sample_tags': sample_tags_list})

def detail(request, tagname):

    render(request, 'z_lab_engine/detail.html', {'tag': tagname})


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


def virus_search(request):

    form = SearchTagForm(request.POST or None)
    if form.is_valid():
        search_tag = form.save(commit=False)
        tag = form.cleaned_data['tags']

        if SearchTag.objects.filter(tags=tag).exists():
            search_tag = SearchTag.objects.get(tags=tag)
            count = search_tag.count
            search_tag.count = count + 1
            search_tag.save()

        else:
            search_tag.tags = tag
            search_tag.save()
        return render(request, 'z_lab_engine/detail.html', {'tag': search_tag})
    liste = SearchTag.objects.get_queryset()
    search_tag_dict = dict()
    for el in liste:
        search_tag_dict[el.tags] = el.count

    most_used_tags = sorted(search_tag_dict.items(), key=lambda x: x[1], reverse=True)
    li = []
    for tag in most_used_tags:
        li.append(tag[0])

    sorted_tags = sorted(search_tag_dict, key=lambda x: x[0])

    li2 = []
    for tag in sorted_tags:
        li2.append(tag)

    context = {
        "form": form,
        "mostused": li,
        "recent": search_tag_dict.keys(),
        "sorted": li2,
    }
    return render(request, 'z_lab_engine/search_in_virustotal.html', context)


def clear_database(request):
    for file in File.objects.all():
        file.file.delete()
        file.delete()
    return redirect(request.POST.get('next'))


def check_if_hash_exists(hash_name):
    all_hash_objects = Hash.objects.get_queryset()
    for h in all_hash_objects:
        upload_tags = Tag.objects.filter(id=h.id)
        if h.sha256 == hash_name.sha256:
            for tag in upload_tags:
                hash_name.upload_tags.add(tag)
            h.delete()
            return True
        if h.md5 == hash_name.md5:
            for tag in upload_tags:
                hash_name.upload_tags.add(tag)
            h.delete()
            return True
        if h.sha1 == hash_name.sha1:
            for tag in upload_tags:
                hash_name.upload_tags.add(tag)
            h.delete()
            return True
    return False
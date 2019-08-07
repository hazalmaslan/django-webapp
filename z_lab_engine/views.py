from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Hash, SearchTag
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, SearchTagForm, HashForm
from taggit.models import Tag


def search(request):
    form = SearchTagForm(request.POST or None)
    if form.is_valid():
        search_tag = form.save(commit=False)
        search_tag.tags = request.POST('input')
        if search_tag in SearchTag.objects.get_queryset():
            SearchTag.objects.get(search_tag).count += 1

        search_tag.save()
        return render(request, 'z_lab_engine/detail.html', {'tag': search_tag})
    context = {
        "form": form,
    }
    return render(request, 'z_lab_engine/search_in_virustotal.html', context)


def dashboard(request):
    data = Hash.objects.get_queryset()
    count = Hash.objects.count()
    d = dict()
    for h in data:
        for tag in h.get_tags():
            if tag in d:
                d[tag] += 1
            else:
                d[tag] = 1

    sorted(d.values(), reverse=False)

    return render(request, 'z_lab_engine/dashboard.html', {'data': data,
                                                           'count': count,
                                                           'tags': list(d),
                                                           'values': list(d.values())})


def upload(request):
    sample_tags_list = Tag.objects.get_queryset()[:5]
    form = HashForm(request.POST or None)
    if form.is_valid():
        hash_save = form.save(commit=False)
        hash_lines = request.POST.get('hash_list')
        hash_list = hash_lines.split()
        upload_tags = request.POST.get('upload_tags').split(", ")

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
    return render(request, 'z_lab_engine/upload.html', {'sample_tags': sample_tags_list})

# TODO: DO not forget to check for 2,3 input hashes

class HashCreateView(CreateView):
    model = Hash
    fields = ('md5', 'sha1', 'sha256', 'update_tags')


class SearchTagCreateView(CreateView):
    model = SearchTag
    fields = ('tags', 'count')


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

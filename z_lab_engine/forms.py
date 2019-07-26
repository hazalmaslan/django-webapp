from django import forms
from .models import Hash, SearchTag
from django.contrib.auth.models import User


class HashForm(forms.ModelForm):

    class Meta:
        model = Hash
        fields = ['md5', 'sha1', 'sha256', 'upload_tags']


class SearchTagForm(forms.ModelForm):

    class Meta:
        model = SearchTag
        fields = ['tags', 'count']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
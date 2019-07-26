from django import forms
from .models import Hash, SearchTag


class HashForm(forms.ModelForm):

    class Meta:
        model = Hash
        fields = ['md5', 'sha1', 'sha256', 'upload_tags']


class SearchTagForm(forms.ModelForm):

    class Meta:
        model = SearchTag
        fields = ['tags', 'count']

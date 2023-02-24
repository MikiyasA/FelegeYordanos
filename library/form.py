from django import forms
from django.forms import FileInput

from . models import *



class FolderCreateForm(forms.ModelForm):
    """ to create a folder """
    class Meta:
        model = Folder
        fields = '__all__'
        exclude = ('folder_key', 'parent_key')


class FileCreateForm(forms.ModelForm):
    """A class to create form for Book"""
    class Meta:
        model = File
        # widgets = {'file': FileInput(attrs={'accept': 'application/pdf, audio/*, video/*'})}
        fields = '__all__'
        exclude = ('folder', )


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        labels = {'file_name': "የሚጭኑትን ፋይል ይምረጡ"}
        fields = ['file_name', ]

from django import forms
from django.forms import FileInput

from . models import *


class ContainerCreateForm(forms.ModelForm):
    """A class to create form for Author"""
    class Meta:
        model = Container
        fields = ['name', 'cover']


class ShelfCreateForm(forms.ModelForm):
    """A class to create form for Shelf"""
    class Meta:
        model = Shelf
        fields = ['name', 'container', 'cover']

    def clean_shelf_id(self):
        """The function to check if the Shelf ID is already exist"""
        shelf_id = self.cleaned_data.get('shelf_id')
        for instance in Shelf.objects.all():
            if instance.shelf_id == shelf_id:
                raise forms.ValidationError("Shelf ID assignment error" + shelf_id)
        return shelf_id


class FolderCreateForm(forms.ModelForm):
    """ to create a folder """
    class Meta:
        model = Folder
        fields = '__all__'


class FileCreateForm(forms.ModelForm):
    """A class to create form for Book"""
    class Meta:
        model = File
        # widgets = {'file': FileInput(attrs={'accept': 'application/pdf, audio/*, video/*'})}
        fields = ['file', 'file_name', 'shelf_name', 'edition', 'type',
                  'cover']

    def clean_book_id(self):
        """The function to check if the Book ID is already exist"""
        file_id = self.cleaned_data.get('book_id')
        for instance in File.objects.all():
            if instance.file_id == file_id:
                raise forms.ValidationError("Book ID assignment error" + file_id)
        return file_id


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        labels = {'file_name': "የሚጭኑትን ፋይል ይምረጡ"}
        fields = ['file_name', ]




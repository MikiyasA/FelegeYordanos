import csv

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import resolve

from . form import *
from django.db.models import Q


def container(request):
    """A function to render the view of shelves and searching mechanism """
    title = 'Book Container'
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(name__icontains=q))  # | Q(cover__icontains=q))
        queryset = Folder.objects.filter(mul_q).distinct()
    else:
        queryset = Folder.objects.all()

    context = {
        'title': title,
        'queryset': queryset,
    }
    return render(request, "container.html", context)


def add_container(request):
    """A function to render the view of form to add author"""
    title = 'Add Container'
    heading = "Add Container"
    form = ContainerCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Container successfully added")
        return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
        'heading': heading,
    }
    return render(request, "add.html", context)


def update_container(request, pk):
    """A function to render the view of form to update shelf"""
    title = 'Update Shelf'
    queryset = Container.objects.get(name=pk)
    form = ContainerCreateForm(instance=queryset)
    if request.method == 'POST':
        form = ContainerCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Container successfully updated")
            return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def shelf(request, pk):
    """A function to render the view of shelves and searching mechanism """
    title = 'Book Shelves'
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(name__icontains=q) | Q(container__icontains=q) | Q(cover__icontains=q))
        queryset = Shelf.objects.filter(container=pk).filter(mul_q).distinct()
    else:
        queryset = Shelf.objects.filter(container=pk)

    context = {
        'title': title,
        'queryset': queryset,
    }
    return render(request, "shelf.html", context)


def add_shelf(request):
    """A function to render the view of form to add shelf"""
    title = 'Add Shelf'
    form = ShelfCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Shelf successfully added")
        return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def update_shelf(request, pk):
    """A function to render the view of form to update shelf"""
    title = 'Update Shelf'
    queryset = Shelf.objects.get(name=pk)
    form = ShelfCreateForm(instance=queryset)
    if request.method == 'POST':
        form = ShelfCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Shelf successfully updated")
            return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def add_folder(request):
    """ to create the initial folder """
    title = 'Add Folder'
    form = FolderCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Shelf successfully added")
        return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def add_sub_folder(request):
    """ to create the initial folder """
    title = 'Add Sub Folder'
    form = FolderCreateForm(request.POST, request.FILES)
    if form.is_valid():
        data = Folder()
        data.name = form.cleaned_data['name']
        data.folder_key = get_random_string(8).upper()
        data.parent_key = form.cleaned_data['parent_key']
        data.cover = form.cleaned_data['cover']
        data.save()
        messages.success(request, "Shelf successfully added")
        return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "sub_folder.html", context)


def file(request, pk):
    """A function to render the view of list of books and searching mechanism"""
    title = 'Files'
    """To search books"""
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(file_id__icontains=q) | Q(file__icontains=q) | Q(edition__icontains=q)
                  | Q(file_name__icontains=q) | Q(type__icontains=q) | Q(shelf_name__icontains=q)
                  | Q(cover__icontains=q))
        queryset = File.objects.filter(shelf_name=pk).filter(mul_q).distinct()
    else:
        queryset = File.objects.filter(shelf_name_id=pk)

    form_imp = CsvModelForm(request.POST or None, request.FILES or None)
    if form_imp.is_valid():
        form_imp.save()
        form_imp = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "; ".join(row)
                    row = row.split("; ")
                    shelf_name, _ = Shelf.objects.get_or_create(name=row[4])
                    File.objects.create(
                        file=row[0], file_name=row[1], edition=row[2], type=row[3], shelf_name=shelf_name,
                        cover=row[5],
                    )
        obj.activated = True
        obj.save()
        """file, file_name, edition, type, shelf_name, cover"""

    context = {
        'title': title,
        'queryset': queryset,
        'form_imp': form_imp,
    }
    return render(request, "file.html", context)


def add_file(request):
    """A function to render the view of form to add book"""
    title = 'Add File'
    form = FileCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Book successfully added")
        return redirect('/library/container')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def update_file(request, pk):
    """A function to render the view of form to update the book"""
    title = 'Update File'
    queryset = File.objects.get(book_id=pk)
    form = FileCreateForm(instance=queryset)
    if request.method == 'POST':
        form = FileCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Book successfully updated")
            return redirect('/shelf')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)
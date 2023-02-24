import csv

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import resolve
from django.utils.crypto import get_random_string

from . form import *
from django.db.models import Q


def folders(request):
    """A function to render the view of shelves and searching mechanism """
    title = 'ቤተ መዛግብት'
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(name__icontains=q))  # | Q(cover__icontains=q))
        queryset = Folder.objects.filter(mul_q).distinct()
    else:
        queryset = Folder.objects.filter(parent_key=None)

    context = {
        'title': title,
        'queryset': queryset,
    }
    return render(request, "folder.html", context)


def sub_folders(request, pk):
    """A function to render the view of shelves and searching mechanism """
    folder = Folder.objects.get(folder_key=pk)
    title = 'ማህደር {}'.format(folder.name)
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(name__icontains=q) | Q(created_on__icontains=q) | Q(cover__icontains=q))
        mul_qf = Q(Q(file__icontains=q) | Q(file_name__icontains=q) | Q(type__icontains=q))
        queryset = Folder.objects.filter(parent_key=pk).filter(mul_q).distinct()
        f_queryset = File.objects.filter(folder__folder_key=pk).filter(mul_qf).distinct()
    else:
        queryset = Folder.objects.filter(parent_key=pk)
        f_queryset = File.objects.filter(folder__folder_key=pk)
    context = {
        'title': title,
        'queryset': queryset,
        'value': queryset.values(),
        'pk': pk,
        'f_queryset': f_queryset,
    }
    return render(request, "sub_folder.html", context)


def create_folder(request):
    """ to create the initial folder """
    title = 'አዲስ ማህደር'
    form = FolderCreateForm(request.POST, request.FILES)
    if form.is_valid():
        folder = form.save(commit=False)
        folder.folder_key = get_random_string(8).upper()
        folder.save()
        messages.success(request, "Folder successfully added")
        return redirect('/library/folders')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def update_folder(request, pk):
    title = 'ማህደር ያስተካክሉ'
    queryset = Folder.objects.get(id=pk)
    form = FolderCreateForm(instance=queryset)
    rdct = queryset.parent_key
    if request.method == "POST":
        form = FolderCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Folder successfully Update")
            if rdct:
                return redirect('/library/folders/{}'.format(queryset.parent_key))
            else:
                return redirect('/library/folders')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def add_sub_folder(request, pk):
    """ to create the initial folder """
    title = 'አዲስ ማህደር'
    form = FolderCreateForm(request.POST, request.FILES)
    if form.is_valid():
        data = Folder()
        data.name = form.cleaned_data['name']
        data.folder_key = get_random_string(8).upper()
        data.parent_key = pk
        data.cover = form.cleaned_data['cover']
        data.save()
        messages.success(request, "Folder successfully added")
        return redirect('/library/folders/{}'.format(pk))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)


def add_file(request, pk):
    """A function to render the view of form to add book"""
    title = 'ፊይል ያስገቡ'
    form = FileCreateForm(request.POST, request.FILES)
    folder = Folder.objects.get(folder_key=pk)
    usr = SysUser.objects.get(user_id=request.user)
    print(usr)
    print(folder.id)
    if form.is_valid():
        zfile = form.save(commit=False)
        zfile.folder_id = folder.id
        zfile.upload_by = usr
        zfile.save()
        messages.success(request, "File successfully added")
        return redirect('/library/folders/{}'.format(pk))
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
            messages.success(request, "File successfully updated")
            return redirect('/library/folders')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "add.html", context)

######################################


"""def create_folder(request):
    form = FolderForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Folder Created")
    context = {
        'title': "Create Folder",
        'form': form,
    }
    return render(request, "add.html", context)"""




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

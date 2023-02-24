import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from .forms import *
from django.db.models import Q


def list_gedam(request):
    title = "List gedamat"
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(name__icontains=q) | Q(address__icontains=q))
        gedam = Gedam.objects.filter(mul_q)
    else:
        gedam = Gedam.objects.all()
    context = {
        'title': title,
        'gedam': gedam
    }
    return render(request, 'listGedam.html', context)


def create_gedam(request):
    title = "create_gedam"
    form = GedamCreateForm(request.POST)
    form_detail = GedamDetailForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Gedam created")
        return redirect('listGedam')

    context = {
        'form': form,
        'title': title,
        'form_detail': form_detail
    }

    return render(request, 'addg.html', context)


def update_gedam(request, pk):
    title = "update gedam"
    queryset = Gedam.objects.get(id=pk)
    form = GedamCreateForm(instance=queryset)
    if request.method == 'POST':
        form = GedamCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "gedam updated")
            return redirect('listGedam')
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'addg.html', context)


def list_guzo(request):
    title = "List Guzo"
    today = datetime.date.today()
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(name__icontains=q) | Q(price__icontains=q) | Q(departure_date__icontains=q) |
                  Q(arrival_date__icontains=q))
        guzo = Guzo.objects.filter(mul_q).order_by('departure_date').exclude(departure_date__lt=today)
    else:
        guzo = Guzo.objects.all().order_by('departure_date').exclude(departure_date__lt=today)
    context = {
        'title': title,
        'guzo': guzo
    }
    return render(request, 'listGuzo.html', context)


def create_guzo(request):
    title = "Create Guzo"
    form = GuzoCreateForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Guzo created")
        return redirect('listGuzo')
    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adda.html', context)


def update_guzo(request, pk):
    title = "update guzo"
    queryset = Guzo.objects.get(id=pk)
    form = GuzoCreateForm(instance=queryset)
    if request.method == 'POST':
        form = GuzoCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Guzo update")
            return redirect('listGuzo')
    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adda.html', context)


def list_booking(request):
    title = "List booking"
    today = datetime.date.today()
    if request.method == 'POST':
        value = request.POST.get('keyword')
        value = value.split(',')
        value = value[:-1]
        q = request.POST.get('q')
        mul_q = Q(Q(full_name__icontains=q) | Q(phone_no__icontains=q) | Q(address__icontains=q) |
                  Q(special_request__icontains=q) | Q(booking_id__icontains=q))
        if value:
            booking = BookGuzo.objects.filter(guzo__in=Guzo.objects.filter(id__in=value))\
                .filter(mul_q).order_by('guzo__departure_date', 'full_name')
        else:
            booking = BookGuzo.objects.filter(mul_q).order_by('guzo__departure_date', 'full_name')\
                .exclude(guzo__arrival_date__lt=today)
    else:
        booking = BookGuzo.objects.all().order_by('guzo__departure_date', 'full_name')\
            .exclude(guzo__arrival_date__lt=today)

    context = {
        'title': title,
        'booking': booking,
        'guzo': Guzo.objects.all().exclude(arrival_date__lt=today)
    }

    return render(request, 'listBooking.html', context)


def book_guzo(request):
    title = "Book guzo"
    form = BookGuzoCreateForm(request.POST)
    if form.is_valid():
        data = form.save(commit=False)
        data.booking_id = get_random_string(6).upper()
        data.save()
        messages.success(request, "Guzo Booked")
        return redirect('listBooking')
    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adda.html', context)


def book_guzo_id(request, pk):
    title = "Book gzuo"
    form = BookGuzoCreateByIdForm(request.POST)
    if form.is_valid():
        data = form.save(commit=False)
        data.guzo_id = pk
        data.booking_id = get_random_string(8).upper()
        data.save()
        messages.success(request, "Guzo Booked")
        return redirect('listBooking')
    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adda.html', context)


def update_booking(request, pk):
    title = "Update booking"
    queryset = BookGuzo.objects.get(id=pk)
    form = BookGuzoCreateForm(instance=queryset)
    if request.method == 'POST':
        form = BookGuzoCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated")
            return redirect('listBooking')
    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adda.html', context)


def detail(request, name, pk):
    gedam, guzo, booking = None, None, None
    """guzo = None
    booking = None"""
    if name == 'gedam':
        gedam = Gedam.objects.get(id=pk)
        name = "The Gedam"
    if name == 'guzo':
        guzo = Guzo.objects.get(id=pk)
    if name == 'booking':
        booking = BookGuzo.objects.get(id=pk)
    title = "Detail " + name
    context = {
        'title': title,
        'gedam': gedam,
        'guzo': guzo,
        'booking': booking
    }

    return render(request, 'detail.html', context)

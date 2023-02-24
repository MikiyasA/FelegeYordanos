from django import forms
from .models import *


class DatePicker(forms.DateInput):
    """ to set up django data picker """
    input_type = 'date'


class GedamCreateForm(forms.ModelForm):
    """ To create the form to add Gedam """
    class Meta:
        model = Gedam
        labels = {}
        fields = '__all__'
        exclude = ('updatedAt', 'createdBy')


class GedamDetailForm(forms.ModelForm):
    class Meta:
        model = Gedam
        fields = ['detail']


class GuzoCreateForm(forms.ModelForm):
    class Meta:
        model = Guzo
        fields = '__all__'
        exclude = ('createdAt', 'updatedAt', 'createdBy', 'updatedBy')
        widgets = {'departure_date': DatePicker(), 'arrival_date': DatePicker()}


class BookGuzoCreateForm(forms.ModelForm):
    class Meta:
        model = BookGuzo
        fields = '__all__'
        exclude = ('booking_id', 'createdBy', 'updatedBy')


class BookGuzoCreateByIdForm(forms.ModelForm):
    class Meta:
        model = BookGuzo
        fields = '__all__'
        exclude = ('guzo', 'booking_id', 'createdBy', 'updatedBy')

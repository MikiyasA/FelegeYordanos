from django import forms
from .models import *


class DatePicker(forms.DateInput):
    input_type = 'date'


class ChildCreateForm(forms.ModelForm):
    class Meta:
        model = Child
        labels = {'idno': "መለያ ቁጥር", 'fname': "ስም", 'mname': "የአባት ስም", 'lname': "የአያት ስም", 'mother_name': "የእናት ስም",
                  'c_name': "ክርስትና ስም", 'phone': "ስልክ", 'sex': "ጾታ", 'midb': "ምድብ",
                  'bday': "የትውልድ ቀን", 'nationality': "ዜግነት",
                  'address': "አድራሻ", 'city': "ከተማ",
                  'wereda': "ወረዳ", 'house_no': "የቤት ቁጥር", 'fam_name': "ያአሳዳጊ ስም", 'fam_phone': "ያአሳዳጊ ስልክ",
                  'education_level': "የትምህርት ደረጃ", 'start_date': 'ሰ/ትቤት የጀመሩበት ቀን',
                  'dikuna': "የክህነት መአረግ", 'photo': "ፎቶ"}
        fields = ['idno', 'fname', 'mname', 'lname', 'mother_name', 'c_name', 'phone',
                  'sex', 'bday', 'nationality', 'midb', 'address', 'city', 'wereda', 'house_no',
                  'fam_name', 'fam_phone', 'education_level', 'start_date',
                  'dikuna', 'photo']
        widgets = {'bday': DatePicker(), 'start_date': DatePicker()}

    """def clean_idno(self):
        idno = self.cleaned_data.get('idno')
        for instance in Child.objects.all():
            if instance.idno == idno:
                raise forms.ValidationError("መለያ ቁጥር  " + idno + " ቀድሞ ተይዙአል")
        return idno"""


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        labels = {'file_name': "የሚጭኑበትን ፋይል ይምረጡ"}
        fields = ['file_name', ]


class SearchChildForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Child
        labels = {}
        fields = []


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        labels = {'course_id': "የትምህርቱ መለያ ቁጥር", 'name': "የትምህርቱ ስም", 'lemidb': "ትምህርቱን የሚወስዱ ምድቦች",
                  'attachment': "የትምህርቱ መርጃ መጻህፍት"}
        fields = ['course_id', 'name', 'lemidb', 'attachment']


class MarkCreateForm(forms.ModelForm):
    class Meta:
        model = Mark
        labels = {'student': "ተማሪው",  'course': "የሚሰጠው ትምህርት", 'assessment': "የተከታታይ ግምገማ ውጤት",
                  'final': "የማጠቃለያ ፈተና ውጤት", 'midb': "ምድብ"}
        fields = ['student', 'midb', 'course', 'assessment', 'final']
        widget = {'assessment': forms.ClearableFileInput(attrs={'multiple': True}), }

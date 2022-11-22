from django import forms
from .models import *


class DatePicker(forms.DateInput):
    input_type = 'date'


class MembersCreateForm(forms.ModelForm):
    class Meta:
        model = Members
        labels = {'idno': "መለያ ቁጥር", 'fname': "ስም", 'mname': "የአባት ስም", 'lname': "የአያት ስም", 'mother_name': "የእናት ስም",
                  'c_name': "ክርስትና ስም", 'c_father_name': "የንሰሃ አባት ስም", 'phone': "ስልክ", 'email': "ኢሜል", 'sex': "ጾታ",
                  'bday': "የትውልድ ቀን", 'nationality': "ዜግነት", 'status': "የጋብቻ ሁኔታ", 'rid_no': "የመታወቂያ ቁጥር",
                  'address': "አድራሻ", 'city': "ከተማ",
                  'wereda': "ወረዳ", 'house_no': "የቤት ቁጥር", 'sos_name': "የቅርብ የተጠሪ ስም", 'sos_phone': "የቅርብ የተጠሪ ስልክ",
                  'education_level': "የትምህርት ደረጃ", 'education': "የተመረቁበት ዘርፍ", 'job': "ስራ", 'talent': "ልዩ ሞያ",
                  'activity': "የአገልግሎት ሁኔታ", 'kifl': "የሚያገለግሉበት ክፍል", 'start_date': 'አገልግሎት የጀመሩበት ቀን',
                  'dikuna': "የክህነት መአረግ", 'zemari': "ይዘምራሉ", 'photo': "ፎቶ"}
        fields = ['idno', 'fname', 'mname', 'lname', 'mother_name', 'c_name', 'c_father_name', 'phone', 'email',
                  'sex', 'bday', 'nationality', 'status', 'rid_no', 'address', 'city', 'wereda', 'house_no',
                  'sos_name', 'sos_phone', 'education_level', 'education', 'job', 'talent', 'activity', 'start_date',
                  'dikuna', 'kifl', 'zemari', 'photo']
        widgets = {'bday': DatePicker(), 'start_date': DatePicker()}

    def clean_idno(self):
        idno = self.cleaned_data.get('idno')
        for instance in Members.objects.all():
            if instance.idno == idno:
                raise forms.ValidationError("መለያ ቁጥር  " + idno + " ቀድሞ ተይዙአል")
        return idno


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        labels = {'file_name': "የሚጭኑበትን ፋይል ይምረጡ"}
        fields = ['file_name', ]


class SearchMemberForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Members
        labels = {'idno': "መለያ ቁጥር", 'fname': "ስም", 'mname': "የአባት ስም", 'lname': "የአያት ስም", 'phone': "ስልክ", 'sex': "ጾታ",
                  'education': "የተመረቁበት ዘርፍ", 'job': "ስራ", 'activity': "የአገልግሎት ሁኔታ", 'kifl': "የሚያገለግሉበት ክፍል"}
        fields = []


class MembersUpdateForm(forms.ModelForm):
    class Meta:
        model = Members
        labels = {'idno': "መለያ ቁጥር", 'fname': "ስም", 'mname': "የአባት ስም", 'lname': "የአያት ስም", 'mother_name': "የእናት ስም",
                  'c_name': "ክርስትና ስም", 'c_father_name': "የንሰሃ አባት ስም", 'phone': "ስልክ", 'email': "ኢሜል", 'sex': "ጾታ",
                  'bday': "የትውልድ ቀን", 'nationality': "ዜግነት", 'status': "የጋብቻ ሁኔታ", 'rid_no': "የመታወቂያ ቁጥር",
                  'address': "አድራሻ", 'city': "ከተማ", 'zemari': "ይዘምራሉ",
                  'wereda': "ወረዳ", 'house_no': "የቤት ቁጥር", 'sos_name': "የቅርብ የተጠሪ ስም", 'sos_phone': "የቅርብ የተጠሪ ስልክ",
                  'education_level': "የትምህርት ደረጃ", 'education': "የተመረቁበት ዘርፍ", 'job': "ስራ", 'talent': "ልዩ ሞያ",
                  'dikuna': "የክህነት መአረግ", 'activity': "የአገልግሎት ሁኔታ", 'kifl': "የሚያገለግሉበት ክፍል", 'start_date': 'አገልግሎት የጀመሩበት ቀን', 'photo': "ፎቶ"}
        fields = ['idno', 'fname', 'mname', 'lname', 'mother_name', 'c_name', 'c_father_name', 'phone', 'email',
                  'sex', 'bday', 'nationality', 'status', 'rid_no', 'address', 'city', 'wereda', 'house_no',
                  'sos_name', 'sos_phone', 'education_level', 'education', 'job', 'talent', 'activity', 'start_date',
                  'dikuna', 'kifl', 'zemari', 'photo']
        widgets = {'bday': DatePicker(), 'start_date': DatePicker()}


class GodFatherCreateForm(forms.ModelForm):
    class Meta:
        model = GodFather
        labels = {'name': "ሙሉ ስም", 'phone': "ስልክ", 'address': "አድራሻ", 'debr': "የሚያገለግሉበት ደብር"}
        fields = ['name', 'phone', 'address', 'debr']


class GodFatherUpdateForm(forms.ModelForm):
    class Meta:
        model = GodFather
        fields = ['name', 'phone', 'address', 'debr']


class SearchGodFather(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = GodFather
        labels = {'name': "ሙሉ ስም", 'phone': "ስልክ", 'debr': "የሚያገለግሉበት ደብር"}
        fields = ['name', 'phone', 'debr']


class PropertyCreateForm(forms.ModelForm):
    class Meta:
        model = Property
        labels = {'property_no': "የንብረት ቁጥ", 'property_name': "የንብረት ስም", 'category': "ዘርፍ",
                  'type': "አይነት", 'price': "የተገዛበት ዋጋ", 'quantity': "ብዛት", 'unit_mesnt': "መለኪያ",
                  'condition': "ይዞታ", 'purch_date': "የተገዛበት ቀን", 'exp_date': "የማብቂያ ጊዜ"}
        fields = ['property_no', 'property_name', 'category', 'type', 'price', 'quantity',
                  'unit_mesnt', 'condition', 'purch_date', 'exp_date']
        widgets = {'purch_date': DatePicker(), 'exp_date': DatePicker()}

    def clean_property_no(self):
        property_no = self.cleaned_data.get('property_no')
        for instance in Property.objects.all():
            if instance.property_no == property_no:
                raise forms.ValidationError("የንብረት ቁጥር  " + property_no + " ቀድሞ ተይዙአል")
        return property_no


class SearchPropertyForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Property
        fields = []


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_no', 'property_name', 'category', 'type', 'price', 'quantity',
                  'unit_mesnt', 'condition', 'purch_date', 'exp_date']
        widgets = {'purch_date': DatePicker(), 'exp_date': DatePicker()}


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        labels = {'idno': "መለያ ቁጥር", 'fname': "ስም", 'mname': "የአባት ስም", 'lname': "የአያት ስም",
                  'mother_name': "የእናት ስም",
                  'c_name': "ክርስትና ስም", 'n_father_name': "የንሰሃ አባት ስም", 'phone': "ስልክ", 'email': "ኢሜል", 'sex': "ጾታ",
                  'bday': "የትውልድ ቀን", 'nationality': "ዜግነት", 'status': "የጋብቻ ሁኔታ", 'rid_no': "የመታወቂያ ቁጥር",
                  'address': "አድራሻ", 'city': "ከተማ",
                  'wereda': "ወረዳ", 'house_no': "የቤት ቁጥር", 'sos_name': "የቅርብ የተጠሪ ስም", 'sos_phone': "የቅርብ የተጠሪ ስልክ",
                  'education_level': "የትምህርት ደረጃ", 'education': "የተመረቁበት ዘርፍ",
                  'activity': "የአገልግሎት ሁኔታ", 'start_date': 'ትምህርት የጀመሩበት ቀን', 'photo': "ፎቶ",
                  'current_class': "አሁን ያሉበት ክፍል"}
        fields = ['idno', 'fname', 'mname', 'lname', 'mother_name', 'c_name', 'n_father_name', 'phone', 'email',
                  'sex', 'bday', 'nationality', 'status', 'rid_no', 'address', 'city', 'wereda', 'house_no',
                  'sos_name', 'sos_phone', 'education_level', 'education', 'start_date', 'current_class', 'photo']
        widgets = {'bday': DatePicker(), 'start_date': DatePicker()}

    def clean_idno(self):
        idno = self.cleaned_data.get('idno')
        for instance in Course.objects.all():
            if instance.idno == idno:
                raise forms.ValidationError("መለያ ቁጥር  " + idno + " ቀድሞ ተይዙአል")
        return idno


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        labels = {'idno': "መለያ ቁጥር", 'fname': "ስም", 'mname': "የአባት ስም", 'lname': "የአያት ስም", 'mother_name': "የእናት ስም",
                  'c_name': "ክርስትና ስም", 'n_father_name': "የንሰሃ አባት ስም", 'phone': "ስልክ", 'email': "ኢሜል", 'sex': "ጾታ",
                  'bday': "የትውልድ ቀን", 'nationality': "ዜግነት", 'status': "የጋብቻ ሁኔታ", 'rid_no': "የመታወቂያ ቁጥር",
                  'address': "አድራሻ", 'city': "ከተማ",
                  'wereda': "ወረዳ", 'house_no': "የቤት ቁጥር", 'sos_name': "የቅርብ የተጠሪ ስም", 'sos_phone': "የቅርብ የተጠሪ ስልክ",
                  'education_level': "የትምህርት ደረጃ", 'education': "የተመረቁበት ዘርፍ",
                  'activity': "የአገልግሎት ሁኔታ", 'start_date': 'ትምህርት የጀመሩበት ቀን', 'photo': "ፎቶ",
                  'current_class': "ያሉበት ክፍል"}
        fields = ['idno', 'fname', 'mname', 'lname', 'mother_name', 'c_name', 'n_father_name', 'phone', 'email',
                  'sex', 'bday', 'nationality', 'status', 'rid_no', 'address', 'city', 'wereda', 'house_no',
                  'sos_name', 'sos_phone', 'education_level', 'education', 'start_date', 'current_class', 'photo']
        widgets = {'bday': DatePicker(), 'start_date': DatePicker()}


class FekadCreateForm(forms.ModelForm):
    class Meta:
        model = Fekad
        labels = {'name': "ስም እና መላያ ቁጥር", 'kifl': "ፈቃድ የሚጠይቁበት ክፍል",
                 'start_date': "ፈቃድ የሚጀምርበት ቀን", 'end_date': "ፈቃድ የሚያበቃበት ቀን", 'reason': "የፈቃዱ ምክንያት"}
        fields = ['name', 'kifl', 'start_date', 'end_date', 'reason']
        widgets = {'start_date': DatePicker(), 'end_date': DatePicker()}


class FekadUpdateForm(forms.ModelForm):
    class Meta:
        model = Fekad
        labels = {'name': "ስም እና መላያ ቁጥር", 'kifl': "ፈቃድ የሚጠይቁበት ክፍል", 'approval': "ምርመራ",
                 'start_date': "ፈቃድ የሚጀምርበት ቀን", 'end_date': "ፈቃድ የሚያበቃበት ቀን", 'reason': "የፈቃዱ ምክንያት"}
        fields = ['name', 'kifl', 'start_date', 'end_date', 'reason', 'approval']
        widgets = {'start_date': DatePicker(), 'end_date': DatePicker()}


class SearchFekadForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Fekad
        labels = {}
        fields = []


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {'type': "የአስተያየቱ አይነት", 'comment': "አስተያየቶ", 'contact': "በምን እናግኞ", 'criticality': "ምን ያህል አስቸካይ ነም"}
        fields = ['type', 'comment', 'contact', 'criticality']

        """ def __int__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(CommentCreateForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            inst = super(CommentCreateForm, self).save(commit=False)
            inst.user = self.user
            if commit:
                inst.save()
                self.save_m2m()
            return inst """


class BlogCreateForm(forms.ModelForm):
    """A class to create form for Blog"""
    class Meta:
        model = Blog
        fields = ['title', 'description', 'photo']
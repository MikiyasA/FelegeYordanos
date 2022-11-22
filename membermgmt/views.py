import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import csv
from django.contrib.auth.decorators import login_required

from felegeyordanosdb import settings
from .forms import *
from .models import *
from .decorators import *

from django.db.models import Q

from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from bidi import algorithm as bidialg
from weasyprint import HTML
import tempfile

import datetime
from dateutil.relativedelta import relativedelta


@login_required
@allowed_users('amerar', 'admin')
def homepage(request):
    title = 'Home Page'
    allM = Members.objects.all().count()
    male = Members.objects.filter(sex__contains='ወንድ').count()
    female = Members.objects.filter(sex__contains='ሴት').count()
    active = Members.objects.filter(activity__contains='ያገለግላሉ').count()
    inactive = Members.objects.filter(activity__contains='አያገለግሉም').count()
    diyakon = Members.objects.filter(dikuna__contains='-ዲያቆን').count()
    e_diyakon = Members.objects.filter(dikuna__contains='እጩ ዲያቆን').count()
    kesis = Members.objects.filter(dikuna__icontains='-ቀሲስ').count()
    e_kesis = Members.objects.filter(dikuna__icontains='እጩ ቀሲስ').count()

    allP = Property.objects.all().count()
    new = Property.objects.filter(condition__contains='አዲስ').count()
    used = Property.objects.filter(condition__contains='ያገለገለ').count()
    old = Property.objects.filter(condition__contains='አሮጌ').count()
    tbscrap = Property.objects.filter(condition__contains='የሚወገድ').count()
    cons = Property.objects.filter(type__contains='አላቂ').count()
    rot = Property.objects.filter(type__contains='ቆሚ').count()
    electronics = Property.objects.filter(category__contains='የኤሌክትሮኒክስ የአይቲ እቃዎች').count()
    stationary = Property.objects.filter(category__contains='የጽህፈት መሳሪያቆች').count()
    furniture = Property.objects.filter(category__contains='የቢሮ እቃዎች').count()
    digs = Property.objects.filter(category__contains='የድግስ እቃዎች').count()
    food = Property.objects.filter(category__contains='ምግብ ነክ ቁሶች').count()
    material = Property.objects.filter(category__contains='ንዋየ ቅድሳት').count()

    content = {
        "titel": title,
        "allM": allM, "allP": allP,
        "male": male, "female": female,
        "active": active, "inactive": inactive,
        "diyakon": diyakon, "e_diyakon": e_diyakon, "kesis": kesis, "e_kesis": e_kesis,
        "new": new, "used": used, "old": old, "tbscrap": tbscrap,
        "cons": cons, "rot": rot,
        "electronics": electronics, "digs": digs, "stationary": stationary, "furniture": furniture,
        "food": food, "material": material,
    }
    return render(request, "dashboard.html", content)


@login_required
@allowed_users('amerar', 'leabalat', 'admin')
def mem_dashboard(request):
    header = "Dashboard of Member"
    queryset = Members.objects.all()

    allM = Members.objects.all().count()
    male = Members.objects.filter(sex__icontains='ወንድ').count()
    female = Members.objects.filter(sex__icontains='ሴት').count()
    active = Members.objects.filter(activity__icontains='ያገለግላሉ').count()
    inactive = Members.objects.filter(activity__icontains='አያገለግሉም').count()
    diyakon = Members.objects.filter(dikuna__contains='-ዲያቆን').count()
    e_diyakon = Members.objects.filter(dikuna__contains='እጩ ዲያቆን').count()
    kesis = Members.objects.filter(dikuna__icontains='-ቀሲስ').count()
    e_kesis = Members.objects.filter(dikuna__icontains='እጩ ቀሲስ').count()

    content = {
        "header": header,
        "queryset": queryset,
        "allM": allM,
        "male": male, "female": female,
        "active": active, "inactive": inactive,
        "diyakon": diyakon, "e_diyakon": e_diyakon, "kesis": kesis, "e_kesis": e_kesis,
    }
    return render(request, "dashboardMem.html", content)


@login_required
@allowed_users('leabalat', 'amerar', 'admin')
def list_members(request):
    header = "List of Member"
    form = SearchMemberForm(request.POST or None)
    queryset = Members.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(idno__icontains=q) | Q(fname__icontains=q) | Q(mname__icontains=q)
                  | Q(lname__icontains=q) | Q(phone__icontains=q) | Q(c_name__icontains=q)
                  | Q(job__icontains=q) | Q(talent__icontains=q) | Q(kifl__icontains=q)
                  | Q(activity__icontains=q) | Q(sex__icontains=q))
        queryset = Members.objects.filter(mul_q).distinct()
    else:
        queryset = Members.objects.all()

    if form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="የአባላት ዝርዝር.csv"'
        writer = csv.writer(response)
        writer.writerow(["መለያ ቁጥር", "ስም", "የአባት ስም", "የአያት ስም", "የእናት ስም", "ክርስትና ስም", "የንሰሃ አባት ስም",
                         "ስልክ", "ኢሜል", "ጾታ", "የትውልድ ቀን", "ዜግነት", "የጋብቻ ሁኔታ", "የመታወቂያ ቁጥር", "አድራሻ",
                         "ከተማ", "ወረዳ", "የቤት ቁጥር", "የቅርብ የተጠሪ ስም", "የቅርብ የተጠሪ ስልክ", "የትምህርት ደረጃ",
                         "የተመረቁበት ዘርፍ", "ስራ", "ልዩ ሞያ", "የአገልግሎት ሁኔታ", "አገልግሎት የጀመሩበት ቀን", "የሚያገለግሉበት ክፍል",
                         "የክህነት መአረግ", "ይዘምራሉ", "ፎቶ"])
        instance = Members.objects.all()
        for m in instance:
            writer.writerow([m.idno, m.fname, m.mname, m.lname, m.mother_name, m.c_name, m.c_father_name,
                             m.phone, m.email, m.sex, m.bday, m.nationality, m.status, m.rid_no, m.address,
                             m.city, m.wereda, m.house_no, m.sos_name, m.sos_phone, m.education_level,
                             m.education, m.job, m.talent, m.activity, m.start_date, m.kifl,
                             m.dikuna, m.zemari, m.photo])
        return response

    form_imp = CsvModelForm(request.POST or None, request.FILES or None)
    if form_imp.is_valid():
        form_imp.save()
        form_imp = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(type(reader))
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "; ".join(row)
                    row = row.split("; ")
                    c_father_name, _ = GodFather.objects.get_or_create(name=row[6])
                    Members.objects.create(
                        idno=row[0], fname=row[1], mname=row[2], lname=row[3], mother_name=row[4],
                        c_name=row[5], c_father_name=c_father_name, phone=row[7], email=row[8], sex=row[9],
                        bday=row[10], nationality=row[11], status=row[12], rid_no=row[13], address=row[14],
                        city=row[15], wereda=row[16], house_no=row[17], sos_name=row[18], sos_phone=row[19],
                        education_level=row[20], education=row[21], job=row[22], talent=row[23], activity=row[24],
                        start_date=row[25], kifl=row[26], dikuna=row[27], zemari=row[28], photo=row[29],
                    )
        obj.activated = True
        obj.save()

    context = {
        "form_imp": form_imp,
        "form": form,
        "header": header,
        "queryset": queryset,
    }
    return render(request, "listMember.html", context)


@login_required
@allowed_users('leabalat', 'amerar', 'admin')
def list_f_members(request, pk):
    header = "List of Member"
    form = SearchMemberForm(request.POST or None)
    queryset = Members.objects.filter()

    form_imp = CsvModelForm(request.POST or None, request.FILES or None)
    if form_imp.is_valid():
        form_imp.save()
        form_imp = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(type(reader))
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "; ".join(row)
                    row = row.split("; ")
                    c_father_name, _ = GodFather
                    Members.objects.create(
                        idno=row[0], fname=row[1], mname=row[2], lname=row[3], mother_name=row[4],
                        c_name=row[5], c_father_name=c_father_name, phone=row[7], email=row[8], sex=row[9],
                        bday=row[10], nationality=row[11], status=row[12], rid_no=row[13], address=row[14],
                        city=row[15], wereda=row[16], house_no=row[17], sos_name=row[18], sos_phone=row[19],
                        education_level=row[20], education=row[21], job=row[22], talent=row[23], activity=row[24],
                        start_date=row[25], kifl=row[26], dikuna=row[27], zemari=row[28], photo=row[29],
                    )
        obj.activated = True
        obj.save()

    """ if 'q' in request.GET:
        q = request.GET['q']"""
    p = pk
    if p == "ወንድ" or p == "ሴት":
        mul_q = Q(Q(sex__icontains=p))
    elif p == "ያገለግላሉ" or p == "አያገለግሉም":
        mul_q = Q(Q(activity__icontains=p))
    elif p == "እጩ ዲያቆን" or p == "-ዲያቆን" or p == "እጩ ቀሲስ" or p == "-ቀሲስ":
        mul_q = Q(Q(dikuna__icontains=p))
    queryset = Members.objects.filter(mul_q).distinct()

    if 'q' in request.GET:
        q = request.GET['q']
        mul_a = Q(Q(idno__icontains=q) | Q(fname__icontains=q) | Q(mname__icontains=q)
                  | Q(lname__icontains=q) | Q(phone__icontains=q) | Q(c_name__icontains=q)
                  | Q(job__icontains=q) | Q(talent__icontains=q) | Q(kifl__icontains=q)
                  | Q(activity__icontains=q) | Q(sex__icontains=q))
        queryset = Members.objects.filter(mul_q).filter(mul_a).distinct()
    else:
        queryset = Members.objects.filter(mul_q).distinct()

    if form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="የአባላት ዝርዝር.csv"'
        writer = csv.writer(response)
        writer.writerow(["መለያ ቁጥር", "ስም", "የአባት ስም", "የአያት ስም", "የእናት ስም", "ክርስትና ስም", "የንሰሃ አባት ስም",
                         "ስልክ", "ኢሜል", "ጾታ", "የትውልድ ቀን", "ዜግነት", "የጋብቻ ሁኔታ", "የመታወቂያ ቁጥር", "አድራሻ",
                         "ከተማ", "ወረዳ", "የቤት ቁጥር", "የቅርብ የተጠሪ ስም", "የቅርብ የተጠሪ ስልክ", "የትምህርት ደረጃ",
                         "የተመረቁበት ዘርፍ", "ስራ", "ልዩ ሞያ", "የአገልግሎት ሁኔታ", "አገልግሎት የጀመሩበት ቀን", "የሚያገለግሉበት ክፍል",
                         "የክህነት መአረግ", "ይዘምራሉ", "ፎቶ"])
        instance = Members.objects.filter(mul_q).filter(mul_a)
        for m in instance:
            writer.writerow([m.idno, m.fname, m.mname, m.lname, m.mother_name, m.c_name, m.c_father_name,
                             m.phone, m.email, m.sex, m.bday, m.nationality, m.status, m.rid_no, m.address,
                             m.city, m.wereda, m.house_no, m.sos_name, m.sos_phone, m.education_level,
                             m.education, m.job, m.talent, m.activity, m.start_date, m.kifl,
                             m.dikuna, m.zemari, m.photo])
        return response

    context = {
        "form_imp": form_imp,
        "form": form,
        "header": header,
        "queryset": queryset,
    }
    return render(request, "listMember.html", context)


@login_required
@allowed_users('admin', 'lemezmur', 'amerar')
def list_zemari(request):
    header = "List of Member"
    form = SearchMemberForm(request.POST or None)
    queryset = Members.objects.filter(zemari=True)

    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(idno__icontains=q) | Q(fname__icontains=q) | Q(mname__icontains=q)
                  | Q(lname__icontains=q) | Q(phone__icontains=q) | Q(c_name__icontains=q)
                  | Q(job__icontains=q) | Q(talent__icontains=q) | Q(kifl__icontains=q)
                  | Q(sex__icontains=q))
        queryset = Members.objects.filter(zemari=True).filter(mul_q)
    else:
        queryset = Members.objects.filter(zemari=True)

    if form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="የአባላት ዝርዝር.csv"'
        writer = csv.writer(response)
        writer.writerow(["መለያ ቁጥር", "ስም", "የአባት ስም", "የአያት ስም", "ክርስትና ስም",
                         "ስልክ", "ጻታ" "የሚያገለግሉእት ክፍል", "ስራ", "ልዩ ሞያ"])
        instance = Members.objects.filter(zemari=True)
        for m in instance:
            writer.writerow([m.idno, m.fname, m.mname, m.lname, m.c_name, m.phone, m.sex,
                             m.kifl, m.job, m.talent])
        return response

    context = {

        "form": form,
        "header": header,
        "queryset": queryset,
    }
    return render(request, "zemari.html", context)


@login_required
@allowed_users('leabalat', 'admin')
def add_members(request):
    form = MembersCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "አባል በስትክክል ተመዝግቦል")
        return redirect('/listMembers')
    content = {
        "form_mem": form,
        "title": "Add Member",
    }
    return render(request, "addMember.html", content)


@login_required
@allowed_users('leabalat', 'admin')
def update_member(request, pk):
    queryset = Members.objects.get(idno=pk)
    form = MembersUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = MembersUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "የአባል መረጃ ተስተካክሉል")
            return redirect('/memberDetail/' + queryset.idno)
    context = {
        'form_mem': form
    }
    return render(request, "addMember.html", context)


@login_required
@allowed_users('admin', 'leabalat', 'amerar')
def member_detail(request, pk):
    header = "Detail of Member"
    queryset = Members.objects.get(idno=pk)
    allqueryset = Members.objects.filter(idno=pk)
    context = {
        "header": header,
        "allqueryset": allqueryset,
        "queryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "memDetail.html", context)


@login_required
@allowed_users('admin', 'leabalat')
def member_id(request, pk):
    header = "Detail of Member"
    queryset = Members.objects.get(idno=pk)
    allqueryset = Members.objects.filter(idno=pk)
    context = {
        "header": header,
        "allqueryset": allqueryset,
        "queryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "memid.html", context)


@login_required
@allowed_users('admin', 'leabalat')
def all_member_id(request):
    header = "Detail of Member"
    queryset = Members.objects.all()
    context = {
        "header": header,
        "allqueryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "allmemid.html", context)


@login_required
@allowed_users('admin', 'leabalat')
def to_pdf(request, pk):
    queryset = Members.objects.get(idno=pk)
    allqueryset = Members.objects.filter(idno=pk)
    print_date = datetime.datetime.now()
    exp_date = print_date + relativedelta(years=1)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=ID' + \
                                      str(datetime.datetime.now()) + '.pdf'
    response['Content-Disposition'] = 'binary'
    context = {
        'print_date': print_date,
        'exp_date': exp_date,
        'queryset': queryset,
        'allqueryset': allqueryset,
        'media_url': settings.MEDIA_URL,
    }
    html_str = render_to_string('memid.html', context)
    html = HTML(string=html_str, base_url=request.build_absolute_uri())
    result = html.write_pdf(
        stylesheets=['membermgmt/' + settings.STATIC_URL + 'css/memid.css'],
        presentational_hints=True
    )

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


@login_required
@allowed_users('admin', 'leabalat')
def all_to_pdf(request):
    queryset = Members.objects.all()
    print_date = datetime.datetime.now()
    exp_date = print_date + relativedelta(years=1)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=ID' + \
                                      str(datetime.datetime.now()) + '.pdf'
    response['Content-Disposition'] = 'binary'
    context = {
        'print_date': print_date,
        'exp_date': exp_date,
        'allqueryset': queryset,
        'media_url': settings.MEDIA_URL,
    }
    html_str = render_to_string('allmemid.html', context)
    html = HTML(string=html_str, base_url=request.build_absolute_uri())
    result = html.write_pdf(
        stylesheets=['membermgmt/' + settings.STATIC_URL + 'css/memid.css'],
        presentational_hints=True
    )

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


@login_required
@allowed_users('admin', 'leabalat', 'amerar')
def list_gf(request):
    header = "List of Gof Father"
    form = SearchGodFather(request.POST or None)
    queryset = GodFather.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form
    }
    if request.method == 'POST':
        queryset = GodFather.objects.filter(name__icontains=form['name'].value(),
                                            phone__icontains=form['phone'].value(),
                                            debr__icontains=form['debr'].value(), )

        if form['export_to_CSV'].value():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="የአባላት ዝርዝር.csv"'
            writer = csv.writer(response)
            writer.writerow(["ሙሉ ስም", "ስልክ", "አድራሻ", "የሚያገለግሉበት ደብር"])
            instance = GodFather.objects.all()
            for m in instance:
                writer.writerow([m.name, m.phone, m.address, m.debr])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "listGodFather.html", context)


@login_required
@allowed_users('admin', 'leabalat')
def add_gf(request):
    form = GodFatherCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "ክርስትና አባት በስትክክል ተመዝግቦል")
        return redirect('/listGodFather')
    content = {
        "form_gf": form,
        "title": "Add God Father",
    }
    return render(request, "addGodFather.html", content)


@login_required
@allowed_users('admin', 'leabalat')
def update_gf(request, pk):
    queryset = GodFather.objects.get(name=pk)
    form = GodFatherUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = GodFatherUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "የክርስትና አባት መረጃ ተስተካክሉል")
            return redirect('/listGodFather')
    context = {
        'form_gf': form
    }
    return render(request, "addGodFather.html", context)


@login_required
@allowed_users('admin', 'lenibret', 'amerar')
def property_dashboard(request):
    allP = Property.objects.all().count()
    new = Property.objects.filter(condition__contains='አዲስ').count()
    used = Property.objects.filter(condition__contains='ያገለገለ').count()
    old = Property.objects.filter(condition__contains='አሮጌ').count()
    tbscrap = Property.objects.filter(condition__contains='የሚወገድ').count()

    cons = Property.objects.filter(type__contains='አላቂ').count()
    rot = Property.objects.filter(type__contains='ቆሚ').count()

    electronics = Property.objects.filter(category__contains='የኤሌክትሮኒክስ የአይቲ እቃዎች').count()
    stationary = Property.objects.filter(category__contains='የጽህፈት መሳሪያቆች').count()
    furniture = Property.objects.filter(category__contains='የቢሮ እቃዎች').count()
    digs = Property.objects.filter(category__contains='የድግስ እቃዎች').count()
    food = Property.objects.filter(category__contains='ምግብ ነክ ቁሶች').count()
    material = Property.objects.filter(category__contains='ንዋየ ቅድሳት').count()

    content = {
        "allP": allP,
        "new": new, "used": used, "old": old, "tbscrap": tbscrap,
        "cons": cons, "rot": rot,
        "electronics": electronics, "digs": digs, "stationary": stationary, "furniture": furniture,
        "food": food, "material": material,
    }
    return render(request, "dashboardProp.html", content)


@login_required
@allowed_users('admin', 'lenibret', 'amerar')
def list_property(request):
    header = "List of Property"
    ps_form = SearchPropertyForm(request.POST or None)
    queryset = Property.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(property_no__icontains=q) | Q(property_name__icontains=q) | Q(category__icontains=q)
                  | Q(type__icontains=q) | Q(price__icontains=q) | Q(quantity__icontains=q)
                  | Q(unit_mesnt__icontains=q) | Q(condition__icontains=q) | Q(purch_date__icontains=q)
                  | Q(exp_date__icontains=q))
        queryset = Property.objects.filter(mul_q).distinct()
    else:
        queryset = Property.objects.all()

    if ps_form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Property.csv"'
        writer = csv.writer(response)
        writer.writerow(["የንብረት ቁጥ", "የንብረት ስም", "ዘርፍ", "አይነት", "የተገዛበት ዋጋ", "ብዛት",
                         "መለኪያ", "ይዞታ", "የተገዛበት ቀን", "የማብቂያ ጊዜ"])
        instance = Property.objects.all()
        for p in instance:
            writer.writerow([p.property_no, p.property_name, p.category, p.type, p.price,
                             p.quantity, p.unit_mesnt, p.condition, p.purch_date, p.exp_date])
        return response

    form_imp = CsvModelForm(request.POST or None, request.FILES or None)
    if form_imp.is_valid():
        form_imp.save()
        form_imp = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(type(reader))
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "; ".join(row)
                    row = row.split("; ")
                    Property.objects.create(
                        property_no=row[0], property_name=row[1], category=row[2], type=row[3], price=row[4],
                        quantity=row[5], unit_mesnt=row[6], condition=row[7], purch_date=row[8], exp_date=row[9],
                    )
        obj.activated = True
        obj.save()

    context = {
        "form_imp": form_imp,
        "ps_form": ps_form,
        "header": header,
        "queryset": queryset,
    }

    return render(request, "listProperty.html", context)


@login_required
@allowed_users('admin', 'lenibret', 'amerar')
def list_f_property(request, pk):
    header = "List of Property"
    ps_form = SearchPropertyForm(request.POST or None)
    queryset = Property.objects.all()

    p = pk
    if p == "ቆሚ" or p == "አላቂ":
        mul_p = Q(Q(type__icontains=p))
    elif p == "የኤሌክትሮኒክስ የአይቲ እቃዎች" or p == "የጽህፈት መሳሪያቆች" or p == "የቢሮ እቃዎች" or p == "የድግስ እቃዎች" or p == "ምግብ ነክ ቁሶች" or p == "ንዋየ ቅድሳት":
        mul_p = Q(Q(category__icontains=p))
    elif p == "አዲስ" or p == "ያገለገለ" or p == "አሮጌ" or p == "የሚወገድ":
        mul_p = Q(Q(condition__icontains=p))
    queryset = Property.objects.filter(mul_p).distinct()

    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(property_no__icontains=q) | Q(property_name__icontains=q) | Q(category__icontains=q)
                  | Q(type__icontains=q) | Q(price__icontains=q) | Q(quantity__icontains=q)
                  | Q(unit_mesnt__icontains=q) | Q(condition__icontains=q) | Q(purch_date__icontains=q)
                  | Q(exp_date__icontains=q))
        queryset = Property.objects.filter(mul_p).filter(mul_q).distinct()
    else:
        queryset = Property.objects.filter(mul_p).distinct()

    if ps_form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Property.csv"'
        writer = csv.writer(response)
        writer.writerow(["የንብረት ቁጥ", "የንብረት ስም", "ዘርፍ", "አይነት", "የተገዛበት ዋጋ", "ብዛት",
                         "መለኪያ", "ይዞታ", "የተገዛበት ቀን", "የማብቂያ ጊዜ"])
        instance = Property.objects.filter(mul_p).filter(mul_q)
        for p in instance:
            writer.writerow([p.property_no, p.property_name, p.category, p.type, p.price,
                             p.quantity, p.unit_mesnt, p.condition, p.purch_date, p.exp_date])
        return response

    form_imp = CsvModelForm(request.POST or None, request.FILES or None)
    if form_imp.is_valid():
        form_imp.save()
        form_imp = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(type(reader))
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "; ".join(row)
                    row = row.split("; ")
                    Property.objects.create(
                        property_no=row[0], property_name=row[1], category=row[2], type=row[3], price=row[4],
                        quantity=row[5], unit_mesnt=row[6], condition=row[7], purch_date=row[8], exp_date=row[9],
                    )
        obj.activated = True
        obj.save()

    context = {
        "form_imp": form_imp,
        "ps_form": ps_form,
        "header": header,
        "queryset": queryset,
    }

    return render(request, "listProperty.html", context)

@login_required
@allowed_users('admin', 'lenibret')
def add_property(request):
    p_form = PropertyCreateForm(request.POST or None)
    if p_form.is_valid():
        p_form.save()
        messages.success(request, "አባል በስትክክል ተመዝግቦል")
        return redirect('/listProperty')
    content = {
        "p_form": p_form,
        "title": "Add Property",
    }
    return render(request, "addProperty.html", content)


@login_required
@allowed_users('admin', 'lenibret')
def update_property(request, pk):
    queryset = Property.objects.get(property_no=pk)
    p_form = PropertyUpdateForm(instance=queryset)
    if request.method == 'POST':
        p_form = PropertyUpdateForm(request.POST, instance=queryset)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "የንብረት መረጃ ተስተካክሉል")
            return redirect('/listProperty')
    context = {
        'p_form': p_form
    }
    return render(request, "addProperty.html", context)


@login_required
@allowed_users('admin')
def list_cstudent(request):
    header = "List of Course"
    c_form = SearchPropertyForm(request.POST or None)
    queryset = Course.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "ps_form": c_form
    }

    if request.method == 'POST':
        queryset = Course.objects.filter(property_name__icontains=c_form['name'].value(),
                                         idno__icontains=c_form['name'].value()
                                         )

        if c_form['export_to_CSV'].value():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Property.csv"'
            writer = csv.writer(response)
            writer.writerow(["የንብረት ቁጥ", "የንብረት ስም", "ዘርፍ", "አይነት", "የተገዛበት ዋጋ", "ብዛት",
                             "መለኪያ", "ይዞታ", "የተገዛበት ቀን", "የማብቂያ ጊዜ"])
            instance = Course.objects.all()
            for c in instance:
                writer.writerow([c.property_no, c.property_name, c.category, c.type, c.price,
                                 c.quantity, c.unit_mesnt, c.condition, c.purch_date, c.exp_date])
            return response

    return render(request, "listStudent.html", context)


@login_required
@allowed_users('admin')
def add_cstudent(request):
    c_form = CourseCreateForm(request.POST or None)
    if c_form.is_valid():
        c_form.save()
        messages.success(request, "ተማሪ በስትክክል ተመዝግቦል")
        return redirect('/listStudent')
    content = {
        "c_form": c_form,
        "title": "Add Property",
    }
    return render(request, "addStudent.html", content)


@login_required
@allowed_users('admin')
def update_cstudent(request, pk):
    queryset = Course.objects.get(idno=pk)
    c_form = CourseUpdateForm(instance=queryset)
    if request.method == 'POST':
        c_form = CourseUpdateForm(request.POST, instance=queryset)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, "የተማሪ መረጃ ተስተካክሉል")
            return redirect('/studentDetail/' + queryset.idno)
    context = {
        'c_form': c_form
    }
    return render(request, "addStudent.html", context)


@login_required
@allowed_users('admin')
def student_detail(request, pk):
    header = "Detail of Member"
    queryset = Course.objects.get(idno=pk)
    allqueryset = Course.objects.filter(idno=pk)
    context = {
        "header": header,
        "allqueryset": allqueryset,
        "queryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "stuDetail.html", context)


@login_required
def list_fekad(request):
    header = "List of Fekad"
    form_f = SearchFekadForm(request.POST or None)

    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(kifl__icontains=q) | Q(reason__icontains=q))
        queryset = Fekad.objects.filter(mul_q).distinct()
    else:
        queryset = Fekad.objects.all()

    context = {
        "form_f": form_f,
        "header": header,
        "queryset": queryset,
    }
    return render(request, "listFekad.html", context)


@login_required
def add_fekad(request):
    form_f = FekadCreateForm(request.POST)
    if form_f.is_valid():
        form_f.save()
        messages.success(request, "አባል በስትክክል ተመዝግቦል")

        return redirect('/listFekad')
    content = {
        "form_f": form_f,
        "title": "Add Member",
    }
    return render(request, "addFekad.html", content)


@login_required
@allowed_users('admin', 'amerar', 'fekaj')
def update_fekad(request, pk):
    queryset = Fekad.objects.get(id=pk)
    form = FekadUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = FekadUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/listFekad/')
    context = {
        'form_f': form
    }
    return render(request, "addFekad.html", context)


@login_required
def add_comment(request):
    form_com = CommentCreateForm(request.POST)#, user=request.user)
    if form_com.is_valid():
        form_com.save()
        messages.success(request, "ስለ አስተያየቶ እናመሰግናለን! የሚስተካከለውን በቅርብ ለማስተካከል እንሞክራለን")
        return redirect('/')
    content = {
        "from_com": form_com,
        "title": "Comment"
    }
    return render(request, "comment.html", content)


def about(request):
    return render(request, "about.html")


def footer(request):
    currentYear = datetime.datetime.now()
    print("date" + currentYear)
    return render(request, "footer.html", {"currentYear": currentYear})


def home(request):
    """A function to render the view of home page including post and last added books"""
    title = 'Home'
    queryset = Blog.objects.order_by('-post_date')[:30]
    context = {
        'title': title,
        'queryset': queryset,
    }
    return render(request, "home.html", context)


def post_blog(request):
    """A function to render the view of form for blog post """
    title = "Post Blog"
    form = BlogCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Author successfully added")
        return redirect('/')
    context = {
        'title': title,
        'form': form
    }
    return render(request, "add.html", context)
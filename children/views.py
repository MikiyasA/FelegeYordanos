import csv
import datetime
import tempfile

from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.template.loader import render_to_string
from weasyprint import HTML

from felegeyordanosdb import settings
from membermgmt.decorators import allowed_users
from .forms import *


@login_required
@allowed_users('hitsanat', 'amerar', 'admin')
def children(request):
    return render(request, "dashboardChild.html")


@login_required
@allowed_users('hitsanat', 'amerar', 'admin')
def list_child(request):
    header = "List of Children"
    form = SearchChildForm(request.POST or None)
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(idno__icontains=q) | Q(fname__icontains=q) | Q(mname__icontains=q)
                  | Q(lname__icontains=q) | Q(phone__icontains=q)
                  | Q(midb__icontains=q) | Q(sex__icontains=q))
        queryset = Child.objects.filter(mul_q).distinct()
        aregawi = Child.objects.filter(midb='ቤተ አረጋዊ').filter(mul_q).distinct()
        kidanemhret = Child.objects.filter(midb='ቤተ ኪዳነምህረት').filter(mul_q).distinct()
        medhanealem = Child.objects.filter(midb='ቤተ መድኃኔአለም').filter(mul_q).distinct()
        yohans = Child.objects.filter(midb='ቤተ ዮሐንስ').filter(mul_q).distinct()
    else:
        queryset = Child.objects.all()
        aregawi = Child.objects.filter(midb='ቤተ አረጋዊ')
        kidanemhret = Child.objects.filter(midb='ቤተ ኪዳነምህረት')
        medhanealem = Child.objects.filter(midb='ቤተ መድኃኔአለም')
        yohans = Child.objects.filter(midb='ቤተ ዮሐንስ')

    if form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="የህጻናት ዝርዝር.csv"'
        writer = csv.writer(response)
        writer.writerow(["መለያ ቁጥር", "ስም", "የአባት ስም", "የአያት ስም", "የእናት ስም", "ክርስትና ስም",
                         "ስልክ", "ጾታ", "የትውልድ ቀን", "ዜግነት", "ምድብ", "አድራሻ",
                         "ከተማ", "ወረዳ", "የቤት ቁጥር", "ያአሳዳጊ ስም", "ያአሳዳጊ ስልክ", "የትምህርት ደረጃ",
                         "ሰ/ትቤት የጀመሩበት ቀን", "የክህነት መአረግ", "ፎቶ"])
        instance = Child.objects.filter(mul_q)
        for m in instance:
            writer.writerow([m.idno, m.fname, m.mname, m.lname, m.mother_name, m.c_name,
                             m.phone, m.sex, m.bday, m.nationality, m.midb, m.address,
                             m.city, m.wereda, m.house_no, m.fam_name, m.fam_phone, m.education_level,
                             m.start_date, m.dikuna, m.photo])
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
                    Child.objects.create(
                        idno=row[0], fname=row[1], mname=row[2], lname=row[3], mother_name=row[4],
                        c_name=row[5],  phone=row[6], sex=row[7], bday=row[8], nationality=row[9], midb=row[10], address=row[11],
                        city=row[12], wereda=row[13], house_no=row[14], fam_name=row[15], fam_phone=row[16],
                        education_level=row[17], start_date=row[18], dikuna=row[19], photo=row[20],
                    )
        obj.activated = True
        obj.save()

    context = {
        "form_imp": form_imp,
        "form": form,
        "header": header,
        "queryset": queryset,
        "aregawi": aregawi,
        "kidanemhret": kidanemhret,
        "medhanealem": medhanealem,
        "yohans": yohans,
    }
    return render(request, "listChild.html", context)


@login_required
@allowed_users('hitsanat', 'admin')
def add_child(request):
    heading = "የህጻናት መመዝገቢያ ፎርም"
    form = ChildCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "ህጻኑ በስትክክል ተመዝግቦል")
        return redirect('/children')
    content = {
        "form": form,
        "title": "Add Child",
        "heading": heading,
    }
    return render(request, "addc.html", content)


@login_required
@allowed_users('hitsanat', 'admin')
def update_child(request, pk):
    queryset = Child.objects.get(idno=pk)
    form = ChildCreateForm(instance=queryset)
    if request.method == 'POST':
        form = ChildCreateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "የህጻኑ መረጃ ተስተካክሉል")
            return redirect('/memberDetail/' + queryset.idno)
    context = {
        'form': form
    }
    return render(request, "addc.html", context)


@login_required
@allowed_users('admin', 'hitsanat', 'amerar')
def child_detail(request, pk):
    header = "Detail of Member"
    queryset = Child.objects.get(idno=pk)
    allqueryset = Child.objects.filter(idno=pk)
    context = {
        "header": header,
        "allqueryset": allqueryset,
        "queryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "childDetail.html", context)


@login_required
@allowed_users('admin', 'hitsanat')
def child_id(request, pk):
    header = "Detail of Children"
    queryset = Child.objects.get(idno=pk)
    allqueryset = Child.objects.filter(idno=pk)
    context = {
        "header": header,
        "allqueryset": allqueryset,
        "queryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "childId.html", context)


@login_required
@allowed_users('admin', 'hitsanat')
def all_child_id(request):
    header = "Detail of Member"
    queryset = Child.objects.all()
    context = {
        "header": header,
        "allqueryset": queryset,
        'media_url': settings.MEDIA_URL,
    }
    return render(request, "allchildid.html", context)


@login_required
@allowed_users('admin', 'hitsanat')
def child_to_pdf(request, pk):
    queryset = Child.objects.get(idno=pk)
    allqueryset = Child.objects.filter(idno=pk)
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
    html_str = render_to_string('childId.html', context)
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
@allowed_users('admin', 'hitsanat')
def all_child_to_pdf(request):
    queryset = Child.objects.all()
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
    html_str = render_to_string('allchildid.html', context)
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
@allowed_users('hitsanat', 'admin')
def add_course(request):
    heading = "የህጻናት ትምህርት መመዝገቢያ ፎርም"
    form = CourseCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "የህጻናት ትምህርት በስትክክል ተመዝግቦል")
        return redirect('children')
    content = {
        "form": form,
        "title": heading,
        "heading": heading,
    }
    return render(request, "addc.html", content)


@login_required
@allowed_users('hitsanat', 'amerar', 'admin')
def list_course(request):
    header = "የህጻናት ትምህርት ዝርዝር"
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(course_id__icontains=q) | Q(name__icontains=q) | Q(lemidb__icontains=q)
                  | Q(attachment__icontains=q))
        queryset = Course.objects.filter(mul_q).distinct()
    else:
        queryset = Course.objects.all()

    context = {
        "header": header,
        "queryset": queryset,
    }
    return render(request, "listChildC.html", context)


@login_required
@allowed_users('hitsanat', 'admin')
def add_mark(request):
    heading = "የህጻናት የትምህርት ውጤት መመዝገቢያ ፎርም"
    form = MarkCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "የህጻናት ትምህርት ውጤት በስትክክል ተመዝግቦል")
        return redirect('children')
    content = {
        "form": form,
        "title": heading,
        "heading": heading,
    }
    return render(request, "addc.html", content)


@login_required
@allowed_users('hitsanat', 'amerar', 'admin')
def list_mark(request):
    header = "የህጻናት ትምህርት ዝርዝር"
    form = SearchChildForm(request.POST or None)
    if 'q' in request.GET:
        q = request.GET['q']
        mul_q = Q(Q(assessment__icontains=q)
                  | Q(final__icontains=q) | Q(total__icontains=q) | Q(midb__icontains=q))
        queryset = Mark.objects.filter(mul_q).distinct()
        aregawi = Mark.objects.filter(midb='ቤተ አረጋዊ').filter(mul_q).distinct()
        kidanemhret = Mark.objects.filter(midb='ቤተ ኪዳነምህረት').filter(mul_q).distinct()
        medhanealem = Mark.objects.filter(midb='ቤተ መድኃኔአለም').filter(mul_q).distinct()
        yohans = Mark.objects.filter(midb='ቤተ ዮሐንስ').filter(mul_q).distinct()
    else:
        queryset = Mark.objects.all()
        aregawi = Mark.objects.filter(midb='ቤተ አረጋዊ')
        kidanemhret = Mark.objects.filter(midb='ቤተ ኪዳነምህረት')
        medhanealem = Mark.objects.filter(midb='ቤተ መድኃኔአለም')
        yohans = Mark.objects.filter(midb='ቤተ ዮሐንስ')

    if form['export_to_CSV'].value():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="የህጻናት ውጤት ዝርዝር.csv"'
        writer = csv.writer(response)
        writer.writerow(["ተማሪው", "ምድብ", "የተሰጠው ትምህርት", "የተከታታይ ግምገማ ውጤት", "የማጠቃለያ ፈተና ውጤት", "ድምር ውጤት"])
        instance = Mark.objects.filter(mul_q)
        for m in instance:
            writer.writerow([m.student, m.midb, m.course, m.assessment, m.final, m.total])
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
                    stu = Mark.objects.get_or_create(student=row[0])
                    Mark.objects.create(
                        student=stu, midb=row[1], course=row[2], assessment=row[3], final=row[4],
                        total=row[5],
                    )
        obj.activated = True
        obj.save()

    context = {
        "form_imp": form_imp,
        "form": form,
        "header": header,
        "queryset": queryset,
        "aregawi": aregawi,
        "kidanemhret": kidanemhret,
        "medhanealem": medhanealem,
        "yohans": yohans,
    }
    return render(request, "listChildM.html", context)


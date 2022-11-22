from django.db import models

sex_choice = {
    ('ወንድ', 'ወንድ'),
    ('ሴት', 'ሴት'),
}

dikuna_choice = {
    ('እጩ ዲያቆን', 'እጩ ዲያቆን'),
    ('-ዲያቆን', '-ዲያቆን'),
}
midb_choice = {
    ('ቤተ አረጋዊ', 'ቤተ አረጋዊ'),
    ('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት'),
    ('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'),
    ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ'),
    ('ወጣት', 'ወጣት'),
}


class Child(models.Model):
    idno = models.CharField(primary_key=True, max_length=100, blank=False, unique=True)
    fname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    mname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    lname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    mother_name = models.CharField(max_length=100, blank=False, null=True, unique=False)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=False, null=True)
    sex = models.CharField(max_length=10, blank=False, null=True, choices=sex_choice)
    bday = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    midb = models.CharField(max_length=100, blank=True, null=True, choices=midb_choice)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    wereda = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    fam_name = models.CharField(max_length=100, blank=True, null=True)
    fam_phone = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    dikuna = models.CharField(max_length=50, blank=True, null=True, choices=dikuna_choice)
    photo = models.ImageField(upload_to='media', blank=True, null=True, default='/images/logo.jpg')

    def __str__(self):
        return "{} {} {} - {}".format(self.fname, self.mname, self.lname, self.idno)


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


midb_choices = {
    ('ቤተ አረጋዊ', 'ቤተ አረጋዊ'),
    ('ቤተ ኪዳነምህረት', 'ቤተ ኪዳነምህረት'),
    ('ቤተ መድኃኔአለም', 'ቤተ መድኃኔአለም'),
    ('ቤተ ዮሐንስ', 'ቤተ ዮሐንስ'),
}


class Course(models.Model):
    course_id = models.CharField(max_length=100, blank=False, null=True, unique=True)
    name = models.CharField(primary_key=True, max_length=100, blank=False, unique=True)
    lemidb = models.CharField(max_length=100, blank=False, null=True, unique=True, choices=midb_choices)
    attachment = models.FileField(upload_to='media')

    def __str__(self):
        return self.name


class Mark(models.Model):
    student = models.ForeignKey(Child, blank=True, null=True, on_delete=models.SET_NULL)
    midb = models.CharField(max_length=100, blank=True, null=True, choices=midb_choices)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.SET_NULL)
    assessment = models.IntegerField()
    final = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True, editable=False)

    def save(self):
        """To calclulate total value of mark"""
        self.total = self.assessment + self.final
        return super(Mark, self).save()

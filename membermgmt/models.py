import datetime

from django.db import models
from registration.forms import User


class GodFather(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    debr = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


sex_choice = {
    ('ወንድ', 'ወንድ'),
    ('ሴት', 'ሴት'),
}
activity_choice = {
    ('ያገለግላሉ', 'ያገለግላሉ'),
    ('አያገለግሉም', 'አያገለግሉም'),
}
status_choice = {
    ('ያላገባ', 'ያላገባ'),
    ('ያገባ', 'ያገባ'),
}
kifl_choice = {
    ('ልማት፤ሙያ እና በጎ አድራጎት ክፍል', 'ልማት፤ሙያ እና በጎ አድራጎት ክፍል'),
    ('ትምሕርት ክፍል', 'ትምሕርት ክፍል'),
    ('የአባላት ክብካቤና ግንኙነት ክፍል', 'የአባላት ክብካቤና ግንኙነት ክፍል'),
    ('መዝሙር ጣእመ ዜማ ክፍል', 'መዝሙር ጣእመ ዜማ ክፍል'),
    ('ሕጻናት ክፍል', 'ሕጻናት ክፍል'),
    ('ስነ-ጥበብ ክፍል', 'ስነ-ጥበብ ክፍል'),
    ('መረጃ ጥበብና መዛግብት ድምጸ ወምስል ክፍል', 'መረጃ ጥበብና መዛግብት ድምጸ ወምስል ክፍል'),
    ('ንብረት አስተዳደርና ግዢ ዘርፍ', 'ንብረት አስተዳደርና ግዢ ዘርፍ'),
    ('የሕዝብ ግንኙነት ዘርፍ', 'የሕዝብ ግንኙነት ዘርፍ'),
    ('የዕቅድ ዝግጅት አፈጻጸምና ፕሮጀክት ዘርፍ', 'የዕቅድ ዝግጅት አፈጻጸምና ፕሮጀክት ዘርፍ'),
    ('የሒሳብ አስተዳደር ዘርፍ', 'የሒሳብ አስተዳደር ዘርፍ'),
    ('የመረጃ አደረጃጀትና ትንተና ዘርፍ', 'የመረጃ አደረጃጀትና ትንተና ዘርፍ'),
    ('የጥናትና ምርምር ዘርፍ', 'የጥናትና ምርምር ዘርፍ'),
    ('የሰንበት ት/ቤቱ ቁጥጥርና ክትትል', 'የሰንበት ት/ቤቱ ቁጥጥርና ክትትል'),
    ('የሰንበት ት/ቤቱ ዋና ሰብሳቢ', 'የሰንበት ት/ቤቱ ዋና ሰብሳቢ'),
    ('የሰንበት ት/ቤቱ ጸሃፊ', 'የሰንበት ት/ቤቱ ጸሃፊ'),
    ('የሰንበት ት/ቤቱ ስራ አመራር ጉባኤ አባል', 'የሰንበት ት/ቤቱ ስራ አመራር ጉባኤ አባል'),
}
dikuna_choice = {
    ('እጩ ዲያቆን', 'እጩ ዲያቆን'),
    ('-ዲያቆን', '-ዲያቆን'),
    ('እጩ ቀሲስ', 'እጩ ቀሲስ'),
    ('-ቀሲስ', '-ቀሲስ'),
}


class Members(models.Model):
    idno = models.CharField(max_length=100, blank=False, null=True, unique=True)
    fname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    mname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    lname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    mother_name = models.CharField(max_length=100, blank=False, null=True, unique=False)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    c_father_name = models.ForeignKey(GodFather, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=False, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=False, null=True, choices=sex_choice)
    bday = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=False, null=True, choices=status_choice)
    rid_no = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    wereda = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    sos_name = models.CharField(max_length=100, blank=True, null=True)
    sos_phone = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=300, blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    talent = models.CharField(max_length=500, blank=True, null=True)
    activity = models.CharField(max_length=50, blank=False, null=True, choices=activity_choice)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    kifl = models.CharField(max_length=500, blank=True, null=True, choices=kifl_choice)
    dikuna = models.CharField(max_length=50, blank=True, null=True, choices=dikuna_choice)
    zemari = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media', blank=True, null=True, default='/images/logo.jpg')

    def __str__(self):
        return "{} {} {} ({})".format(self.fname, self.mname, self.lname, str(self.idno), self.photo)


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


type_choice = {
    ('ቆሚ', 'ቆሚ'),
    ('አላቂ', 'አላቂ'),

}
category_choice = {
    ('የኤሌክትሮኒክስ የአይቲ እቃዎች', 'የኤሌክትሮኒክስ/የአይቲ እቃዎች'),
    ('የጽህፈት መሳሪያቆች', 'የጽህፈት መሳሪያቆች'),
    ('የቢሮ እቃዎች', 'የቢሮ እቃዎች'),
    ('የድግስ እቃዎች', 'የድግስ እቃዎች'),
    ('ምግብ ነክ ቁሶች', 'ምግብ ነክ ቁሶች'),
    ('ንዋየ ቅድሳት', 'ንዋየ ቅድሳት'),
}
condition_choice = {
    ('አዲስ', 'አዲስ'),
    ('ያገለገለ', 'ያገለገለ'),
    ('አሮጌ', 'አሮጌ'),
    ('የሚወገድ', 'የሚወገድ'),
}


class Property(models.Model):
    property_no = models.CharField(max_length=100, blank=False, null=True, unique=True)
    property_name = models.CharField(max_length=100, blank=False, null=True)
    category = models.CharField(max_length=100, blank=True, null=True, choices=category_choice)
    type = models.CharField(max_length=100, blank=True, null=True, choices=type_choice)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    unit_mesnt = models.CharField(max_length=100, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=False, null=True, choices=condition_choice)
    purch_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    exp_date = models.CharField(max_length=100, blank=True, null=True)


class_choice = {
    ('ቀዳማይ', 'ቀዳማይ'),
    ('ካልዓይ', 'ካልዓይ'),
    ('ሣልሣይ', 'ሣልሣይ'),
    ('ራብዓይ', 'ራብዓይ'),
}


class Course(models.Model):
    idno = models.CharField(max_length=100, blank=False, null=True, unique=True)
    fname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    mname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    lname = models.CharField(max_length=100, blank=False, null=True, unique=False)
    mother_name = models.CharField(max_length=100, blank=False, null=True, unique=False)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    n_father_name = models.ForeignKey(GodFather, blank=False, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=False, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=False, null=True, choices=sex_choice)
    bday = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=False, null=True, choices=status_choice)
    rid_no = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    wereda = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    sos_name = models.CharField(max_length=100, blank=True, null=True)
    sos_phone = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=300, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    current_class = models.CharField(max_length=100, blank=False, null=True, choices=class_choice)
    photo = models.ImageField(upload_to='media', blank=True, null=True, default='/images/logo.jpg')


fekad_choice = {
    ('ተጠይቁአል', 'ተጠይቁአል'),
    ('ጸድቁአል', 'ጸድቁአል'),
    ('አልጸደቀም', 'አልጸደቀም'),
}
class Fekad(models.Model):
    name = models.ForeignKey(Members, blank=False, on_delete=models.CASCADE)
    kifl = models.CharField(max_length=100, blank=True, null=True, choices=kifl_choice)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    request_date = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)
    reason = models.CharField(max_length=1000, blank=False, null=True)
    approval = models.CharField(max_length=50, default="ተጠይቁአል", choices=fekad_choice)


com_type_choice = {
    ('አስተያየት', 'አስተያየት'),
    ('መስተካከል ያለበት', 'መስተካከል ያለበት'),
    ('መጨመር ያለበት', 'መጨመር ያለበት'),
    ('መዳረሻ ገጽ ጭማሪ ጥያቄ', 'መዳረሻ ገጽ ጭማሪ ጥያቄ'),
    ('ማይሰራ ነገር', 'ማይሰራ ነገር'),
}
criticality_choice = {
    ('አስቸኩይ', 'አስቸኩይ'),
    ('መካከለኛ', 'መካከለኛ'),
    ('ማያስቸኩል', 'ማያስቸኩል'),
}


class Comment(models.Model):
    type = models.CharField(max_length=100, blank=False, null=True, choices=com_type_choice)
    comment = models.CharField(max_length=5000, blank=False, null=True)
    date = models.DateTimeField(auto_now=True, blank=False)
    contact = models.CharField(max_length=1000, blank=True)
    criticality = models.CharField(max_length=1000, blank=True, choices=criticality_choice)
#    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} የተጠየቀበት ቀን - {} ተሰርቱአል - {}".format(self.type, self.criticality, self.date, self.done)


class Blog(models.Model):
    """ Class to post blog """
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=10000, blank=False, null=True)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=True)
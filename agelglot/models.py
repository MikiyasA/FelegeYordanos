from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django_registration.forms import User


class Gedam(models.Model):
    """ Guzo class to save detail information of Gedamat """
    name = models.CharField(max_length=300, blank=False)
    address = models.TextField(blank=True)
    detail = RichTextUploadingField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, null=True)
    # updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Guzo(models.Model):
    """ Guzo class to describe the detail of guzo """
    name = models.CharField(max_length=200, blank=False)
    to = models.ForeignKey(Gedam, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    departure_date = models.DateField(blank=False)
    arrival_date = models.DateField(blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.to)


class BookGuzo(models.Model):
    """ To book selected Guzo """
    guzo = models.ForeignKey(Guzo, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=False)
    phone_no = models.CharField(max_length=30, blank=False)
    address = models.TextField(blank=True, null=True)
    special_request = models.TextField(blank=True, null=True)
    booking_id = models.CharField(max_length=50, blank=False, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.guzo, self.full_name)

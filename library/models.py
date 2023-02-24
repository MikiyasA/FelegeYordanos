from django.db import models
from registration.forms import User


class SysUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.CharField(max_length=10, blank=False, null=False)
    roll = models.CharField(max_length=50, blank=True, null=True)


class Folder(models.Model):
    """ to create foldering system """
    name = models.CharField(max_length=100, blank=False)
    folder_key = models.CharField(max_length=100, blank=False, unique=True)
    parent_key = models.CharField(max_length=100, blank=True, null=True)
    no_of_file = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, default='media/folder.png')
    created_by = models.ForeignKey(SysUser, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class File(models.Model):
    """ class of Book to define entities """
    file = models.FileField(upload_to='media', blank=False, null=True)
    file_name = models.CharField(max_length=1000, blank=True, null=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False)
    type = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def.jpg')
    upload_date = models.DateTimeField(auto_now_add=True, blank=False, editable=False)
    upload_by = models.ForeignKey(SysUser, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "{} -\t- {} \t {} \t {}".format(self.file, self.file_name, self.upload_date, self.upload_by)


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

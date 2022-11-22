from django.db import models


class Container(models.Model):
    """A class to contain all shelves as per category """
    name = models.CharField(primary_key=True, max_length=100, blank=False, null=False, unique=True)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def_cont.jpg')

    def __str__(self):
        return "{}".format(self.name)


class Shelf(models.Model):
    """ class of Shelf to group a files """
    name = models.CharField(primary_key=True, max_length=100, blank=False, unique=True)
    container = models.ForeignKey(Container, blank=True, on_delete=models.CASCADE)
    no_of_books = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def_shelf.jpg')

    def __str__(self):
        return "{}".format(self.name)


class Folder(models.Model):
    """ to create foldering system """
    name = models.CharField(max_length=100, blank=False)
    folder_key = models.CharField(max_length=100, blank=False, unique=True)
    parent_key = models.CharField(max_length=100, blank=False, default=0)
    no_of_file = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def_shelf.jpg')


def book_idno():
    """To generate auto increment book ID """
    prfx = "FL"   # prefix of the ID
    last = File.objects.all().last()
    if not last:
        fl_id = "{}{}".format(prfx, '0001')
        return fl_id
    last = str(last)
    last = last.replace(' - FL', ', ')
    last = last.split(', ')
    last = last[1]
    last = int(last)
    fl_id = "{}{:06d}".format(prfx, (last + 1))
    return fl_id


class File(models.Model):
    """ class of Book to define entities """
    file_id = models.CharField(max_length=45, blank=False, unique=True, editable=False, default=book_idno)
    file = models.FileField(upload_to='media', blank=False, null=True)
    file_name = models.CharField(max_length=1000, blank=False)
    edition = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    shelf_name = models.ForeignKey(Shelf, blank=True, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='media', blank=True, default='media/def.jpg')
    upload_date = models.DateTimeField(auto_now_add=True, blank=False, editable=False)

    def __str__(self):
        return "{} - {}".format(self.file_name, self.file_id)


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

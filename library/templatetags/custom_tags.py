from django import template
register = template.Library()


def extn(file):
    ext = str(file)
    ext = ext.split('.')
    return ext[-1]


register.filter('extn', extn)

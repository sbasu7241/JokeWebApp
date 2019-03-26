from django.contrib import admin
from mysite.models import Student,Contact

# Register your models here.

# Responsible for anything that goes inside the administartion panel

admin.site.register(Student)
admin.site.register(Contact)


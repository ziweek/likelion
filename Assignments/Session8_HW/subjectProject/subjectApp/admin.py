from ast import Sub
from django.contrib import admin

# Register your models here.
from .models import Major, Subject

admin.site.register(Major)
admin.site.register(Subject)
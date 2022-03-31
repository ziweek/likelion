from django.contrib import admin

# Register your models here.
from .models import Person, Ariticle

admin.site.register(Person)
admin.site.register(Ariticle)


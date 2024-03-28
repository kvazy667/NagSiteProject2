from django.contrib import admin

from django.contrib import admin
from .models import project,person

# Register your models here.
admin.site.register(project)
admin.site.register(person)
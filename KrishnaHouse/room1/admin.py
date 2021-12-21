from django.contrib import admin

# from room1.models import BioData
# from room1 import models.BioData
# from . import models.BioData
from .models import BioData

# Register your models here.

class bio(admin.ModelAdmin):
    list_display = ('Name','Age')

admin.site.register(BioData, bio)
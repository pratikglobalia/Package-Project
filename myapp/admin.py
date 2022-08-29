from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Package)

@admin.register(Activity)
class Activity(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'package', 'user']

@admin.register(PurchasePackage)
class ParchasePackageAdmin(admin.ModelAdmin):
    list_display = ['package', 'user', 'created_on']
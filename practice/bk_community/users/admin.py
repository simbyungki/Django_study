from django.contrib import admin
from .models import BKUser

# Register your models here.

class BKUserAdmin(admin.ModelAdmin) : 
    list_display = ('name', 'email', 'password', 'registered_dttm')

admin.site.register(BKUser, BKUserAdmin)
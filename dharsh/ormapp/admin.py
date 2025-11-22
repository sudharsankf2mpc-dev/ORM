from django.contrib import admin

# Register your models here.
from .models import Website,Websiteadmin
admin.site.register(Website,Websiteadmin)
from django.db import models
from django.contrib import admin
class Website(models.Model):
    name=models.CharField(max_length=100)
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=200)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    product_description=models.TextField()
    seller_name=models.CharField(max_length=100)
    seller_contact=models.CharField(max_length=15)
class Websiteadmin(admin.ModelAdmin):
    list_display=['name','product_id','product_name','product_price','product_description','seller_name','seller_contact']  
    

# Create your models here.

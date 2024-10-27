from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
  date_of_birth=models.CharField(max_length=50,primary_key="date_of_birth")
  fathers_name=models.CharField(max_length=70)
  age=models.IntegerField()
  customerid=models.IntegerField()
  accountdetails=models.IntegerField()


class BankloanAdmin(admin.ModelAdmin):
 list_display=('date_of_birth','fathers_name','age','customerid','accountdetails')


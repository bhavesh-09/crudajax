from django.contrib import admin
from .models import CrudUser

# Register your models here.
@admin.register(CrudUser)
class CrudUse(admin.ModelAdmin):
    list_display=('id','name','age')
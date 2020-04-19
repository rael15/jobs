from django.contrib import admin
from .models import Empregos

# Register your models here.

class EmpregosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'empresa', 'data_criacao')

admin.site.register(Empregos, EmpregosAdmin)
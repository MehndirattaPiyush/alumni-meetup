# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Branch
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['name', 'year', 'email'] 
    list_filter = ('year',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Branch)


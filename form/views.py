# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student

# Create your views here.
def index(request):
	context = {}
	return render(request, 'form/index.html', context)
	
class AddStudent(CreateView):
	model = Student
	fields = ["name","year","email","phone","branch"]
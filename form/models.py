# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

import datetime
YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

# Create your models here.
class Branch(models.Model):
	branch = models.CharField(max_length=4)

	class Meta:
		verbose_name_plural = "branches"

	def __str__(self):
		return self.branch


class Student(models.Model):
	name = models.CharField(max_length=250)
	year = models.IntegerField("Year of graduation",
        choices=YEAR_CHOICES,
    )
	email = models.CharField(primary_key=True, max_length= 100)
	phone = models.CharField(max_length=10,  validators=[RegexValidator(
		regex=r'^[789]\d{9}$',
        message="Invalid mobile number",
        code="invalid_mobile"
	)])
	branch = models.ForeignKey(Branch)

	def __str__(self):
			return self.name

	def get_absolute_url(self):
		return reverse('form:index')


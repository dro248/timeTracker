# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class RequestDate(models.Model):
	username = models.CharField(max_length=30)
	timestamp = models.DateTimeField(auto_now_add=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)		
	approval_status = models.CharField(max_length=10)
	sickLeave = models.BooleanField(default=False)
	halfDay = models.BooleanField(default=False)
	# {'PENDING', 'APPROVED', 'DENIED'}

	def approve(self):
		self.approval_status = 'APPROVED'

	def deny(self):
		self.approval_status = 'DENIED'

	def __str__(self):
		return (str(self.username) + " (start:" + str(self.start_date) 
				+ "  -  end:" + str(self.end_date) + ") -- Sick: " + str(self.sickLeave) + " -- "
				+ ("FullDay" if self.halfDay is False else "HalfDay"))

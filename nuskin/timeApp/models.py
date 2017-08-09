# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


# class UserProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()
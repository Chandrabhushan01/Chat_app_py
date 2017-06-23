from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
	message = models.CharField(max_length=250)
	sender = models.ForeignKey(User, related_name='sender')
	reciever = models.ForeignKey(User, related_name='reciever')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s sent by %s" %(self.message, self.sender)
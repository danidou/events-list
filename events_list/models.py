from django.db import models
from django.contrib.auth.models import User

class EventType(models.Model):
	title = models.CharField(max_length=64)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='event_types_images', null=True, blank=True)
	def __str__(self):
		return self.title

class Event(models.Model):
	title = models.CharField(max_length=64)
	description = models.TextField(null=True, blank=True)
	datetime = models.DateTimeField()
	event_type = models.ForeignKey('EventType')
	link = models.URLField()
	image = models.ImageField(upload_to='events_images', null=True, blank=True)
	user = models.ForeignKey(User)
	def __str__(self):
		return self.title
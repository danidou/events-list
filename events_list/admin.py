from django.contrib import admin
from events_list.models import Event
from events_list.models import EventType

admin.site.register(Event)
admin.site.register(EventType)
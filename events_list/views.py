from django.shortcuts import render_to_response
from events_list.models import Event

def list(request):
	e = Event.objects.all()
	return render_to_response('list.html', {'events': e})
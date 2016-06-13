from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index( request ):
	LatestQList = Question.objects.order_by('-create_date')[:5]
	#output = ', '.join( [ q.question_text for q in LatestQList ] )
	template = loader.get_template( 'HelloDJ/index.html' )
	context = {
		'LatestQList': LatestQList,
	}
	return HttpResponse(template.render(context, request))

def Greeting( request, name ):
	return HttpResponse( "Hello %s" % name )

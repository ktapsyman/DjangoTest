from django.conf.urls import url
from . import views

urlpatterns = [
	url( r'^$', views.index, name="index" ),
	url( r'^Greeting/(?P<name>\w+)$', views.Greeting, name="Greetings" )
]

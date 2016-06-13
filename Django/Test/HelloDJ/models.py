from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	create_date = models.DateTimeField('date created')
	def __str__(self):
		return self.question_text
	def IsRecently(self):
		return self.create_date >= timezone.now() - datetime.timedelta(days=1)
class Choice( models.Model ):
	question = models.ForeignKey( Question, on_delete=models.CASCADE )
	choice_text = models.CharField( max_length=200 )
	voites = models.IntegerField( default = 0 )
	def __str__(self):
		return self.choice_text

class Receipt( models.Model ):
	ItemName=models.CharField( max_length=60 )
	ShoppingDate=models.DateField()

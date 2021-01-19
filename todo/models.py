from django.db import models

# Create your models here.
class Todo(models.Model):
	name = models.CharField(max_length=100)
	due_date = models.DateField()

	def __str__(self):
		#return string representation of the model
		return self.name , self.due_date
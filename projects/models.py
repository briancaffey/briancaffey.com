from django.db import models

# Create your models here.



class Project(models.Model):

	name = models.CharField(max_length=50)
	description = models.CharField(max_length=10000)
	date_created = models.DateField(auto_now_add=True)


	def __str__(self):
		return str(self.name)
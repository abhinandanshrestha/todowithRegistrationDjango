from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
	user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) #one to many relationship as we use one user have all the relations with next items in the database
	title= models.CharField(max_length=200)
	description= models.TextField(null=True,blank=True)
	complete= models.BooleanField(default=False)
	created= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['complete'] ##automatically sends completed items to the bottom
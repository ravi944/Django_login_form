from django.db import models

# Create your models here.
class registration_details(models.Model):
	Name = models.CharField( max_length=200)
	your_email = models.EmailField( max_length=200)
	password = models.CharField(max_length=50)
	Phone = models.CharField( max_length=12)

class login_details(models.Model):
	your_email = models.EmailField( max_length=200)
	password = models.CharField(max_length=50)
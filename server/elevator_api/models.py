from django.db import models

# Create your models here.


class carmodel(models.Model):
	"""docstring for ClassName"""
	owner=models.CharField(max_length=100,null=True)
	plateno=models.TextField(null=True)
	model=models.CharField(max_length=100,null=True)

		

	def __str__(self):
		return self.plateno

class statusmodel(models.Model):
	"""docstring for ClassName"""
	status=models.IntegerField(max_length=100,null=True)
	car= models.ForeignKey(carmodel, on_delete=models.CASCADE,null=True)
	

		

	def __str__(self):
		return self.plateno

class ownermodel(models.Model):
	"""docstring for ClassName"""
	fname=models.CharField(max_length=100,null=True)
	lname=models.CharField(max_length=100,null=True)
	mobile=models.CharField(max_length=100,null=True)
	address=models.CharField(max_length=100,null=True)
	city=models.CharField(max_length=100,null=True)
	idtype=models.CharField(max_length=100,null=True)
	idno=models.CharField(max_length=100,null=True)
	gender=models.CharField(max_length=100,null=True)
	car= models.ForeignKey(carmodel, on_delete=models.CASCADE,null=True)



		

	def __str__(self):
		return self.fname + " "+self.lname




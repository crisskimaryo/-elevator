from django.db import models


class contents(models.Model):
	"""docstring for ClassName"""
	sub_title=models.CharField(max_length=100,null=True)
	content=models.TextField(null=True)
	chapter=models.CharField(max_length=100,null=True)
	
	def __str__(self):
		return self.sub_title

class author(models.Model):
	"""docstring for ClassName"""
	firstname=models.CharField(max_length=100,null=True)
	lastname=models.CharField(max_length=100,null=True)
	email=models.CharField(max_length=100,null=True)
	phone=models.CharField(max_length=100,null=True)
	
	def __str__(self):
		return self.firstname

class booksmodel(models.Model):
	"""docstring for ClassName"""
	title=models.CharField(max_length=100,null=True)
	content= models.ForeignKey(contents, on_delete=models.CASCADE,null=True)
	author= models.ForeignKey(author, on_delete=models.CASCADE,null=True)
	extra=models.CharField(max_length=100,null=True, blank=True)
	cover=models.CharField(max_length=100,null=True,blank=True)
	
	def __str__(self):
		return self.title




# class calendarmodel(models.Model):
# 	"""docstring for ClassName"""
# 	name=models.CharField(max_length=100,null=True)
# 	date=models.CharField(max_length=100,null=True)
# 	quota=models.CharField(max_length=100,null=True)	

# 	def __str__(self):
# 		return self.name


# class user(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True) 
# 	fn=models.CharField(max_length=100,null=True)
# 	ln=models.CharField(max_length=100,null=True)
# 	regno=models.CharField(max_length=100,null=True)
# 	prof=models.ImageField(upload_to='prof_img',null=True)
# 	semi =models.CharField(max_length=100,null=True)
# 	mob = models.CharField(max_length=100,null=True)


# 	def __str__(self):
# 		return self.user.username 

	

class carmodel(models.Model):
	"""docstring for ClassName"""
	owner=models.CharField(max_length=100,null=True)
	plateno=models.TextField(null=True)
	model=models.CharField(max_length=100,null=True)

		

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



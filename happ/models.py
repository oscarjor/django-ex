from django.db import models

# Employer class.
class Employer(models.Model):
    name = models.CharField(max_length=200)	
	companyname = models.CharField(max_length=200)
	email = models.IntegerField(max_length=200)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	browser = models.CharField(max_length=1000)
	ip = models.CharField(max_length=200)

	def __str__(self):
		return self.name

# Employee Class.
class Employee(models.Model):	
	name = models.CharField(max_length=200)
	email = models.IntegerField(max_length=200)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)
	browser = models.CharField(max_length=1000)
	ip = models.CharField(max_length=200)

# Task Status Class.
class Task_Status(models.Model):	
	name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)

# Task Class.
class Taks(models.Model):	
	name = models.CharField(max_length=200)
	description = models.IntegerField(max_length=500)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	due_date = models.DateTimeField('Due Date', blank=True, null=True)
	status = models.ForeignKey(Task_Status, blank=True, null=True)
	employee = models.ForeignKey(Employee, blank=True, null=True)

# Event Type
class Event_Type(models.Model):	
	name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)

# Event Class.
class Event(models.Model):	
	eventtype = models.ForeignKey(Event_Type, blank=True, null=True)	
	capture = models.FileField("Image", upload_to="captures/")
	result = models.CharField(max_length=200)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employee = models.ForeignKey(Employee, blank=True, null=True)

# Motivational Quotes Class.
class Quote(models.Model):	
	text = models.CharField(max_length=500)
	author = models.IntegerField(max_length=200)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)

# Motivational Quotes Class.
class Exercise(models.Model):	
	title = models.CharField(max_length=200)
	description = models.IntegerField(max_length=500)
	image = models.FileField("Image", upload_to="exercises/")
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)

# Motivational Habits Class.
class Habit(models.Model):	
	title = models.CharField(max_length=200)
	description = models.IntegerField(max_length=500)
	image = models.FileField("Image", upload_to="exercises/")
	video = models.FileField("Image", upload_to="motivations/", blank=True, null=True)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)

# Motivation and.
class Motivation(models.Model):	
	title = models.CharField(max_length=200)
	description = models.IntegerField(max_length=500)
	image = models.FileField("Image", upload_to="motivations/", blank=True, null=True)
	video = models.FileField("Image", upload_to="motivations/", blank=True, null=True)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)

# Motivational Quotes Class.
class Message(models.Model):	
	employee = models.ManyToManyField(Employee, blank=True, null=True)
	quote = models.ManyToManyField(Quote, blank=True, null=True)
	exercise = models.ManyToManyField(Exercise, blank=True, null=True)
	motivation = models.ManyToManyField(Motivation, blank=True, null=True)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)

# Motivational Quotes Class.
class Sounds(models.Model):	
	name = models.CharField(max_length=200)	
	icon = models.FileField("Image", upload_to="soundicons/")
	sound = models.FileField("Sound", upload_to="sounds/")
	color = models.CharField(max_length=20)
	creation_date = models.DateTimeField('Creation Date', blank=True, null=True)
	employer = models.ForeignKey(Employer, blank=True, null=True)
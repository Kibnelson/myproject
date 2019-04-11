from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your models here.

class PeopleDetail(models.Model):
	
	firstnames = models.CharField(max_length=200)
	surname	= models.CharField(max_length=200)
	bio = models.TextField(max_length=20000,null=True,blank=True)
	email = models.EmailField(max_length=200,null = True,blank=True)
	website = models.URLField(max_length=200,null=True, blank=True)

	headshot = models.ImageField(upload_to='personimage',default='personimage/default.png')
	
	class Meta:
		verbose_name_plural = "Person details"
	
	def __str__(self):
		return self.firstnames +	' , '  + str (self.surname) 

		# + str (self.bio)+ ' | '  + str (self.email) + ' | ' + str(self.website) + '|' 
def image_tag(self):
       return mark_safe('<img src="/personimage/" width="174" height="262" />'  (self.headshot_image))

image_tag.short_description = 'Image'

	
class StaffDetail(models.Model):
	person_id = models.ForeignKey(PeopleDetail, on_delete=models.CASCADE,related_name='person', null=True, blank=True)
	#category = models.CharField(max_length=200)
	CS = 'Core Staff'
	RAF = 'Research Associates And Fellows'
	TSS = 'Technical Support Staff'
	T = 'Trainees'
	A = 'Alumni'
	STAFF_CATEGORY_CHOICES = (
		('CS','Core Staff'),
		('RAF','Research Associates And Fellows'),
		('TSS','Technical Support Staff'),
		('T','Trainees'),
		('A','Alumni'),
		)
	category = models.CharField(max_length = 200, choices = STAFF_CATEGORY_CHOICES)
	#category2 = models.ForeignKey(StaffCategories, on_delete=models.CASCADE,related_name=staffcategories2,null=True,blank=True)
	job_title = models.CharField(max_length=500)
	job_description =models.TextField(max_length=20000,null=True, blank=True)
	appointment_date =models.DateField(max_length=200)
	termination_date =models.DateField(max_length=200,null=True,blank=True)
	is_active =models.BooleanField(default=True)
	def __str__(self):
		return self.job_title + ' | '  + ' | '  + str (self.category) + ' | '  + str (self.job_title) + ' | '  + str (self.job_description) + ' | '  + str (self.appointment_date) + ' | '  + str (self.termination_date) + ' | '  + str (self.is_active) + ' | ' 


class StudentDetail(models.Model):
	person_id= models.ForeignKey(PeopleDetail, on_delete=models.CASCADE,related_name='supervisor', null=True, blank=True)	
	#supervisor = models.ForeignKey(StaffDetail,on_delete=models.CASCADE, related_name='staffperons',null=True,blank=True)
	#firstnames = models.CharField(max_length=200)
	#surname	= models.CharField(max_length=200)
	#supervisor = models.CharField(max_length=200)
	supervisor = models.CharField(max_length=500, null=True, blank=True)
	supervisor_additional = models.CharField(max_length=500, null=True, blank=True)
	institution = models.CharField(max_length=500)
	department = models.CharField(max_length=500, null=True, blank=True)
	thesis_title =models.TextField(max_length=10000)
	Hns = 'Hns'
	MSc = 'MSc'
	PhD = 'PhD'
	ERF = 'ERF'
	DEGREE_CHOICES = (
		('Hns','Hns'),
		('MSc','MSc'),
		('PhD','PhD'),
		('ERF','ERF'),
		)
	degree = models.CharField(max_length = 8, choices = DEGREE_CHOICES)
	
	REGISTRATION_CHOICES = (
		('No','No'),
		('Yes','Yes'),
		)
	currently_registered = models.CharField(max_length = 3, choices = REGISTRATION_CHOICES)
	start_date = models.DateField()
	graduation_date = models.DateField(max_length=200,null=True,blank=True)
	abstract = models.TextField(max_length=20000,null=True, blank=True)
	archivesupload_id =models.CharField(max_length =100,null=True, blank=True)
	class Meta:
		verbose_name_plural = "Student details"


	def __str__(self):
		return self.supervisor + ' | '  + str (self.supervisor) + '|' + str (self.institution) + '|' + str (self.department) +' | '  + str (self.thesis_title)+ ' | ' + str(self.degree) + '|' + str(self.currently_registered) + '|' + str(self.start_date) + '|' + str(self.graduation_date) + '|' + str(self.abstract) + '|' + str(self.archivesupload_id) + '|' 
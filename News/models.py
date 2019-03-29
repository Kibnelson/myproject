from django.db import models

# Create your models here.
class Newsletters(models.Model):
	
	title = models.CharField(max_length=200, null=True, blank=True)
	newsletter_date = models.DateField(null=True, blank=True)
	newsletter_number = models.CharField(max_length=200, null=True, blank=True)
	file =models.FileField(upload_to='newsletters', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Newsletters"

	




from django.db import models
# Create your models here.
class Tsetse(models.Model):
	caseno2 = models.CharField(max_length=50,null=True, blank=True)
	vpn  = models.CharField(max_length=50,null=True, blank=True)
	volume  = models.CharField(max_length=50,null=True, blank=True)
	page	 = models.CharField(max_length=50,null=True, blank=True)
	number_on_page	 = models.CharField(max_length=50,null=True, blank=True)
	capture_day_of_month	 = models.CharField(max_length=50,null=True, blank=True)
	capture_month_year	 = models.CharField(max_length=50,null=True, blank=True)
	capture_year	 = models.CharField(max_length=50,null=True, blank=True)
	experimental_month	 = models.CharField(max_length=50,null=True, blank=True)
	capture_days_since_01011960 = models.CharField(max_length=50,null=True, blank=True)
	disector_code = models.CharField(max_length=50,null=True, blank=True)
	microscope = models.CharField(max_length=50,null=True, blank=True)
	capture_sites = models.CharField(max_length=50,null=True, blank=True)



	class Meta:
		verbose_name_plural = "Tsetse data"
	#def __str__(self):
	#	return self.rainfall_mm +' | '+ str (self.temperature_degrees_celcius) +' | '+ str (self.period)  
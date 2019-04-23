from django.contrib import admin

from .models import Tsetse
from import_export.admin import ImportExportModelAdmin
from TRAP.resources import TsetseResource
# Register your models here.


class TsetseAdmin(ImportExportModelAdmin):
	list_display = ('caseno2','vpn','volume','page','number_on_page','capture_day_of_month','capture_month_year','capture_year','experimental_month','capture_days_since_01011960','disector_code','microscope','microscope','capture_sites')
	list_filter = ['capture_year','capture_month_year','capture_day_of_month']
	list_per_page =100
	

	
	resource_class = TsetseResource #Configure the resource class

admin.site.register(Tsetse,TsetseAdmin)


from django.contrib import admin
from .models import Newsletters
# Register your models here.

class NewslettersAdmin(admin.ModelAdmin):
	list_display = ('id','title','newsletter_date','newsletter_number','file','created_at') #
	ordering =	['newsletter_date']
	list_filter =['newsletter_date']
	list_per_page = 15

admin.site.register(Newsletters, NewslettersAdmin)
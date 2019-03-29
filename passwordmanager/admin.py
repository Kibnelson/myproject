from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
	list_display = ('id','account_name','username','password','created_at','updated_at')
	ordering =	['id']
	search_fields =('account_name','username')

admin.site.register(Account, AccountAdmin)
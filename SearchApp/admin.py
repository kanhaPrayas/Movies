from django.contrib import admin
from .models import *
# Register your models here.
class search_app_admin_users (admin.ModelAdmin):
    list_per_page = 100
    search_fields = ['name','email_id'] 

class search_app_admin_movies(admin.ModelAdmin):
    list_per_page = 100
    search_fields = ['name','director'] 

admin.site.register(Users, search_app_admin_users)
admin.site.register(Movies, search_app_admin_movies)
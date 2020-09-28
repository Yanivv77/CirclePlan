from django.contrib import admin
from .models import Instructor

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date',)
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 40
    exclude = ['description']
 

admin.site.register(Instructor,InstructorAdmin)





from django.contrib import admin
from .models import Yashuv

from attendance.models import Circle


class YashuvAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    #list_filter = (name)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Yashuv,YashuvAdmin) 

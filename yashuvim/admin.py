from django.contrib import admin
from .models import Yashuv

class YashuvAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name')
    #list_filter = ('realtor',)
    search_fields = ('name',)
    list_per_page = 25
    
    

admin.site.register(Yashuv,YashuvAdmin) 
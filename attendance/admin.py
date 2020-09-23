from django.contrib import admin

from .models import Member, Circle, Meeting, Participation

class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name','yashuv')
    list_filter = ('yashuv',)
    search_fields = ('name',)
    
admin.site.register(Member,MemberAdmin) 


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
   list_display = ('title','instructor','yashuv','is_active','team',)
   list_display_links = ('title',)  
   search_fields = ('title','yashuv',)
   list_filter = ('yashuv','instructor',)
    



@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('circle', 'date', 'time')


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'member', 'attended')



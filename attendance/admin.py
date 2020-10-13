from .models import Member, Circle, Meeting, Participation
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator








class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name','yashuv','id')
    list_filter = ('yashuv',)
    search_fields = ('full_name',)
    exclude = ['description',]
    
admin.site.register(Member,MemberAdmin) 


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
   list_display = ('title','instructor','yashuv','is_active','participates')
   list_display_links = ('title',)  
   search_fields = ('title',)
   list_filter = ('yashuv','instructor',)
   exclude = ['description']
   


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('circle', 'date_time', )
    search_fields = ['circle__title','circle__auth_user ']
    exclude = ['description']

'''
@admin.register(Participation)   
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('meeting','member')
'''   







class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups',)}),
        (_('Important dates'), {'fields': ( 'date_joined',)}),
    )


class CustomGroupAdmin(GroupAdmin):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            qs = qs.exclude(codename__in=(
                'add_permission',
                'change_permission',
                'delete_permission',

                'add_contenttype',
                'change_contenttype',
                'delete_contenttype',

                'add_session',
                'delete_session',
                'change_session',

                'add_logentry',
                'change_logentry',
                'delete_logentry',
            ))
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super(GroupAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)
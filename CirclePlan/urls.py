from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('', include('accounts.urls')),

    path('circles/', include('attendance.urls')),
   
    path('yashuvim/', include('yashuvim.urls')),

    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

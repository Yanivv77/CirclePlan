from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:circle_id>/',views.circle, name='circle'),
    path('<int:circle_id>/<int:meeting_id>/',views.meeting, name='meeting')
    
   
] 
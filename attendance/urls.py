from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:circle_id>/',views.circle, name='circle')
    
   
] 
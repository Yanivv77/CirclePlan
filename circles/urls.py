from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminCircles, name='adminCircles'),
    path('<int:circle_id>/',views.adminCircle, name='adminCircle'),
    path('<int:circle_id>/<int:meeting_id>/',views.adminMeeting, name='adminMeeting'),
    #path('<int:circle_id>/<int:pk>/att/', views.MeetingViewSet.as_view({'post':'att'}), name='MeetingViewSet'),
    path('search' , views.search, name= 'search'),
] 
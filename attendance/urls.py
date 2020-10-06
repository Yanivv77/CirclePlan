from django.urls import path
from . import views
circle_detail = views.CircleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:circle_id>/',views.circle, name='circle'),
    path('<int:circle_id>/<int:meeting_id>/',views.meeting, name='meeting'),
    path('<int:circle_id>/<int:pk>/att/', views.MeetingViewSet.as_view({'post':'att'}), name='MeetingViewSet'),
    path('circle/<int:pk>/', circle_detail, name='circle-detail'),
]

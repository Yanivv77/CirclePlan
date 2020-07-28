from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='yashuvim'),
    path('<int:yashuv_id>',views.yashuv, name='yashuv'),
    path('search' , views.search, name= 'search'),
] 
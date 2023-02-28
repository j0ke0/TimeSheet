
from . import views
from django.urls import path

app_name = 'tim'
urlpatterns = [
    path('', views.home, name='home'),
    path('dept1/', views.dept1, name='dept1'),
    path('dept2/', views.dept2, name='dept2'),
    path('dept3/', views.dept3, name='dept3'),
    
]

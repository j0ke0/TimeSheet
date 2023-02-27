
from . import views
from django.urls import path

app_name = 'tim'
urlpatterns = [
    path('', views.home, name='home'),
    path('dept1/', views.dept1, name='dept1'),
    
]

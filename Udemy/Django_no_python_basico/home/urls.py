from django.urls import path
from . import views

# HTTP Request <-> HTTP Response
# MVT (MVC)

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
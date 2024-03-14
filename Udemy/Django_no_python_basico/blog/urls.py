from django.urls import path
from blog import views

# HTTP Request <-> HTTP Response
# MVT (MVC)

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
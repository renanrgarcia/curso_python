from django.urls import path
from . import views

app_name = 'blog'

# blog/
# https://docs.djangoproject.com/en/5.0/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]

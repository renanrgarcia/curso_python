from django.urls import path
from . import views

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]

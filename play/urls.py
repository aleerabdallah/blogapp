from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('posts/', views.posts, name='posts'),
  path('post/<slug:slug>/', views.post, name='post_detail'),
  path('register/', views.register, name="register"),
  path('login/', views.login_view, name="login"),
]
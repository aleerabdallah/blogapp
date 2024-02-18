from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('posts/', views.posts, name='posts'),
  path('post/<int:id>/', views.post, name='post'),
  path('register/', views.register, name="register"),
  path('login/', views.login_view, name="login"),
  # path('todoapp/', views.todoHome, name="todo-home"),
]
from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('posts/', views.posts, name='posts'),
  path('post/<int:id>/', views.post, name='post'),
  path('test/', views.test, name='test'),
  path('register/', views.register, name="register"),
  path('todolists/', views.todolist, name="todolist"),
  path('todolists/add', views.addtodo, name="addtodo"),
  path('todolists/update/<int:id>/', views.updatetodolist, name="update"),
  path('todolists/delete/<int:id>/', views.deletetodo, name="delete"),
  path('login/', views.login_view, name="login"),
  path('todoapp/', views.todoHome, name="todo-home"),
]
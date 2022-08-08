from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('todos/', views.todos_index, name='todos_index'),
  path('todos/create/', views.TodoCreate.as_view(), name='todos_create'),
  path('accounts/signup/', views.signup, name='signup')
]
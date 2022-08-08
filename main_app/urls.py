from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('todos/', views.todos_index, name='todos_index'),
  path('accounts/signup/', views.signup, name='signup')
]
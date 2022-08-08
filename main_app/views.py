from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Importance,Todo
# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def todos_index(request):
  return render(request, 'todo/index.html')

class TodoCreate(CreateView):
  model = Todo
  fields = ['task','description']
  success_url = '/todos/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('todos_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
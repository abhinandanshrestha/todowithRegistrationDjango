from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
# Create your views here.

class TaskList(ListView): #by default looks for templates/base/task_list.html
	model = Task 
	context_object_name = 'tasks'

class TaskDetail(DetailView): #by default looks for templates/base/task_detail.html
	model = Task
	context_object_name = 'task'
	template_name ='base/task.html'

class TaskCreate(CreateView): #by default looks for templates/base/task_form.html
	model = Task
	fields = '__all__' #fires all the modelForms
	success_url = reverse_lazy('tasks') #after success re-directs to url 'tasks'

class TaskUpdate(UpdateView): #by default looks for templates/base/task_form.html
	model = Task
	fields = '__all__' #fires all the modelForms
	success_url = reverse_lazy('tasks') #after success re-directs to url 'tasks'

class TaskDelete(DeleteView):
	model = Task
	context_object_name = 'task'
	success_url = reverse_lazy('tasks')

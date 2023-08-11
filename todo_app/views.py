from typing import Any, Dict, List

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView, View
from django.views.generic.edit import CreateView, FormView

from todo_app.forms import TaskForm
from todo_app.models import TaskModel


class TaskListView(ListView): # show tasks - list view
    model = TaskModel
    template_name = 'show_task.html'
    context_object_name = 'tasks' 
    
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)
    
class TaskFormView(CreateView): # add task
    model = TaskModel
    template_name =  'home.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_task')
    
class TaskUpdateView(UpdateView): 
    model = TaskModel
    template_name =  'home.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_task')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'delete_con.html'
    success_url = reverse_lazy('show_task')
    

class TaskCompletedListView(ListView):
    model = TaskModel
    template_name = 'completed_task.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)
    
    
class CompleteTaskView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(TaskModel, pk=kwargs['pk'])
        task.is_completed = True
        task.save()
        return HttpResponseRedirect(reverse_lazy('completed_task'))

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from webapp.form import TaskForm
from webapp.models.task import Task

class TaskAddView(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'task_create.html', context={'form': form})
        else:
            task = form.save()
            return redirect('task_detail', pk = task.pk)


class TaskDetailView(TemplateView):
    template_name = 'task.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk = kwargs['pk']),
        return context

class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk = kwargs['pk'])
        context['form'] = TaskForm(instance = context['task'])
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_update.html', context={'form': form, 'task': task})


class TaskDeleteView(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk = kwargs['pk'])
        return context

    def post(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')




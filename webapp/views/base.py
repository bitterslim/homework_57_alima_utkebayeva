from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context

# def index_view(request: WSGIRequest):
#     task = Task.objects.all()
#     context = {
#         'task' : task
#     }
#     return render(request, 'index.html', context=context)
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context

class IndexRedirectView(RedirectView):
    pattern_name = 'index'

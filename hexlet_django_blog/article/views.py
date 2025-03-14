from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class ArticlesHomePageView(View):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'articles'
        return context

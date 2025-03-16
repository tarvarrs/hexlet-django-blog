from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

# Create your views here.
class ArticlesHomePageView(View):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'articles'
        return context
    
    def get(self, request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')

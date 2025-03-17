from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

from hexlet_django_blog.article.models import Article
# Create your views here.

class IndexView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'articles'
        return context
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})
        # return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')

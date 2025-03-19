from django.shortcuts import render, get_object_or_404
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


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article})


# class ArticleCommentsView(View):

#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

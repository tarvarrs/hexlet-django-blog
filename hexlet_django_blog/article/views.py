from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.contrib import messages
from .forms import ArticleForm
from hexlet_django_blog.article.models import Article


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



class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            # messages.add_message(request, messages.SUCCESS, "Статья успешно добавлена.")
            messages.success(request, "Статья успешно добавлена.")
            form.save()
            return redirect('article')
        return render(request, 'articles/create.html', {'form': form})

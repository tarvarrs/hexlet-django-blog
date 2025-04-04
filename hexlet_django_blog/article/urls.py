from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormEditView, ArticleFormDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='article'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='article_delete'),
    path('<int:id>/', ArticleView.as_view(), name='articleGet'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    # path('<int:article_id>/comments/<int:id>', ArticleCommentsView.as_view()),
    # path('<str:tags>/<int:article_id>/', views.index, name='article'),
]
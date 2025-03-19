from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView # , ArticleCommentsView

urlpatterns = [
    path('', IndexView.as_view(), name='article'),
    path('<int:id>/', ArticleView.as_view(), name='articleGet'),
    # path('<int:article_id>/comments/<int:id>', ArticleCommentsView.as_view()),
    # path('<str:tags>/<int:article_id>/', views.index, name='article'),
]
from django.urls import path
from hexlet_django_blog.article.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='article'),
    # path('<str:tags>/<int:article_id>/', views.index, name='article'),
]
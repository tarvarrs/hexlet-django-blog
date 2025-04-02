from django.forms import CharField, ModelForm
from .models import Article

class ArticleForm(ModelForm):
    body = CharField(
        max_length=100,
    )
    class Meta:
        model = Article
        fields = ['name', 'body']

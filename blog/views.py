from django import forms
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import HttpResponseRedirect


# Create your views here.

def article_index(request):
    articles = Article.objects.all().order_by('-pub_date')
    context = {"articles":articles}
    return render(request, 'blog/article_index.html', context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article':article}
    return render(request, 'blog/article_detail.html', context)
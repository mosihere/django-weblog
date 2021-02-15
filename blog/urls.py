from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_index, name='index'),
    path('<int:pk>/', views.article_detail, name='detail'),
]

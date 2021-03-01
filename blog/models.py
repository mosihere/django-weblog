from django.db import DefaultConnectionProxy, models
from django.db.models.query_utils import PathInfo
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:180] + ' ...'

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk":self.pk})
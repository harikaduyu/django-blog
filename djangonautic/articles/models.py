from django.conf import settings
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'

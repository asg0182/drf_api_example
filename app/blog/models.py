from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostManager(models.Manager):

    def get_qs_by_user(self, user):
        return self.get_queryset().filter(author=user)


class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-updated']

    title = models.CharField(max_length=255, verbose_name='Наименование')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True, verbose_name='категории')

    objects = PostManager()

    def __str__(self):
        return self.title

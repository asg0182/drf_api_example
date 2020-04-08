from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailVIew(DetailView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'


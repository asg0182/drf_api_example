

from rest_framework import mixins, generics, filters, permissions

from .serializers import PostSerializer
from blog.models import Post


class PostListView(generics.ListAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    search_fields = ('title', 'categories__name')
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

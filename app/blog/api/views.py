

from rest_framework import mixins, generics, filters, permissions, views, authentication
from  rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post


class HealthCheck(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request, format=None):
        return Response('APP is up state')


class PostListView(generics.ListAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    search_fields = ('title', 'categories__name')
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

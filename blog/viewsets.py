from rest_framework import viewsets, permissions

from blog.models import Post
from blog.permissions import isOwnerOrReadOnly
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
      isOwnerOrReadOnly
    ]

   def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


    def get_permissions(self):
        if self.request.method == 'create':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
        elif self.action.method == 'destroy':
            return [permissions.IsAuthenticated()]
        elif self.action.method == 'update':
            return [permissions.IsAuthenticated()]
        elif  self.action.method == 'partial_update':
            return [permissions.IsAuthenticated()]
        elif self.action.method == 'list':
            return [permissions.IsAuthenticated()]


def perform_create(self, serializer):
    serializer.save(author=self.request.user)



    @permission_classes([permissions.IsAuthenticated])
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-fecha_publicacion')
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

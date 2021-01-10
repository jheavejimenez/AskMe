from rest_framework import generics
from Pregúntame.models import Post
from .serializer import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.post_object.all()
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    pass




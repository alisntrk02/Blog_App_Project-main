from rest_framework.viewsets import ModelViewSet
from .models import Blog, Category, Comment, Like, PostView
from .permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly, IsOwnerUserOrReadOnly
from .serializers import BlogSerializer, CategorySerializer, CommentSerializer, LikeViewSerializer, UserBlogSerializer, PostViewSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class BlogMVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_serializer_class(self):
      
        if self.request.user.is_staff:
            return BlogSerializer
        return UserBlogSerializer


    def get_queryset(self):
        if self.request.user.is_staff:
            return Blog.objects.all()

        if Blog.objects.filter(user=self.request.user.id):
            return Blog.objects.filter(user=self.request.user.id) and Blog.objects.filter(status="P")
        else:
            return Blog.objects.filter(status='P')



    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        views = PostView.objects.filter(blog=instance, user=request.user)
        if not views.exists():
            PostView.objects.create(blog=instance, user=request.user, post_views=True)
        return super().retrieve(request, *args, **kwargs)
        
 

class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerUserOrReadOnly]  


class LikeMVS(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeViewSerializer


class PostviewMVS(ModelViewSet):
    queryset = PostView.objects.all()
    serializer_class = PostViewSerializer

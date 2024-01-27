from django.urls import path
from rest_framework import routers
from .views import CategoryMVS, BlogMVS, CommentMVS, LikeMVS, PostviewMVS


router = routers.DefaultRouter()
router.register("categories", CategoryMVS)
router.register("blogs", BlogMVS)
router.register("comments", CommentMVS)
router.register("likes", LikeMVS)
router.register("postviews", PostviewMVS)

urlpatterns = [
    
] + router.urls
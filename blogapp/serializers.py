from rest_framework import serializers

from .models import Category, Blog , Comment , PostView ,Like 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ['id']


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    comment_count = serializers.SerializerMethodField() 
    likes_count = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'user',
            'user_id',
            'title', 
            'content',
            'category_id',
            'category',
            'comment_count',
            'views_count',
            'likes_count',
            'status',
            'publish_date',
            )
        read_only_fields = ["id", "user"]


    def get_comment_count(self, obj):
        return obj.BlogComment.count()

    def get_likes_count(self, obj):
        return obj.BlogLikes.filter(likes=True).count()

    def get_views_count(self, obj):
        return obj.BlogPostViews.filter(post_views=True).count()


    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Blog.objects.create(**validated_data)
        return instance



class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'user_id',
            'blog_id',
            'blog',
            'content',
            'time_stamp',            
        )
        read_only_fields = ['id', 'user']


    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Comment.objects.create(**validated_data)
        return instance


class LikeViewSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = (
            'id',
            'user_id',
            'user',
            'blog_id',
            'blog',
            'likes',
        )
        read_only_fields = ['id', 'user']


    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Like.objects.create(**validated_data)
        return instance


class PostViewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = PostView
        fields = (
            'id',
            'user_id',
            'user',
            'blog_id',
            'blog',
            'post_views',
            'time_stamp',
        )
        read_only_fields = ['id', 'user']


    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = PostView.objects.create(**validated_data)
        return instance



class UserBlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    
    comment_count = serializers.SerializerMethodField() 
    likes_count = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'user',
            'user_id',
            'title', 
            'content',
            'category_id',
            'category',
            'comment_count',
            'views_count',
            'likes_count',
            'publish_date',
            )  #    exclude = ['status',]
        read_only_fields = ["id", "user"]


    def get_comment_count(self, obj):
        return obj.BlogComment.count()

    def get_likes_count(self, obj):
        return obj.BlogLikes.filter(likes=True).count()

    def get_views_count(self, obj):
        return obj.BlogPostViews.filter(post_views=True).count()


    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Blog.objects.create(**validated_data)
        return instance
    
   

    
    
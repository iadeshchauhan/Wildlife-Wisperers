from rest_framework import serializers
from .models import ExtendedUser, BlogPost, Comment, Category

class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('id', 'user', 'fav_blog')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    author = ExtendedUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()  
    categories = CategorySerializer(many=True) 

    class Meta:
        model = BlogPost
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count() 
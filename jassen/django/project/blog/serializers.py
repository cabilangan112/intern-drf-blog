from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post,Comment,Category,Tag



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)

 

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    category_name = serializers.SerializerMethodField()
    banner_photo = serializers.FileField()
    class Meta:
        model = Post
        fields = ('title',
                  'sub_title', 
                  'banner_photo', 
                  'body', 
                  'date_modified', 
                  'category',
                  'category_name',
                  'tags', 
                  'status')

    def get_category_name(self,instance):
       return instance.category.title

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 
                  'text')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title' ,'author',)


 
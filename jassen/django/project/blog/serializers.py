from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Blog,Post,Comment,Category,Tag



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('heading', 
                  'sub_heading')

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(Tag, many=True)
    blog_heading = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    banner_photo = serializers.FileField(required=False)
    class Meta:
        model = Post
        fields = ('title',
                  'sub_title', 
                  'banner_photo', 
                  'body', 
                  'date_modified', 
                  'blog',
                  'blog_heading',
                  'category',
                  'category_name',
                  'tags', 
                  'status')

    def get_category_name(self,instance):
       return instance.category.title

    def get_blog_heading(self,instance):
       return instance.blog.heading   
 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 
                  'text')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


 
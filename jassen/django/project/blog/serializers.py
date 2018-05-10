from django.contrib.auth.models import User, Group

from django.utils.timesince import timesince
from rest_framework import serializers
from .models import Post,Comment,Category,Tag



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
          'id','title',)

 

class PostSerializer(serializers.ModelSerializer):
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'sub_title', 
                  'banner_photo', 
                  'body',
                  'date_display',
                  'date',
                  'timesince',
                  'date_modified', 
                  'category',
                  'category_name',
                  'tags', 
                  'status')

    def get_category_name(self,instance):
       return instance.category.title

    def get_date_display(self, instance):
        return instance.date.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self, instance):
        return timesince(instance.date_modified) + " ago"   
         

class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ('post', 
                  'text',
                  'author',
                  'date_created',)

 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title' ,)
 
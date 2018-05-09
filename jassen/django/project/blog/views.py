from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Post,Comment,Category,Tag
from .serializers import PostSerializer,CommentSerializer,CategorySerializer,TagSerializer
 

class PostViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Post.objects.all()
        serializer_context = {'request': request,}
        serializer = PostSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            for tag in request.data.get('tags'):
                t = Tag.objects.get(id=tag)
                post.tags.add(t)
            return Response(serializer.data)
        return Response(serializer.errors )


    def get_tags(self, *args, **kwargs):
        tags = Tags.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializers.data)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_context = {'request': request,}
        serializer = PostSerializer(post, context=serializer_context)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)        

    def post(self, request, format=None):
        post= get_object_or_404(Post, pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors )

class CategoryViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Category.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = CategorySerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

 
    def post(self, request, format=None):
        post= get_object_or_404(Post, pk=pk)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Tag.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = TagSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tag.objects.all()
        tag = get_object_or_404(queryset, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = TagSerializer(tag, context=serializer_context)
        return Response(serializer.data)

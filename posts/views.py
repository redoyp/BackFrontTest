from django.shortcuts import render
from .models import Post
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.
# title, content, author, createdAt, updatedAt
class Posts(APIView) :
    def get(self, request) :
        all_posts = Post.objects.all()
        serializer = PostSerializer(all_posts, many = True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        

class PostDetail(APIView) :
    def get_object(self, id) :
        try :
            id = Post.objects.get(id = id)
        except :
            raise NotFound
        return id
    
    def get(self, request, id) :
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id) :
        post = self.get_object(id)
        serializer = PostSerializer(post, data =request.data, partial = True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.errors)
        else :
            return Response(serializer.errors)
        
    def delete(self, request, id) :
        post = self.get_object(id)
        post.delete()
        return Response(status = HTTP_204_NO_CONTENT)
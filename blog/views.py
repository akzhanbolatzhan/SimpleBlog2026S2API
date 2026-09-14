# from django.db.migrations import serializer
# from django.http import JsonResponse, HttpResponse
# from http.client import HTTPResponse
#
# from django.shortcuts import render
# from rest_framework.decorators import api_view
#
# from blog.models import Post
# from blog.serializers import PostSerializer
#
#
# # Create your views here.
# @api_view(['GET'])
# def home(request):
#     posts = PostSerializer(Post.objects.all(), many=True)
#     return JsonResponse(serializer.data, safe=False)


from django.http import JsonResponse
from rest_framework.decorators import api_view

from blog.models import Post
from blog.serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def home(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)
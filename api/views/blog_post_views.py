from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.blog_post import Blog
from ..serializers import BlogSerializer, UserSerializer

class Blog(generics.ListCreateAPIView):
    def get(self, request):
      """index request"""
      blogs = Blog.objects.filter(owner=request.user.id)
      data = BlogSerializer(blogs, many=True).data
      return Response(data)

    serializer_class = BlogSerializer
    def post(self, request):
      """create request"""
      request.data['blog']['owner'] = request.user.id
      blog = BlogSerializer(data=request.data['blog'])
      if blog.is_valid():
          blog.save()
          return Response({ 'blog': blog.data }, status=status.HTTP_201_CREATED)
      else:
          return Response(blog.errors, status.HTTP_400_BAD_REQUEST)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
      """show request"""
      blog = get_object_or_404(Blog, pk=pk)
      data = BlogSerializer(blog).data

      if not data['owner'] == request.user:
          raise PermissionDenied('Unauthorized, you do not own this post')


      return Response(data)


    def delete(self, request, pk):
        """delete request"""
        blog = get_object_or_404(Blog, pk=pk)
        if not blog.owner.id == request.user.id:
            raise PermissionDenied('Unauthorized, you do not own this post')

        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# def partial_update(self, request, pk):
#    """update request"""
#    if request.data['blog'].get('owner', False):
#        del request.data['blog']['owner']

#    blog = get_object_or_404(Blog, pk=pk)
#    if not request.user.id == blog.owner.id:
#        raise PermissionDenied('Unauthorized, you do not own this post')

#    request.data['blog']['owner'] = request.user.id
#    data = BlogSerializer(blog, data=request.data['blog'])
#    if data.is_valid():
#        data.save()
#        return Response(status.HTTP_204_NO_CONTENT)
#    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

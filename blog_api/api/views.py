# *** template from django.views.generic import ListView

from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


#  *** eith templates
# class BlogListView(ListView):
#     model = Blog
#     template_name = "blog_list.html"

class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

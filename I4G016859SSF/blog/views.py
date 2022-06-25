from audioop import reverse
from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy

from blog.models import Post

# Create your views here.
def PostListView(request):
    model = Post.objects.all()
    return render(request, 'blog/post_list.html')

def PostCreateView(request):
    model = Post.objects.all()
    fields = "__all__"
    success_url = reverse_lazy('blog:all')
    return render(request, 'blog/post_create.html', {'model': model})


def PostDetailView(request):
    model = Post.objects.all()
    return render(request, 'blog/post_detail.html')

def PostUpdateView(request):
    model = Post.objects.all()
    fields = "__all__"
    success_url = reverse_lazy('blog:all')
    return render(request, 'blog/post_update.html', {'model': model})

def PostDeleteView(request):
    model = Post.objects.all()
    fields = "__all__"
    success_url = reverse_lazy('blog:all')
    return render(request, 'blog/post_delete.html', {'model': model})
from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    # Post 클래스에 모든 오브젝트를 가져와서 변수에 저장
    posts = Post.objects.all()

    context = {
        'posts':posts,
    }

    return render(request, 'posts/index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

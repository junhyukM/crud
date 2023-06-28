from django.shortcuts import render, redirect
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

def new(request):
    return render(request, 'posts/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    post = Post()
    post.title = title
    post.content = content
    post.save()

    # redirect(app_name:name)
    return redirect('posts:detail', id=post.id)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('posts:index')

def edit(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post,
    }

    return render(request, 'posts/edit.html', context)

def update(request, id):
    # 기존정보
    post = Post.objects.get(id=id)

    # 사용자가 방금 입력한 정보
    title = request.POST.get('title')
    content = request.POST.get('content')

    post.title = title
    post.content = content
    post.save()

    return redirect('posts:detail', id=post.id)

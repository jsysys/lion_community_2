from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

def home(request):
    posts = Post.objects.all()
    post_num = len(posts)
    return render(request, "home.html", {"posts": posts, "post_num":post_num})

def detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, "detail.html",{"post": post})

def new(request):
    return render(request, "new.html")

def create(request):
    new_post = Post()
    new_post.title = request.POST["title"]
    new_post.writer = request.POST["writer"]
    new_post.body = request.POST["body"]
    new_post.pub_date = timezone.now()
    new_post.save()
    return redirect("detail", new_post.id)

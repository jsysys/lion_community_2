from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm 

def home(request):
    posts = Post.objects.all()
    post_num = len(posts)
    return render(request, "home.html", {"posts": posts, "post_num":post_num})

def detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, "detail.html",{"post": post})

def new(request):
    form = PostForm()
    return render(request, "new.html", {'form': form})

def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.pub_date = timezone.now()
        new_post.save()
        return redirect("detail", new_post.id)
    return redirect('home')

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, "edit.html", {"post": edit_post})

def update(request, id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST["writer"]
    update_post.body = request.POST["body"]
    update_post.pub_date = timezone.now()
    update_post.save()
    return redirect("detail", update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect("home")
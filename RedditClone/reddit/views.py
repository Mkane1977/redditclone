
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.username)


def post_list(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'reddit/post_list.html',  {'posts': posts})

@login_required
def post_new(request):
    context = {}
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
           
            post = form.save(commit=False)
            post.submitter = request.user
            post.save()
            
            for subreddit_id in request.POST.getlist('subreddits'):
                SubRedditPost.objects.create(subreddit_id=subreddit_id, post=post)
            return redirect('post_detail', pk=post.pk)
            
    else:
        form = PostForm()
        context['form'] = form
    return render(request, 'reddit/post_edit.html', {'form': form, 'is_create': True})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post, initial={'subreddits' : post.subreddits.all()})
    return render(request, 'reddit/post_edit.html', {'form': form, 'is_create': False})

def post_detail(request, pk):
     
   
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'reddit/post_detail.html', {'post': post})

def sub_detail(request, pk):
    sub = get_object_or_404(SubReddit, pk=pk)
    return render(request, 'reddit/sub_detail.html', {'sub': sub})

@login_required
def add_comment(request, pk, parent_pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.parent_id = parent_pk
            comment.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'reddit/add_comment.html', {'form': form})


# Create your views here.
def home_view(request):
    context = {}
    context['form'] = PostForm()
    return render( request, "base.html", context)


def display_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
       post = Post.objects.all() 
       return render((request, 'post_detail.html',
                     {'images' : post}))
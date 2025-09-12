# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.contrib import messages

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            # redirect to detail page after successful save
            return redirect('blog:post_detail', pk=post.pk)
        # if invalid, falls through to re-render with errors
    else:
        # initial form; author is shown in template from request.user
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

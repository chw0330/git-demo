from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post


def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "发布成功。")
            return redirect("post_list")
    else:
        form = PostForm()

    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"form": form, "posts": posts})

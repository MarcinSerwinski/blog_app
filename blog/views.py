from django.shortcuts import render, get_object_or_404
from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'home/list.html',
                  {'posts': posts})


def post_detail(request):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'home/post_detail.html',
                  {'posts': post})

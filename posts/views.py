from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from posts.models import Post


def post_list_and_create(request):
    posts = Post.objects.all()
    print(posts.count())
    return render(request, "posts/main.html", {"posts": posts})

def load_post_data_view(request, max_idx):
    num_visible = 3
    min_idx = max_idx - num_visible
    size = Post.objects.count()
    
    posts = Post.objects.all()
    data = []
    for post in posts:
        item = {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "liked": True if request.user in post.liked.all() else False,
            "author": post.author.user.username
        }
        data.append(item)
    return JsonResponse({"data": data[min_idx: max_idx], "size": size})
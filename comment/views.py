from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Comment
from post.models import Post
from django.http import JsonResponse

@login_required(login_url='login')
@require_POST
def add_comment(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get("content")

    if not content:
        return JsonResponse({"error": "Empty comment"}, status=400)

    comment = Comment.objects.create(
        author=request.user,
        post=post,
        content=content
    )

    return JsonResponse({
        "username": request.user.username,
        "content": comment.content,
        "created_at": comment.created_at.strftime("%b %d"),
        "comment_count": post.comments.count()
    })

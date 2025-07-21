from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    return render(request, 'main/post_list.html', {'posts': posts, 'comment_form': comment_form})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'main/post_new.html', {'form': form})

def like_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.get(id=data['id'])

        if data['type'] == 'like':
            post.like += 1
        else:
            post.dislike += 1

        post.save()
        return JsonResponse({'id': post.id, 'type': data['type']})

@require_POST
def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return JsonResponse({'content': comment.content, 'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')})
    return JsonResponse({'error': 'Invalid form'}, status=400)

@require_POST
def comment_delete(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({'success': True})
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': '댓글이 존재하지 않습니다.'}, status=404)

@require_POST
def post_delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return JsonResponse({'success': True})
    except Post.DoesNotExist:
        return JsonResponse({'success': False, 'error': '게시글이 존재하지 않습니다.'}, status=404)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CreatePostForm, EditPostForm
from .models import Post


@login_required
def create_post(request):
    form = CreatePostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('all_post', username=request.user.username)

    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'blog_post/new_post.html', context)


@login_required
def edit_post(request, username, post_id):
    other_user = User.objects.get(username=username)
    post = Post.objects.get(user=other_user.pk, pk=post_id)

    form = EditPostForm(data=request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('single_post', username=username, post_id=post_id)

    context = {
        'form': form,
        'user': request.user,
        'other_user': other_user,
        'post': post
    }
    if request.user.username == username:
        context['is_same_user'] = True
    else:
        context['is_same_user'] = False
    return render(request, 'blog_post/edit_post.html', context)


@login_required
def delete_post(request, username, post_id):
    if request.user.username == username:
        Post.objects.get(pk=post_id).delete()
        return redirect('all_post', username=username)
    else:
        pass


def view_post(request, username, post_id):
    other_user = User.objects.get(username=username)
    single_post = Post.objects.get(user=other_user.pk, pk=post_id)

    context = {
        'user': request.user,
        'other_user': other_user,
        'post': single_post
    }
    if request.user.username == username:
        context['is_same_user'] = True
    else:
        context['is_same_user'] = False
    return render(request, 'blog_post/single_post.html', context)


def view_all_post(request, username):
    # print('User:', User.objects.get(username=username).pk)
    other_user = User.objects.get(username=username)
    post = Post.objects.filter(user=other_user.pk)
    context = {
        'user': request.user,
        'other_user': other_user,
        'all_post': post
    }
    return render(request, 'blog_post/all_post.html', context)






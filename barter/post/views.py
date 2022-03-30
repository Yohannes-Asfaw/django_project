from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings

from .forms import *
from .models import *

User = get_user_model()


# @login_required
def home(request):

    if request.user.is_anonymous:
        return render(request, 'index.html')

    posts = Post.objects.all()

    if request.POST:

        if request.POST['submit'] == "send-offer":

            post = Post.objects.get(id=request.POST['post'])
            offer = Post.objects.get(id=request.POST['offer'])

            Request.objects.create(
                post=post,
                receiver=post.poster,
                offered=offer,
                sender=offer.poster
            )

        else:
            req = Request.objects.get(id=request.POST['request_id'])

            if request.POST['submit'] == 'accept':
                req.status = 'accepted'
                req.save()
            elif request.POST['submit'] == 'reject':
                req.delete()

    elif request.GET.get('search'):
        text = request.GET['search']
        posts = posts.filter(commodity_name__icontains=text) \
            | posts.filter(description__icontains=text)

    elif request.GET.get('category'):
        category = request.GET['category']
        posts = posts.filter(category=category)

    return render(request, 'home.html', context={'posts': posts, 'categories': Post.CATEGORIES})


@login_required
def edit_profile(request):

    if request.POST:
        form = EditProfileForm(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('edit_profile')

    return render(request, 'edit_profile.html', context={'form': EditProfileForm(instance=request.user)})


@login_required
def create_post(request):

    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
            return redirect('home')

    return render(request, 'post.html', context={'post': Post(), 'is_create': True})


@login_required
def edit_post(request, id):

    if request.POST:
        post = Post.objects.get(id=id)
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        try:
            post = Post.objects.get(id=id)
            if request.user.username != post.poster.username:
                raise Exception('User try to edit others post')
            return render(request, 'post.html', context={'post': post, 'is_create': False})
        except:
            return render(request, '403.html')


@login_required
def delete_post(request, id):

    try:
        post = Post.objects.get(id=id)
        post.delete()
    except:
        pass

    return redirect('home')


@login_required
def others_profile(request, username):

    try:
        user = User.objects.get(username=username)
        print(username, user)

        if user.username == request.user.username:
            return redirect('edit_profile')

        return render(request, 'others_profile.html', context={'other': user, 'categories': Post.CATEGORIES})
    except:
        return redirect('home')


@login_required
def post_detail(request, id):

    if request.POST:

        if request.POST['submit'] == "send-offer":

            post = Post.objects.get(id=request.POST['post'])
            offer = Post.objects.get(id=request.POST['offer'])

            Request.objects.create(
                post=post,
                receiver=post.poster,
                offered=offer,
                sender=offer.poster
            )

    try:
        post = Post.objects.get(id=id)
        return render(request, 'post_detail.html', {'post': post})
    except:
        return render(request, '403.html')

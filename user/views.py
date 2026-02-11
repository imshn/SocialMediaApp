from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from post.models import Post

def profile(request):
    # print(username)
    return render(request, 'profile/profile.html', {'fullname': request.user.first_name + ' ' + request.user.last_name})

def home(request):
    if request.user.is_authenticated:
        allposts = Post.objects.select_related('author').prefetch_related('likes')
        for post in allposts:
            post.liked_by_user = post.likes.filter(user=request.user).exists()
        return render(request, 'home/home.html',{"title": f"{request.user.username} | Home", "all_posts": allposts} )
    else:
        return redirect('login')

@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'profile/edit_profile.html', {'form': form})

    return render(request, 'edit_profile.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = RegisterForm()

    return render(request, 'register.html', {'form': form})
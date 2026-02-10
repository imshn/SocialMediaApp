from django.shortcuts import render, redirect
from .forms import RegisterForm


def profile(request, username):
    print(username)
    return render(request, 'profile/profile.html', {'fullname': request.user.first_name + ' ' + request.user.last_name})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html',{"title": f"{request.user.username} | Home"} )
    else:
        return redirect('login')
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
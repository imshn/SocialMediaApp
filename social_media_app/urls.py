"""
URL configuration for social_media_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views

from comment.views import add_comment
from post.views import create_post, likePost
from user.forms import LoginForm
from django.urls import path
from user.views import register, home, profile, edit_profile
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("user/register/", register, name='register'),
    path(
        'user/login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            authentication_form=LoginForm
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('user/edit_profile/', edit_profile, name='edit_profile'),
    # path('accounts/profile/<str:username>/', profile, name='profile'),
    path('user/create/', create_post, name='create_post'),
    path('user/like/<int:post_id>', likePost, name='like_post'),
    path('user/comment/<int:post_id>', add_comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

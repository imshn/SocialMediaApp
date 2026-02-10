from django.contrib import admin
from post.models import Post, Like

# Register your models here.
@admin.register(Post)
@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    app_label = 'post'

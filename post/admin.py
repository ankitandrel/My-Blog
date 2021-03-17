from django.contrib import admin
from . models import Post
from . froms import CreatePostForm
# Register your models here.




class PostAdmin(admin.ModelAdmin):
    form = CreatePostForm


admin.site.register(Post, PostAdmin)
from django.core import paginator
from django.shortcuts import redirect, render,get_object_or_404
from . models import Post
from . froms import CreatePostForm
from django.core.paginator import Paginator

# Create your views here.

def posts(request):
    # posts = Post.objects.order_by('-updated_date')
    # paginator = Paginator(posts, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # data = {
    #     # 'posts':posts,
    #     'page_obj':page_obj,
        
    # }

    # return render(request, 'webpages/home.html', data)
    pass

def post_details(request, id):
    posts = get_object_or_404(Post, pk = id)
    data = {
        'posts': posts,
    }

    return render(request, 'posts/post_details.html', data)
    
def create_post(request):
    posts = Post(author = request.user)
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance= posts)
        if form.is_valid():
            form.save()
            return redirect('home')
    data = {
        'form':form,
    }
    return render(request, 'posts/create_post.html', data)

def update_post(request, id):
    posts = Post.objects.get(id = id)
    form = CreatePostForm(instance=posts)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=posts)
        form.is_valid()
        form.save()
        return redirect('home')
    data = {
        'form':form,
    }

    return render(request, 'posts/create_post.html', data)

def delete_post(request, id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        post.delete()
        return redirect('profile')
    data = {
        'post':post,
    }

    return render(request, 'posts/profile.html', data)

def search(request):
    posts = Post.objects.order_by('-updated_date')
    blog_category_search = Post.objects.values_list('blog_category', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = posts.filter(heading__icontains = keyword)
    
    if 'blog_category' in request.GET:
        blog_category = request.GET['blog_category']
        if blog_category:
            posts = posts.filter(blog_category__iexact  = blog_category)
    data = {
        'posts':posts,
        'blog_category_search':blog_category_search,
    }

    return render(request, 'posts/search.html', data)

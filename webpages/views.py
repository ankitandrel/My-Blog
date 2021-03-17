from django.shortcuts import redirect, render
from post . models import Post
from django.core.paginator import Paginator
from . forms import ContactForm
# Create your views here.

def home(request):
    posts = Post.objects.order_by('-updated_date')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        # 'posts': posts,
        'page_obj':page_obj,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact_form = ContactForm(
           name = name,
           email = email,
           message = message,
        )
        contact_form.save()
        return redirect('home')


        
    return render(request, 'webpages/contact.html')

def services(request):
    return render(request, 'webpages/services.html')
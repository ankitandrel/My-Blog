from django.shortcuts import redirect, render
from . forms import UserRegisterForm
from . models import Profile
from django.contrib import messages
from . forms import ProfileUpdateForm, UserUpdateForm
from post . models import Post
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})



def logout_user(request):
    logout(request) 
    return redirect('home')
    
@login_required()
def profile(request):
    current_user = request.user
    posts = Post.objects.filter(author= current_user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Account Updates Succesfully !!!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    data = {
        'p_form':p_form,
        'u_form':u_form,
        'posts': posts,
    }

    return render(request, 'users/profile.html', data)



from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .forms import CustomUserCreationForm,ProfileUpdateForm,UserUpdateForm,PostForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def registerPage(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        else:
            messages.error(request, 'Failed to register. Correct your details.')

    else:
        form = CustomUserCreationForm()
        
    print("register_form in context:", form)

    context = {'register_form': form, 'page': 'register'}
    return render(request, 'login_register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        updateform =  UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST,request.FILES, instance=request.user)
        if updateform.is_valid() and  profileform.is_valid():
            updateform.save()
            profileform.save()
            messages.success(request,'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request,'Failed to update profile. Please correct the errors and try again.')
    else:
        updateform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
        context = {'u-form': updateform, 'profile_form': profileform}
    return render(request, 'profile.html', context)

def login_view(request):

    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('blog-home')
    
    next_url = request.GET.get('next')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            # Redirect to 'next' if it exists, otherwise default
            if next_url:
                return redirect(next_url)
            return redirect('blog-home')
        else:
            messages.error(request, 'Invalid username or password.')
    

    context = {'page': 'login'}
    return render(request, 'login_register.html', context)

def logout_view(request):
    # Handle logout logic here
    logout(request)
    messages.success(request,'You have been logged out successfully.')
    return redirect('blog-home')


def home(request):
    posts = Post.objects.all()
    context = {'posts':posts    }
    return render(request, 'home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Specify your template name here
    context_object_name = 'posts' 
    ordering = ['-published_date']  # Order posts by published date (newest first)
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

# CRUD operations for blog posts  using class-based views
# only logged in users can create, update or delete posts
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author remains unchanged
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
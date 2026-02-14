from django.shortcuts import render,redirect
from .models import Post,Comment
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .forms import CustomUserCreationForm,ProfileUpdateForm,UserUpdateForm,PostForm,CommentForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def registerPage(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Form created, about to validate") 
        if form.is_valid():
            print("Form is VALID")
            user =  form.save()
            print(f"User saved: {user.username}")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            print("Redirecting to blog-home") 
            return redirect('blog-home')
        else:
            print("Form is INVALID")                         # 7
            print("Errors:", form.errors.as_json()) 
            messages.error(request, 'Failed to register. Correct your details.')

    else:
        print("GET request") 
        form = CustomUserCreationForm()
        
    print("register_form in context:", form)

    context = {'register_form': form, 'page': 'register'}
    print("Rendering login_register.html") 
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
        context = {'u_form': updateform, 'profile_form': profileform}
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
    print("=== home view ===") 
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
    template_name = 'blog/post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add comment form and comments list to the context
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context
    

# CRUD operations for blog posts  using class-based views
# only logged in users can create, update or delete posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')  # Redirect to post list after successful creation
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')  # Redirect to post list after successful update
    def form_valid(self, form):
        
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to update the post

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to delete the post
    
# Comment views here
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def form_valid(self, form):
        # automatically set the author to the current user and associate the comment with the correct post
        form.instance.author = self.request.user  
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post=post     
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()   # redirect to post detail

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
#search functionality
class  SearchResults(ListView):
    model = Post
    template = 'blog/search_results.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
            
        return Post.objects.none()
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # reuse your existing list template
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Post.objects.filter(tags__name__iexact=tag_slug).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag_slug']   # optional: display tag name
        return context
    
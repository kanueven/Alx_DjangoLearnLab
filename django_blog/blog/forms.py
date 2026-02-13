from django import forms
from django.contrib.auth.models import User
from .models import Profile,Post,Comment
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget,TagField

class CustomUserCreationForm(UserCreationForm):
    # Extend Django’s UserCreationForm for 
    # the registration form to include additional fields like email.
    email = forms.EmailField(required=True  , help_text='Required. Enter a valid email address.')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address already in use.')
        return email
    
    class Meta:
        model= User
        fields = ["username","email","password1","password2"]
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','prof_pic']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = TagField(
        required=False,
        widget=TagWidget(attrs={'placeholder': 'Add tags separated by commas'})
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
from django import forms
from django.contrib.auth.models import User
from .models import Profile,Post
from django.contrib.auth.forms import UserCreationForm

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
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
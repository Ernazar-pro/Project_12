from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Posts

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    fullname = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('fullname','username', 'email', 'password1', 'password2')

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'description',
            'category',
            'image',
            'author',
        ]
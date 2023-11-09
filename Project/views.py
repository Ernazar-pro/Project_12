from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm
from .models import Category, Posts
from django.views import View


def home(request):
    category = Category.objects.all()
    posts = Posts.objects.all()
    context = {
        'posts' : posts,
        'category': category,
    }
    return render(request, 'index.html', context)

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
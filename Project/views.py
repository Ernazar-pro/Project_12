from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm, PostForm
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

def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
        return redirect('/')
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def post_update(request, pk):
    obj = get_object_or_404(Posts, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = PostForm(instance=obj)
    
    return render(request, 'update.html', {'form': form})
        
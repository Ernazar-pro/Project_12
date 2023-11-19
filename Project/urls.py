from django.urls import path
from .views import SignUpView, CustomLoginView, home, create, post_update, account, post_detail

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', post_update, name='post_update'),
    path('account/<int:pk>/', account, name='profile'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
]
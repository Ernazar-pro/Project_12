from django.urls import path
from .views import SignUpView, CustomLoginView, home

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', home, name='home'),
]
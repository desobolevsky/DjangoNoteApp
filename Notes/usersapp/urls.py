from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as page_views

urlpatterns = [
    path('register/', page_views.register_page, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='notesapp/home.html'), name='logout-page'),
]

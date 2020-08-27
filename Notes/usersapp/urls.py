from django.urls import path

from . import views as page_views

urlpatterns = [
    path('register/', page_views.register_page, name='register-page'),
]

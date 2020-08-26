from django.urls import path

from . import views as page_views

urlpatterns = [
    path('', page_views.home_page, name='home-page'),
]

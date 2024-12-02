from django.urls import path

from .views import home, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='biz_haqimizda'),
    path('contact/', contact, name='kantakt'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('sign-in/', signIn, name='sign-in'),
    path('sign-up/', signUp, name='sign-up'),

    path('', home, name='home'),
    path('settings/', settings, name='settings'),

    path('post', post, name='post'),
    path('like-post/', likePost, name='likepost'),

    path('profile/<str:pk>/', profilePage, name='profile'),
    path('follow', follow, name='follow'),
    path('search', search, name='search')
]
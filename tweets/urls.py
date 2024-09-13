from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweets_list, name='tweets_list'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
    path('register/', views.register, name='register'),
]

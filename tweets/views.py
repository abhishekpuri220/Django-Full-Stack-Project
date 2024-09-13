from django.shortcuts import render
from .models import Tweets
from .forms import TweetsForm, UserRegistration
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweets_list(request):
    tweets = Tweets.objects.all().order_by('-created_on')
    return render(request, 'tweets_list.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetsForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets_list')
    else:
        form = TweetsForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required   
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweets, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetsForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets_list')
    else:
        form = TweetsForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweets, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweets_list')
    return render(request, 'tweet_delete_confirm.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweets_list')
    else:
        form = UserRegistration()

    return render(request, 'registration/register.html', {'form': form})

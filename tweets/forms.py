from django import forms
from .models import Tweets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetsForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['tweet', 'image']

class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
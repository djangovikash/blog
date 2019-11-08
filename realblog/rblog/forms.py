from django import forms
from django.contrib.auth.models import User
from rblog.models import Post

class SINGUPFORM(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body','status']

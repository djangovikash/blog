from django.shortcuts import render,get_object_or_404
from rblog.forms import postform,SINGUPFORM
from rblog.models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms
from django.template.defaultfilters import slugify
from django.views.generic import DetailView

# Create your views here.
def f(request):
    return render(request,'rblog/home.html')
@login_required
def blog(request):
    form=forms.postform()
    if(request.method=='POST'):
        form=forms.postform(request.POST)
        instance=form.save(commit=False)
        instance.author=request.user
        instance.slug=slugify(form.cleaned_data['title'])
        instance.save()
        return HttpResponseRedirect('/')




        return HttpResponseRedirect('/v')
    return render(request,'rblog/blog.html',{'form':form})
@login_required
def read(request):
    post_list=Post.objects.all()
    return render(request,'rblog/read.html',{'post_list':post_list})
def logout(request):
    return render(request,'rblog/logout.html')
def singup(request):
    form=SINGUPFORM()
    if request.method=='POST':
        form=SINGUPFORM(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'rblog/singup.html',{'form':form})
class detail_view(DetailView):
    model=Post
    template_name='rblog/detail.html'

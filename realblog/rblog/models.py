from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

class custommanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
# Create your models here.
class Post(models.Model):
    STATUS_CHOICS=(('draft','DRAFT'),('published','PUBLISHED'))
    title=models.TextField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICS,default='draft')
    objects=custommanager()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args={'pk':self.pk})

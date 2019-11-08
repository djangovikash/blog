from django.contrib import admin
from .models import Post

# Register your models here.
class postbAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','status']
    prepopulated_fields={"slug":('title',)}
admin.site.register(Post,postbAdmin)

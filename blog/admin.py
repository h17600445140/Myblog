from django.contrib import admin

# Register your models here.
from blog.models import *

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','modified','created']
    list_filter = ['created','category__name']

admin.site.register(Post,PostModelAdmin)
admin.site.register(Category)
admin.site.register(Tags)
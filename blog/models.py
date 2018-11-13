from django.db import models

# Create your models here.
from django.core.paginator import Paginator
from  ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = '类别'

class Tags(models.Model):
    name = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = '标签'

class Post(models.Model):
    title = models.CharField(max_length=20)
    desc = RichTextUploadingField()
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = '贴子'

    # 分页处理函数
    @staticmethod
    def get_posts_by_page(num):
        num = int(num)
        paginator = Paginator(Post.objects.order_by('-modified').all(),1)
        if num<1:
            num = 1
        if num>paginator.num_pages:
            num = paginator.num_pages

        post = paginator.page(num)

        pervious = 1
        last = 1
        if num <= pervious:
            start = 1
            end = last + pervious + 1
        if num > pervious:
            start = num - pervious
            end = num + last
        if end > paginator.num_pages:
            end = paginator.num_pages
        end +=1

        return (post,range(start,end))

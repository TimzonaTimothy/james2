from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    # description = models.TextField(blank=True)
    # cat_image = models.ImageField(upload_to='photos/categories', blank=True)


    class Meta:
        verbose_name = 'blog_category'
        verbose_name_plural = 'blog_categories'


    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


    def __str__(self):
        return self.category_name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, unique=True)
    text = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(upload_to="photos", null= True, blank= True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True,blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    
    
    def get_url(self):
        return reverse('post_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.title +  '|' + str(self.author)


class SubscribedUser(models.Model):
    name = models.CharField(max_length=100, null= True)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
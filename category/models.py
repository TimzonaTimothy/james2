from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=200,blank=False,null=True)
    description = RichTextUploadingField(null=True, blank=True)
    # cat_image = models.ImageField(upload_to='photos/categories', blank=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def get_url(self):
        return reverse('product_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name

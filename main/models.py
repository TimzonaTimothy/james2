from xml.parsers.expat import model
from django.db import models
from category.models import *
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Product(models.Model):
    name     = models.CharField(max_length=200, unique=True, null=True)
    slug             = models.SlugField(max_length=200, unique=True, null=True)
    info = RichTextUploadingField(null=True, blank=True)
    pros      = models.TextField(blank=True, max_length=500, null=True)
    pros_1 = models.TextField(blank=True, max_length=500, null=True)
    pros_2 = models.TextField(blank=True, max_length=500, null=True)
    pros_3 = models.TextField(blank=True, max_length=500, null=True)
    pros_4 = models.TextField(blank=True, max_length=500, null=True)
    cons      = models.TextField(blank=True, max_length=500, null=True)
    cons_1 = models.TextField(blank=True, max_length=500, null=True)
    cons_2 = models.TextField(blank=True, max_length=500, null=True)
    cons_3 = models.TextField(blank=True, max_length=500, null=True)
    cons_4 = models.TextField(blank=True, max_length=500, null=True)
    more_info_1 = models.TextField(blank=True, max_length=500, null=True)
    more_info_2 = models.TextField(blank=True, max_length=500, null=True)
    score     = models.IntegerField(null=True, blank=True)
    image           = models.FileField(upload_to='photos', blank=True, null=True)
    thumbnail = models.FileField(upload_to='reviews', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    category         = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date     = models.DateTimeField(auto_now_add=True)
    modified_date    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('score',)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

class Terms(models.Model):

    text = RichTextUploadingField(null=True, blank=True)




    def __str__(self):
        return self.text
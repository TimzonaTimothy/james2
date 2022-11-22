from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'category','score', )
    # search_fields = ['name','category','score',]
    list_per_page = 20
    
    def get_queryset(self, request):
        queryset = super(ProductAdmin, self).get_queryset(request)
        queryset = queryset.order_by('score')
        return queryset

admin.site.register(Product, ProductAdmin)
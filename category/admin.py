from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug','title')

    def get_queryset(self, request):
        queryset = super(CategoryAdmin, self).get_queryset(request)
        queryset = queryset.order_by('id')
        return queryset

admin.site.register(Category, CategoryAdmin)
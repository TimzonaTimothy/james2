from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published',)
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','category','author',]
    list_filter = ['is_published',]
    list_per_page = 20

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}


admin.site.register(BlogCategory,CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(SubscribedUser)
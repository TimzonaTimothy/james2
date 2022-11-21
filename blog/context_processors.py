from .models import BlogCategory

def menu_links(request):
    links = BlogCategory.objects.all()
    return dict(blog_links=links)
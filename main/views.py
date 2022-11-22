from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .models import *
from blog.models import *
# Create your views here.


def main(request, category_slug=None):
    blog_post = Post.objects.all().order_by("-published_date").filter(is_published = True)

    categories = None 
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug= category_slug)
        products = Product.objects.filter(category=categories,)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        category_product =  products.first()

    else:

        products = Product.objects.all(9).order_by('-score')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        category_product = products.first()

    context = {
        'products':products,
        'category_product':category_product,
        'blog_post':blog_post,
    }

    return render(request, 'components/main.html', context)

def detail(request, id):
    single_product = Product.objects.get(id=id)
    return render(request, 'components/AaveReview.html', {'single_product':single_product})
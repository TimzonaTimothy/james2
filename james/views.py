from pyexpat import model
from django.shortcuts import render, redirect
from main.models import Product
from django.contrib import messages
from django.core.mail import send_mail
from blog.models import SubscribedUser
from blog.models import *

def home(request):
    products = Product.objects.all().filter(score=1)
    second_products = Product.objects.all().filter(score=2)

   

    blog_post = Post.objects.all().order_by("-published_date").filter(is_published = True)
    
    return render(request, 'index.html', context={'products':products,'second_products':second_products,'blog_post':blog_post})


def product_detail(request, category_slug, product_slug):

    blog_post = Post.objects.all().order_by("-published_date").filter(is_published = True)

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        
        
    except Exception as e:
        raise e
    return render(request, 'product_detail.html',{'single_product':single_product,'blog_post':blog_post})


def subscribe(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        if SubscribedUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('/')

        contact = SubscribedUser(name=name,email=email)

        contact.save()


        messages.success(request, 'Subscribtion Successful')
        return redirect('/')


def contact(request):
    if request.method == 'POST':
        name = request.POST['from_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            # email + ' sent you an enquiry'+ ' Subject :'  +subject,
            'New Mail For Advertisment From ' + '' + email + ','  + 'Subject : ' + '' + subject + ',' + ' Company Name/Personal Name : ' + '' + name,
            'message : '+message,
            'whipfinanceinfo@gmail.com',
            ['abrahamjames543@gmail.com','abrahamjames543@gmail.com'],
            fail_silently=False
        )
       
        messages.success(request, 'Your email has been sent ','alert alert-success alert-dismissible')
        return redirect(request.path)

    return render(request, 'contact.html', {})

def terms(request):
    return render(request, 'termsAndConditions.html')
def privacy(request):
    return render(request, 'privacyPolicy.html.html')
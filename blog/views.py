from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def post_list(request):
    post_list = Post.objects.all().filter(is_published=True).order_by('-published_date')
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'Blog/post_list.html',{'post_list':paged_listings})


def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'Blog/post_detail.html',{'post':post})

def subscribe(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        if SubscribedUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('/')

        contact = SubscribedUser(name=name,email=email)

        contact.save()

        # send_mail(
        #     'User Subscribed',
        #     name  +' '+ email + '. Subscribed',
        #     'whipfinanceinfo@gmail.com',
        #     ['arizonatymothy@gmail.com','whipfinanceinfo@gmail.com'],
        #     fail_silently=False
        # )
        # send_mail(
        #     'Thank You',
        #     'Hello '+name +' thank you for Subscribing',
        #     'whipfinanceinfo@gmail.com',
        #     [email,],
        #     fail_silently=False
        # )
        
        messages.success(request, 'Subscribtion Successful')
        return redirect(request.path)
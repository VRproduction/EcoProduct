from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from ecoapp.models import Product,Category,Basket_card,Brend,NutritionValue,Header,Blog,HomeAbout,HomeIcons,Partners,Slides,User
from django.urls import translate_url
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings
from django.db.models import F
from django.http import JsonResponse
import json
from ecoapp.forms import Messageform
def set_language(request, lang_code):
    url = request.META.get("HTTP_REFERER", None)
    if lang_code == 'az':
        return HttpResponseRedirect('/')
    else:
        response = redirect(translate_url(url, lang_code))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    
def home(request):
    headers = Header.objects.all()
    blogs = Blog.objects.all()
    if len(blogs)>4:
        blogs = blogs[0:4]
    about = HomeAbout.objects.first()
    icons = HomeIcons.objects.all()
    partners = Partners.objects.all()
    products = Product.objects.annotate(result=F('price') - F('discount_price'))
    categories = Category.objects.all()
    slides = Slides.objects.all()
    if request.GET.get('name'):
        name = request.GET.get('name')
        products = products.filter(Q(name__icontains=name) | Q(description__icontains=name) | Q(information__icontains=name))

    context = {
        'products':products,
        'headers':headers,
        'blogs':blogs,
        'about':about,
        'icons':icons,
        'partners':partners,
        'categories':categories,
        'slides':slides
    }
    return render(request,'index.html',context)

def shop(request):
    products = Product.objects.annotate(result=F('price') - F('discount_price'))
    categories = Category.objects.all()
    context = {'products':products,'categories':categories,}
    return render(request,'Shop.html',context)

def account(request):

    context = {}
    return render(request,'Account.html',context)

def about(request):
    icons = HomeIcons.objects.all()
    partners = Partners.objects.all()
    context = {
        'icons':icons,
        'partners':partners,

    }
    return render(request,'about.html',context)

def contact(request):
    context = {}
    return render(request,'Contact.html',context)

def blog(request):
    blogs = Blog.objects.all()


    paginator = Paginator(blogs, 4)
    page = request.GET.get("page", 1)
    blog_list = paginator.get_page(page)
    page_count = paginator.num_pages
    page_count = [x+1 for x in range(page_count)]
    context = {
        'blogs':blog_list,
        'count':page_count
    }
    return render(request,'Blog.html',context)

def message(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        newmessage = Messageform(data=data)
        if data.get('message') == '':
            return HttpResponse(status=401)
    
        if data.get('name') == '':
            return HttpResponse(status=404)
        if data.get('email') == '':
            return HttpResponse(status=405)
        if newmessage.is_valid():
            newmessage.save()
        else:
            return HttpResponse(status=405) 
        data = {'message': 'Data saved successfully'}
        return JsonResponse(data)
    else:
        return HttpResponse(status=405) 
    
def wish(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        product=Product.objects.get(id=data.get('id'))
        user = User.objects.get(id=data.get('userid'))
        if user in product.wishlist.all():
            product.wishlist.remove(user)
            print('remove')
            return HttpResponse(status=200) 
        else:
            product.wishlist.add(user)
            print('add')

            return HttpResponse(status=201) 
    else:
        return HttpResponse(status=405) 
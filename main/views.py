from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from cart.forms import CartAddProductForm
from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


# Create your views here.


def index(request):
    g = GeoIP2(settings.GEOIP_PATH)
    # 149.115.178.2 - ip адрес, который есть в базе
    a = g.country('149.115.178.2') # запрос к базе с данным айпи адресом
    print(request.META.get('REMOTE_ADDR')) # адрес пользователя
    print(a['country_name']) # вывод страны пользователя
    items = Catalog.objects.all()
    category = Category.objects.all()
    return render(request, 'main/index.html', {'items': items, 'category': category})

def detail(request, item_id):
    # items = Catalog.objects.get(id = item_id)
    # return render(request, 'main/detail.html', {'items': items})
    try:
        item: object = Catalog.objects.get(id = item_id)
        cart_product_form = CartAddProductForm
    except:
        return redirect('/') 
    return render(request, 'main/detail.html', {'item': item,
                                                'cart_product_form': cart_product_form})   

def add_product(request):
    if request.method == "POST":
        Catalog(name=request.POST.get('name'), price=request.POST.get('price'),
                description=request.POST.get('description')).save()  
        
    add_form = AddProductForm()
    return render(request, 'main/add.html', {'add_form': add_form})


def delete_product(request):
    if request.method == "POST":
        Catalog.objects.filter(name=request.POST.get('name')).delete()  
        
    delete_form = DeleteProductForm()
    return render(request, 'main/delete.html', {'delete_form': delete_form})


def search(request):
    # Check if the request is a post request.
    if request.method == 'GET':
        # Retrieve the search query entered by the user
        query = request.GET.get('search')
        # Filter your model by the search query
        items = Catalog.objects.filter(name__icontains=query)
        return render(request, 'main/search.html', {'query':query, 'items':items})
    else:
        return render(request, 'main/index.html',{})


def category(request):
    if request.method == "GET":
        query = request.GET.get("category")
        category_instance = get_object_or_404(Category, name=query)
        category_id = category_instance.id
        items = Catalog.objects.filter(category=category_id)
        return render(request, 'main/category.html', {'query':query, 'category_id': category_id, 'items':items})
    else:
        return render(request, 'main/index.html',{})
      

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 
                          'mereke.mr@bk.ru',
                          ['mereke.mr@bk.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:index")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})



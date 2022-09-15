
from ast import Pass
from itertools import product
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.conf import settings
from django.contrib.auth import logout as auth_logout
# Create your views here.
context = {
    'user_roles' : UserRole.objects.all()
}


def index(request):
    profile_data(request)
    return render(request, "index.html", context)


def login_page(request):
    return render(request, "login.html")



def register_page(request):
    return render(request, "register.html", context)


def login(request):
    print(request.POST)
    try:
        user_profile = Profile.objects.get(email=request.POST['email'])
        if user_profile.password == request.POST['password']:
            request.session['email'] = user_profile.email
            return redirect(profile_page)
        else:
            return redirect(login_page)
    except Profile.DoesNotExist as Err:
        print("Record Not Found")
        
    return redirect(register_page)


def register(request):
    print(request.POST)
    

    userrole = UserRole.objects.get(role=request.POST['user_role'])


    profile = Profile.objects.create(
        UserRole = userrole,
        email=request.POST['email'],
        password = request.POST['password']
        )

    Product.objects.create(Profile=profile)


    return redirect(login_page)

def profile_data(request):
    context['profile_data'] = Profile.objects.get(email = request.session['email'])
    

def profile_page(request):
    if 'email' in request.session:
        profile_data(request)
        return render(request, 'profile.html', context)
    return redirect(login_page)


def update_data(request):

    user_profile = Profile.objects.get(email=request.session['email'])


    user_profile.fullname = request.POST['fullname']
    user_profile.location = request.POST['location']
    user_profile.contact_info = request.POST['mobile']

    user_profile.save()


    return redirect(profile_page)


def upload_image(request):
    user_profile = Profile.objects.get(email=request.session['email'])

    if 'image' in request.FILES:
        user_profile.profileimage = request.FILES['image']
        user_profile.save()

    return redirect(profile_page)



def logout(request):
    if 'email' in request.session:
        auth_logout(request)
    return redirect(login_page)

def change_password(request):
    user_profile = Profile.objects.get(email=request.session['email'])

    if user_profile.password == request.POST['cpass']:
        user_profile.password = request.POST['npass']
        user_profile.save()
        return redirect(login_page)
    else:
        messages.info(request, "Current Password is incorrect")
        return redirect(profile_page)


       



def product_upload(request):
    if 'email' in request.session:
        profile = Profile.objects.get(email = request.session['email'])
        product_data = Product.objects.get(Profile=profile)
        context = {
            'product_data' : product_data
        }
        return render(request, 'product_upload.html', context)
    return redirect(login_page)


def update_product_upload(request):
    
    profile = Profile.objects.get(email = request.session['email'])
    product_data = Product.objects.get(Profile=profile)

    if 'product_image' in request.FILES:
        product_data.product_image = request.FILES['product_image']
        product_data.product_name = request.POST['product_name']
        product_data.description = request.POST['desc']
        product_data.product_price = request.POST['price']
        product_data.save()
        

    return redirect(product_upload)


def shop(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'shop.html', context)


def detail(request):
    
    return render(request, "detail.html", context)

def product_detail(request, query):
    new = query.split()
    products = Product.objects.filter(product_name__icontains=new[0])
    context = {
        'products' : products
    }
    return render(request, "detail.html", context)








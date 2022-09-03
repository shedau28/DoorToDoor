
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.conf import settings
# Create your views here.
context = {
    'user_roles' : UserRole.objects.all()
}


def index(request):
    return render(request, "index.html")


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


    Profile.objects.create(
        UserRole = userrole,
        email=request.POST['email'],
        password = request.POST['password']
        )

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
# from pathlib import Path
# def remove_image(request):
#     user_profile = Profile.objects.get(email=request.session['email'])

    
#     upload_path = Path.joinpath(settings.MEDIA_ROOT, "profile_images/{user_profile.profileimage.url}")
#     Path(upload_path).unlink()
    
#     user_profile.ProfileImage = ""
#     user_profile.save()
    

#     print('image removed.')
#     context['image_uploaded'] = 'false'

#     return redirect(profile_page)


def logout(request):
    if 'email' in request.session:
        del request.session['email']
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




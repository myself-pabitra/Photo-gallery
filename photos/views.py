import django
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def gallery(request):
    if request.method == 'POST':
        catagory = request.POST['catagory']
        if catagory != 'All':
            catagory = Catagory.objects.get(name=catagory)
            photos = Photo.objects.filter(catagory=catagory)
        else:
            photos = Photo.objects.all()

    else:
        # if catagory == None:
        photos = Photo.objects.all()
        # else:
        #     photos = Photo.objects.filter(catagory__name__contains = catagory)
        #     photos = Photo.objects.all()


    catagories = Catagory.objects.all().order_by('name')
    context={
        'catagories': catagories,
        'photos': photos,
        'mediaurl':settings.MEDIA_URL
    }
    return render(request,'gallery.html',context)


def showPhoto(request,pk):
    photos = Photo.objects.get(id = pk)

    return render(request,'photo_show.html',{'photos':photos})


# def photoAdd(request):
#     catagories = Catagory.objects.all()
#     if request.method == "POST":
#         data = request.POST
#         image = request.FILES.get('image')

#         if data['category'] != 'none':
#             category = category.objects.get(id=data['category'])
#         elif data['category_new'] != '':
#             category , created = Catagory.objects.get_or_create(name = data['category_new'])
#         else:
#             category = None
        
#         photo = Photo.objects.create(
#             category = category,
#             description = description,
#             image = image
#         )


#     context={
#         'catagories': catagories,
#     }
#     return render(request,'add_photo.html',context)

@login_required(login_url= 'login')
def photoAdd(request):
    catagories = Catagory.objects.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        description = request.POST['description']

        if data['category'] != 'none':
            category = Catagory.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category , created = Catagory.objects.get_or_create(name = data['category_new'])
        else:
            category = None
        
        Photo.objects.create(
            catagory = category,
            description = description,
            image = image
        )
        return redirect('gallery')


    context={
        'catagories': catagories,
    }
    return render(request,'add_photo.html',context)


def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username , password=password)
            if user is not None:
                login(request,user)
                return redirect('gallery')
            else:
                return redirect(loginUser)
        return render(request,'login.html')
    else:
        return redirect(gallery)


def registerUser(request):
    if request.method == 'POST':
        fname = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username = username).exists():
            messages.error(request, 'This Username already Exists..!!')
            return redirect(registerUser)
        elif User.objects.filter(email = email).exists():
            messages.error(request, 'This Email already Exists..!!')
        else:
          user =  User.objects.create_user(username = username , password = password , email = email,first_name = fname)
        #   user = CustomUser.objects.create(name = name , phone_number = phone , user = request.user)
          user.save()
          messages.success(request, 'Account created successfully..!!')
          return redirect(gallery)
    return render(request,'register.html')



def logoutUser(request):
    logout(request)
    return redirect(loginUser)
from django.urls import path
from .import views

urlpatterns = [
    path('',views.gallery , name = 'gallery'),
    path('add_photo',views.photoAdd , name = 'add_photo'),
    path('show_photo/<str:pk>/',views.showPhoto , name = 'show_photo'),
    path('login_user',views.loginUser , name = 'login'),
    path('register_user',views.registerUser , name = 'register'),
    path('logout',views.logoutUser , name = 'logout'),

]

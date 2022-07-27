from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class CustomUserInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = False
#     verbose_name_plural = 'CustomUsers'

# class CustomizedUserAdmin(UserAdmin):
#     inlines = (CustomUserInline,)

# admin.site.unregister(User)
# admin.site.register(User,CustomizedUserAdmin)
admin.site.register(Catagory)
admin.site.register(Photo)
# admin.site.register(CustomUser)

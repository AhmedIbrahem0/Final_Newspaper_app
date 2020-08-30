from django.contrib import admin
from .forms import Customchangeform ,Customusercreation
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class Custemuseradmin(UserAdmin):
    add_form =Customusercreation
    form= Customchangeform
    model =CustomUser
    list_display=['username' ,'email' ,'age' ,'is_staff']
admin.site.register(CustomUser,Custemuseradmin)
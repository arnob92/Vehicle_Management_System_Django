from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Requisition)
admin.site.register(Schedule)

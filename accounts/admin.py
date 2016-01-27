from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *


class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profile_picture', 'phone_number', 'uni_division', 'description')


# Define an inline admin descriptor for Company Detail model
# which acts a bit like a singleton
class ExtendedUserInLine(admin.StackedInline):
    model = ExtendedUser
    can_delete = False
    verbose_name_plural = 'Extended User'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ExtendedUserInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ExtendedUser, ExtendedUserAdmin)


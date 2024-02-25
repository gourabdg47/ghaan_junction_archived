   
from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm

  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'countries', 
                                       'highest_education', 'communication_languages', 'industry', 
                                       'skills')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions', 'tutor_status')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('native_name', 'phone_number')}),
  )

  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )

  list_display = ['email', 'first_name', 'last_name', 'is_staff', "native_name", "phone_number", 'tutor_status']
  search_fields = ('email', 'first_name', 'last_name', 'tutor_status', 'skills', 'industry', 'communication_languages')
  ordering = ('email', )

admin.site.register(User, UserAdmin)
from django.contrib import admin

# Register your models here.
from users.models import UsersProfile

admin.site.register(UsersProfile)
from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Control)
admin.site.register(CardIndex)
admin.site.register(Query)
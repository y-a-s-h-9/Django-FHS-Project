
from django.contrib import admin

from .models import SignUp, Admin, Restaurants, Manager

admin.site.register(SignUp)
admin.site.register(Admin)
admin.site.register(Restaurants)
admin.site.register(Manager)


from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Customer)
admin.site.unregister(Group)


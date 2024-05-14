from django.contrib import admin
from .models import Customer, Order,UrgentDelivery,Invoice,Maintainence
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(UrgentDelivery)
admin.site.register(Invoice)
admin.site.register(Maintainence)
admin.site.unregister(Group)


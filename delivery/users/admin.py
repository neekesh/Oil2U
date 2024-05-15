from django.contrib import admin
from .models import Customer, Order,UrgentDelivery,Invoice,Maintainence
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite

# class ServiceAdmin(AdminSite):
#     site_header = 'Admin Portal'
#     site_title = 'Admin Portal'
#     index_title = 'Welcome to the Admin Portal'
# admin_site = ServiceAdmin(name='myadmin')

# # Register models with the custom admin site
# admin_site.register(YourModel, YourModelAdmin)
# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ('email', 'company_name', 'date_joined')  # Display these fields in the admin list view
    search_fields = ('email', 'company_name') 
    list_per_page = 25

class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'status', "id")
    list_filter= ['status']
    search_fields = ('id', 'user', "start_date") 
    list_per_page = 25

class UrgentDeliveryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status', "id")
    list_filter= ['status']
    search_fields = ('id', 'user', "date") 
    list_per_page = 25
    
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'urgent_delivery_id', 'payment_date', "id")
    list_filter= ['payment_date']
    search_fields = ['id']
    list_per_page = 25

class MaintainenceAdmin(admin.ModelAdmin):
    list_display = ('date', 'email', 'address', "problem_statment")
    list_filter= ['date']
    list_per_page = 25

admin.site.register(Customer,AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(UrgentDelivery, UrgentDeliveryAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Maintainence, MaintainenceAdmin)
admin.site.unregister(Group)


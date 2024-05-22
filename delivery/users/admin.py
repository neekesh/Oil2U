from django.contrib import admin
from .models import Customer, Order,UrgentDelivery,Invoice,Maintainence
from django.contrib.admin import AdminSite
from django.urls import path
from django.shortcuts import render
from datetime import date

class MyAdminSite(AdminSite):
    site_header = 'Oil2U'  # Customize the header
    site_title = 'Admin Portal'
    index_title = 'Welcome to Oil2U Admin'
    login_template = 'admin/login.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.custom_view), name='my_custom_view')
        ]
        return custom_urls + urls

        
    def custom_view(self, request):
        urgent_deliveries = UrgentDelivery.objects.filter(status="pending").all()
        orders = Order.objects.filter(status="pending")  # .filter(start_date=date.today())

        # Convert QuerySets to lists
        urgent_deliveries = list(urgent_deliveries)
        orders = list(orders)
        
        # Combine lists
        combined_data = urgent_deliveries + orders
        
        # Sort combined list based on 'date' or 'start_date'
        combined_data.sort(key=lambda x: x.date if hasattr(x, 'date') else x.start_date, reverse=True)

        context = dict(
            self.each_context(request),
            table_data=combined_data,  # Add custom context here
        )
        return render(request, 'admin/custom_index.html', context)

custom_admin_site = MyAdminSite(name='Oil2U')
# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ('email', 'company_name', 'date_joined')  # Display these fields in the admin list view
    search_fields = ('email', 'company_name') 
    search_help_text = "Search by email or company name"
    list_per_page = 25

class AdminOrder(admin.ModelAdmin):
    list_display = ("id", 'user', 'start_date', 'status', )
    list_display_links = ["id", "user"]
    list_filter= ['status']
    # filter_horizontal = ["start_date"]
    search_fields = ('id', 'user') 
    search_help_text = "Search by order_id  or user"
    list_per_page = 25

class UrgentDeliveryAdmin(admin.ModelAdmin):
    list_display = ( "id",'user', 'date', 'status',)
    list_display_links = ["id", "user"]
    list_filter= ['status']
    search_fields = ('id', 'user', "date") 
    search_help_text = "Search by order_id  or user"
    list_per_page = 25
    
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ( "id","user",'order_id', 'urgent_delivery_id', 'payment_date')
    list_display_links = ["id", "user", "order_id", "urgent_delivery_id"]
    list_filter= ['payment_date']
    search_fields = ['id']
    search_help_text = "Search by invoice id "
    list_per_page = 25

class MaintainenceAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'user','email', 'address', "problem_statment")
    list_display_links = ['id','user']
    list_filter= ['date']
    list_per_page = 25

custom_admin_site.register(Customer,AdminCustomer)
custom_admin_site.register(Order, AdminOrder)
custom_admin_site.register(UrgentDelivery, UrgentDeliveryAdmin)
custom_admin_site.register(Invoice, InvoiceAdmin)
custom_admin_site.register(Maintainence, MaintainenceAdmin)



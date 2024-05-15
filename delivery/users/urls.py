from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)


from. import views

urlpatterns = [
    path("register",views.create, name="user_register"),
    path("login", views.login, name="user_signup"),
    path("edit_user/<int:pk>", views.update_customer, name="user_edit"),
    path("user/<int:pk>", views.user_details, name="user_detail"),
    path("order", views.create_order, name="create_order"),
    path("invoice", views.invoice, name="create_invoices"),
    path("invoice/all", views.all_invoices, name="invoices_lists"),
    path("invoice/<int:pk>", views.invoice_details, name="invoice_get"),
    path("notification/<int:pk>", views.notification_details, name="notfication_details"),
    path("notification/latest", views.notifcation_latest, name="notifcation_latest"),
    path("notification/lists", views.notification_list, name="notifcation_list"),
    path("notificaiton/update/<int:pk>", views.notification_update, name="notification_update"),
    
    path("urgent-delivery", views.urgent_delivery, name="urgent_delivery"),
    path("history", views.history, name="history"),
    path("maintainence", views.maintainence, name="maintainence"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
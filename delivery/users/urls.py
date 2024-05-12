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
    # path("edit_user", views.edit, name="user_edit"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
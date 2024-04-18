from django.urls import path
from .views import CustomUserCreate, CustomUserLogin, CustomUserLogout

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('login/', CustomUserLogin.as_view(), name='user_login'),
    path('logout/', CustomUserLogout.as_view(), name='user_logout'),
]
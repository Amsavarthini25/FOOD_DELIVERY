from django.urls import path
from .views import (
    home_view, register, get_customer_details, update_customer_details,
    login_user, logout_user
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_view, name='home'),  # ✅ Homepage
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),  
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # ✅ Ensures redirection after logout
    path('details/', get_customer_details, name='get_customer_details'),
    path('update/', update_customer_details, name='update_customer_details'),
]


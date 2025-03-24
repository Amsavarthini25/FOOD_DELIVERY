from django.urls import path
from .views import (
    register, get_customer_details, update_customer_details,
    login_user, logout_user
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),  # ⬅️ Added login
    path('logout/', logout_user, name='logout'),  # ⬅️ Added logout
    path('details/', get_customer_details, name='get_customer_details'),
    path('update/', update_customer_details, name='update_customer_details'),
]

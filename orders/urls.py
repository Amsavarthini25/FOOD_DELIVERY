from django.urls import path
from .views import place_order, cancel_order, modify_order

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('modify_order/<int:order_id>/', modify_order, name='modify_order'),
]

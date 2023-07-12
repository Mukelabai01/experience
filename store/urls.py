from django.urls import path
from .views import store, cart, product, checkout, order, singleproduct

urlpatterns = [
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('product/<str:pk>/', product, name="product"),
    path('checkout/', checkout, name="checkout"),
    path('order/', order, name="order"),
    path('singleproduct/', singleproduct, name="singleproduct"),
]



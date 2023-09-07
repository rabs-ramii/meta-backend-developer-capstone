from django.urls import path, include
from .views import MenuItemViewSet, BookingViewSet
from .views import menu_view, booking_view
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'menu', MenuItemViewSet),
router.register(r'booking', BookingViewSet),

urlpatterns = [
    path('restaurant/', include(router.urls)),
    
    path('menu-view/', menu_view, name="menu-view"),
    path('booking-view/', booking_view, name="booking-view"),
    path('api-token-auth/', obtain_auth_token),

]
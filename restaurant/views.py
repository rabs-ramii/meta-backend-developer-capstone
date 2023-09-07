from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from .forms import MenuForm, BookingForm

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    A viewset pertaining to the Menu Items
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated] # Optional for ease of Checking

def menu_view(request):

    menu_items = Menu.objects.all()
    
    context = {
        'menu_items': menu_items,
        'form': MenuForm,
    }

    return render(request, 'menu.html', context)

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset pertaining to the Table Booking schedule
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated] # Optional for ease of Checking

def booking_view(request):

    booking_items = Booking.objects.all()
    
    context = {
        'booking_items': booking_items,
        'form': BookingForm,
    }

    return render(request, 'booking.html', context)


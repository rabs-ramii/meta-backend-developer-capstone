from django import forms
from .models import Menu, Booking

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'


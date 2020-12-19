from django import forms
from .models import Hotel_image


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel_image
        fields = ['name', 'Hotel_images']

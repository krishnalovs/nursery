# forms.py
from django import forms

class ProductFilterForm(forms.Form):
    category = forms.CharField(required=False)
    subcategory = forms.CharField(required=False)
    brand = forms.CharField(required=False)
    price_range = forms.CharField(required=False)

from .models import *

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['number','street_address','address_line2','city', 'state', 'postal_code']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username','mobile','address', 'image']

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

# class AddressForm(forms.Form):
#     Email = forms.EmailField()
#     Mobile= forms.IntegerField()
#     Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model= Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


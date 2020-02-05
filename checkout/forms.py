from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    YEAR_CHOICES = [(i,i) for i in range(2018, 2028)]
    MONTH_CHOICES = [(i,i) for i in range(1, 12)]

    credit_card_number = forms.CharField(max_length = 20, required=False)
    cvv = forms.CharField(label = 'Security code (CVV)', required=False)
    expiry_month = forms.CharField(label='Month',choices=MONTH_CHOICES, required=False)
    expiry_year = forms.CharField(label='Year',choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name','phone_number','street_address1','street_address2','town_or_city','postcode','county','country',)



from django import forms
from django.core.validators import RegexValidator
from store.models import Vehicle, vehicles, payments
phone_validator = RegexValidator(r'[0-9]{10}', message="Please enter a valid mobile number.")


class Sell(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'Year': forms.widgets.DateInput(attrs={'type': 'date'}),
            'Contact': forms.widgets.TextInput(attrs={'pattern':'[0-9]{10}'}, )
        }
    

price_ranges = []
PRICE_DIFF = 2500000
KM_DIFF = 25000
for i,price in enumerate(range(0, 10_000_000-1, 2500000)):
    price_ranges.append((str(i), f"{price} - {price+2500000}"))

km_ranges = []
for i,price in enumerate(range(0, 100_000-1, 25000)):
    km_ranges.append((str(i), f"{price} - {price+25000}"))

class Buy(forms.Form):
    vehicle_type = forms.ChoiceField(label="Vehicle Type", choices=vehicles, required=True)
    brand = forms.CharField(label = "Brand", max_length=50, required=False)
    kilometers = forms.ChoiceField(choices=km_ranges, required=False)
    price = forms.ChoiceField(label="Price (INR)", choices=price_ranges)
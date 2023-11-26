from django.db import models
from django.core.validators import RegexValidator
vehicles = (
    ("B", "Bike"),
    ("C", "Car")
)
payments = (
    ("Card", "Card"),
    ("Net", "Netbanking"),
    ("Cash", "Cash on Delivery")
)

phone_validation = RegexValidator(r"[0-9]{10}")
class Vehicle(models.Model):
    name = models.CharField(name="Name", max_length=50)
    contact = models.CharField(name="Contact",max_length=10, validators=[phone_validation])
    vehicle_type = models.CharField(name="VehicleType",max_length=50, choices=vehicles, default="C")
    brand = models.CharField(name = "Brand", max_length=50)
    model = models.CharField(name="Model", max_length=50)
    year = models.DateField(name="Year")
    kilometers = models.IntegerField(name="Kilometers")
    color = models.CharField(name="Color", max_length=50)
    state = models.CharField(name="State", max_length=20)
    owners = models.IntegerField(name="NumberofOwners")
    price = models.IntegerField(name="Price")
    payment = models.CharField(name="Payment", max_length=50, choices=payments, default="Card")
    photos = models.ImageField(name="Photos", upload_to="Photos", blank=True)

from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

from events.models import Event, Seat


# Create your models here.
class Payment(models.Model):
    purchaser_email = models.EmailField()
    purchaser_number = models.CharField(max_length=16)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    cc_number = models.CharField(max_length=64)
    cc_expiry = models.CharField(max_length=64)
    cc_code = models.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(null=True)
    count = models.IntegerField(default=1)
    status = models.CharField(max_length=64, choices=[
        ("SUCCESS", "SUCCESS"),
        ("CANCELLED", "CANCELLED"),
        ("FAILED", "FAILED")
    ], default="SUCCESS")

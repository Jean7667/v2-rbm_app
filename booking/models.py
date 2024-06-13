from django.db import models
from customer.models import CustomUser

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    expert = models.ForeignKey(CustomUser, related_name='expert_bookings', on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, related_name='customer_bookings', on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
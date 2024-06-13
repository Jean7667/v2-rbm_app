from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """Form to add or edit a booking."""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['expert'].queryset = user.expert_bookings.all()
            self.fields['customer'].queryset = user.customer_bookings.all()
            self.fields['email'].initial = user.email
        self.fields['expert'].required = True
        self.fields['customer'].required = True
        self.fields['checkin'].required = True
        self.fields['checkout'].required = True

        self.fields['expert'].label = "Expert Name"
        self.fields['customer'].label = "Customer Name"
        self.fields['checkin'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['checkout'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')

        # Check if checkout is after checkin
        if checkin and checkout and checkin >= checkout:
            self.add_error('checkout', 'Checkout date must be after checkin date')

        # Check if a booking with the same date and time already exists
        if checkin and checkout:
            conflicting_bookings = Booking.objects.filter(
                checkin__lt=checkout, checkout__gt=checkin
            )
            if self.instance and self.instance.pk:
                conflicting_bookings = conflicting_bookings.exclude(pk=self.instance.pk)
            if conflicting_bookings.exists():
                self.add_error('checkin', 'This date and time is already booked. Please choose another day and time')

    class Meta:
        model = Booking
        fields = ['expert', 'customer', 'checkin', 'checkout']
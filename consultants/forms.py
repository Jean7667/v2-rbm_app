from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.core.exceptions import ValidationError
#from django.utils import timezone
import datetime
from datetime import date

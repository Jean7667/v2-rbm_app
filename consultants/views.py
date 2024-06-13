from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Expert, Skill
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

# Create your views here.
def consultants(request):
    return render(request, 'consultants/consultants.html')

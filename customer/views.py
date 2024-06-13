from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

# Create your views here.

class CxProfileView(View):
    cx_profile_template = 'customer/cxprofile.html'

    def get(self, request):
        # find the current user
        user = request.user
        if user.is_authenticated and user.is_customer:
            return render(request, self.cx_profile_template, {'user': user, 'edit_mode':True})
        else:
            return redirect('home')
        
    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            user.first_name = request.POST.get('firstname', user.first_name)
            user.last_name = request.POST.get('lastname', user.last_name)
            user.location = request.POST.get('location', user.location)
            user.email = request.POST.get('email', user.email)
            user.save()
            return redirect('customer_profile')  
        else:
            return redirect('login')
                
class DeleteCxProfileView(View):
    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_customer:
            user.delete()
            return redirect('home')
        else:
            return redirect('unauthorized')
        

# Read        
#Display in cxprofileview
#fct to show last Customer since created_date 
#fct last connection 

#Generic based view
# views for displaying a list of experts

# updated view with new context object name to reflect multiple selected skills



def customer(request):
    return render(request, 'customer/customer.html')
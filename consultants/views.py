from django.shortcuts import render

# Create your views here.
def consultants(request):
    return render(request, 'consultants/consultants.html')

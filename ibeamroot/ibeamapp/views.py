from django.shortcuts import render
from django.http import HttpResponse
   
def get_ibeam_form(request):
    return render(request, 'base.html')

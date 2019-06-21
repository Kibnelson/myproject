from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import StaffDetail, PeopleDetail, StudentDetail

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone # to display ate and time as per timezone

# Create your views here.


def people(request):
  return render(request, "people.html", {})
def person(request):
	    #intbursaryapps = Intbursary.objects
   return render(request, "person.html", {})
def home(request):
	    #intbursaryapps = Intbursary.objects
   return render(request, "home.html", {})

   return redirect('home')

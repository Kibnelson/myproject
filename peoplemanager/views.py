from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import StaffDetail, PeopleDetail, StudentDetail

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone # to display date and time as per timezone


# Create your views here.
def corestaff(request):
    #peopledetails = PeopleDetail.objects.filter(id=4).select_related() #shows on person online
    staffdetails = StaffDetail.objects.order_by('id')#code will list all records without joins
  
    # Assumes you have a row with a primary key of 1
    #staffdetail = StaffDetail.objects.get(pk=1)
 
# get the email of the reporter for the article
    #peopledetails = staffdetail.PeopleDetail.firstnames
     

    return render(request, "corestaff.html", {'staffdetails': staffdetails})


def person(request):
   return render(request, "person.html", {})


def people(request):
   return render(request, "people.html", {})


def postdcrfellows(request):
   return render(request, "postdcrfellows.html", {})


def researchafellows(request):
   return render(request, "researchafellows.html", {})


def students(request):
    studentdetails = StudentDetail.objects.order_by('id')
    return render(request, "students.html", {'studentdetails': studentdetails})

def steering_committee(request):
   return render(request, "steering_committee.html", {})

def home(request):
   return render(request, "home.html", {})
   return redirect('home')

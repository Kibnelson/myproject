from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Archivesuploads, Archivetypes, Interests

# Create your views here.
class ArchivesuploadsList(ListView):
    model = Archivesuploads
    template_name = "publications.html"



    #physicaladdress = Physicaladdress.objects.order_by('id')
    #postaladdress = Postaladdress.objects.order_by('id')

    #return render(request, "publications.html", context)


def home(request):

   return render(request, "home.html", {})

   return redirect('home')

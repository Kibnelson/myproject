from django.shortcuts import render
from .models import Archivesuploads, Archivetypes, Interests

# Create your views here.
def publications(request):
    #generalenquiries = Generalenquiries.objects.order_by('id')
    #physicaladdress = Physicaladdress.objects.order_by('id')
    #postaladdress = Postaladdress.objects.order_by('id')

    return render(request, "publications.html", {})


def home(request):

   return render(request, "home.html", {})

   return redirect('home')

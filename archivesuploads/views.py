from django.shortcuts import render
from django.views import generic
from .models import Archivesuploads, Archivetypes, Interests

# Create your views here.
class ArchivesuploadsListView(generic.ListView):
    model = Archivesuploads
    queryset = Archivesuploads.objects.order_by('id')[:20] # get 20 publications per page
    template_name ='publications.html'# specify your own template name /location



def publications(request):
    archivesupload = Archivesuploads.objects.order_by('id')
    context = {
            'archivesupload': archivesupload
    }

    #physicaladdress = Physicaladdress.objects.order_by('id')
    #postaladdress = Postaladdress.objects.order_by('id')

    return render(request, "publications.html", context)


def home(request):

   return render(request, "home.html", {})

   return redirect('home')

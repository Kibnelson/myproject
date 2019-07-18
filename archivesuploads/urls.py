
from django.urls import path, include
from archivesuploads.views import ArchivesuploadsList
from . import views


urlpatterns = [
   path('publications/',views.ArchivesuploadsList.as_view(), name ='publications'),

]

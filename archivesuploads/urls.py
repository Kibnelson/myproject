
from django.urls import path, include

from . import views


urlpatterns = [
   path('publications/',views.ArchivesuploadsListView.as_view(), name ='publications'),

]

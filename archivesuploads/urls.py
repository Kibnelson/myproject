
from django.urls import path, include
from . import views


urlpatterns = [
   path('publications/',views.publications, name ='publications'),

]

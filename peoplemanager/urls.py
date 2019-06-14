
from django.urls import path, include
from . import views


urlpatterns = [

   path('people/',views.people, name ='people') ,
   path('person/',views.person, name ='person') ,
   ]
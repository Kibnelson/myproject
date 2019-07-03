
from django.urls import path, include
from . import views


urlpatterns = [

   path('people/',views.people, name ='people') ,
   path('person/',views.person, name ='person') ,
   path('corestaff/',views.corestaff, name ='corestaff') ,
   path('postdcrfellows/',views.postdcrfellows, name ='postdcrfellows') ,
   path('researchafellows/',views.researchafellows, name ='researchafellows') ,
   path('students/',views.students, name ='students') ,
   path('steering_committee/',views.steering_committee, name ='steering_committee') ,
   ]

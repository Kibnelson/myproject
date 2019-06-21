from django.shortcuts import render

# Create your views here.
def contactus(request):
  return render(request, "contactus.html", {})
  
def home(request):
	    #intbursaryapps = Intbursary.objects
   return render(request, "home.html", {})

   return redirect('home')

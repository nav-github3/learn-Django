from django.http import HttpResponse

def homeResquest(request):
	return HttpResponse("You are at chai aur djaongo Home page"); 

def about(request):
	return HttpResponse("This is the about page of the djaongo"); 

def contact(request): 
	return HttpResponse("This is the contact page of the djapgo"); 
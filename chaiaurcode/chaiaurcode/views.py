from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	#return HttpResponse("Hello, world ! you are at Django page")
	return render(request , 'website/index.html')

def about(request):
	return HttpResponse("Hellow  this is about  page of the application ")

def contact(request):
	return HttpResponse("This  is  the contact page of the the application ")
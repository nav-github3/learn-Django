from django.http import HttpResponse 

def home(request):
	return HttpResponse("Hello World . You are the chai aur django home page ")

def about(request):
	return HttpResponse("Hello World . You are the chai aur django about page ")

def contact(request):
	return HttpResponse("Hello World . You are the chai aur django contact page ")




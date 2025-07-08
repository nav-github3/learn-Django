from django.shortcuts import render
from .models import chaiVarieties

# Create your views here.
def allChai(request):
	chais = chaiVarieties.objects.all()
	return render(request, 'chai/all_chai.html', {'chais': chais})




from django.http import HttpResponse
from django.shortcuts import render
def index(request):
  return HttpResponse("hai sreeraj")

def login(request): 
	data={}
	return render(request,"login.html",data)
def signup(request):
	data={}
	return render(request,"signup.html",data)
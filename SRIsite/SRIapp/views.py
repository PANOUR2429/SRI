#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world.")

from django.http import HttpResponse
from django.template import loader

def SRIapp(request):
  template = loader.get_template('SRI_page1.html')
  context = {
    'fruits': ['Apple', 'Banana']
  }
  return HttpResponse(template.render())
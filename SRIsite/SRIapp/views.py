#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world.")

from django.http import HttpResponse
from django.template import loader
from .models import *



def SRIapp(request):
  myLevels = Levels.objects.all().values()
  myDomainWeight = DomainWeight.objects.all().values()
  myImpactWeight = ImpactWeight.objects.all().values()
  myServices = Services.objects.all().values()
  mySelection = UserSelections.objects.all().values()
  template = loader.get_template('SRI_page1.html')
  context = {
    'myLevels': myLevels,
    'myDomainWeight' : myDomainWeight,
    'myImpactWeight' : myImpactWeight,
    'myServices' : myServices,
    'mySelection' : mySelection
  }
  return HttpResponse(template.render(context, request))

def test(request):
     template = loader.get_template('test.html')
     if request.method == 'POST':
       testtype = request.POST['testtype']
       test1.objects.create(testtype=testtype)
     return HttpResponse(template.render())
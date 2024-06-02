#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world.")

from django.http import HttpResponse
from django.template import loader
from .models import Levels
from .models import DomainWeight
from .models import ImpactWeight
from .models import Services
from .models import UserSelections

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
  if request.method == 'POST':
    selected_building_type = request.POST['selected_building_type']
    selected_zone = request.POST['selected_zone']
    selected_H = request.POST['selected_H']
  #  UserSelections = UserSelections.objects.create(selected_building_type = selected_building_type, selected_zone = selected_zone, selected_H = selected_H)
  return HttpResponse(template.render(context, request))


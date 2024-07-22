#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world.")

from django.http import HttpResponse
from django.template import loader

from .SRIcalc2 import calcSRI, SRIcalculator
from .models import *

from django.shortcuts import render, redirect
from .forms import *

def SRIapp(request):
  if request.method == 'POST':
    #form = DomainControlForm(request.POST)
    form = ControlForm(request.POST)
    if form.is_valid():
      instance = form.save()
      instance.id
      return redirect('test/' + str(instance.id))
  else:
    #form = DomainControlForm()
    form = ControlForm()
  return render(request, 'SRI_page1.html', {'form': form})


def Result(request,id):
  myLevels = Levels.objects.all().values()
  myDomainWeight = DomainWeight.objects.all().values()
  myImpactWeight = ImpactWeight.objects.all().values()
  myServices = Services.objects.all().values()
  mySelection = UserSelections.objects.all().values()
  Y = SRIcalculator()
#  Y = calcSRI()

  template = loader.get_template('test.html')
  context = {
    'myLevels': myLevels,
    'myDomainWeight' : myDomainWeight,
    'myImpactWeight' : myImpactWeight,
    'myServices' : myServices,
    'mySelection' : mySelection,
    'Y' : Y
  }
  return HttpResponse(template.render(context, request))


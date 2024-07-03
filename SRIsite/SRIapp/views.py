#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world.")

from django.http import HttpResponse
from django.template import loader
from .models import *

from django.shortcuts import render, redirect
from .forms import *

def SRIapp(request):
  if request.method == 'POST':
    #form = DomainControlForm(request.POST)
    form = ControlForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('test/')
  else:
    #form = DomainControlForm()
    form = ControlForm()
  return render(request, 'SRI_page1.html', {'form': form})


def Test(request):
  myLevels = Levels.objects.all().values()
  myDomainWeight = DomainWeight.objects.all().values()
  myImpactWeight = ImpactWeight.objects.all().values()
  myServices = Services.objects.all().values()
  mySelection = UserSelections.objects.all().values()

  template = loader.get_template('test.html')
  context = {
    'myLevels': myLevels,
    'myDomainWeight' : myDomainWeight,
    'myImpactWeight' : myImpactWeight,
    'myServices' : myServices,
    'mySelection' : mySelection
  }
  return HttpResponse(template.render(context, request))

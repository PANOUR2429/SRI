#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world.")

from django.http import HttpResponse
from django.template import loader

from .SRIcalc2 import SRIcalculator
from .models import *

from django.shortcuts import render, redirect
from .forms import *

def SRIapp(request):
  if request.method == 'POST':
    #form = DomainControlForm(request.POST)
    form = ControlForm(request.POST)
    if form.is_valid():
      instance = form.save()
      return redirect('SRI_result/' + str(instance.id))
  else:
    #form = DomainControlForm()
    form = ControlForm()
  return render(request, 'SRI_page1.html', {'form': form})


def Result(request, id):
  myLevels = Levels.objects.all().values()
  myDomainWeight = DomainWeight.objects.all().values()
  myImpactWeight = ImpactWeight.objects.all().values()
  myServices = Services.objects.all().values()
  mySelection = UserSelections.objects.all().values()
  Y = SRIcalculator(id)
  SRI=Y['SRI']
  kf1=Y['kf1']
  kf2 = Y['kf2']
  kf3 = Y['kf3']
  UserSelection = Y['user_sel']
  H = Y['H']
  DHW = Y['DHW']
  C = Y['C']
  V = Y['V']
  L = Y['L']
  DE = Y['DE']
  E = Y['E']
  EV = Y['EV']
  MC = Y['MC']
  Hmax = Y['Hmax']
  DHWmax = Y['DHWmax']
  Cmax = Y['Cmax']
  Vmax = Y['Vmax']
  Lmax = Y['Lmax']
  DEmax = Y['DEmax']
  Emax = Y['Emax']
  EVmax = Y['EVmax']
  MCmax = Y['MCmax']
  N_H = Y['N_H']
  N_DHW = Y['N_DHW']
  N_C = Y['N_C']
  N_V = Y['N_V']
  N_L = Y['N_L']
  N_DE = Y['N_DE']
  N_E = Y['N_E']
  N_EV = Y['N_EV']
  N_MC = Y['N_MC']
  N_Hmax = Y['N_Hmax']
  N_DHWmax = Y['N_DHWmax']
  N_Cmax = Y['N_Cmax']
  N_Vmax = Y['N_Vmax']
  N_Lmax = Y['N_Lmax']
  N_DEmax = Y['N_DEmax']
  N_Emax = Y['N_Emax']
  N_EVmax = Y['N_EVmax']
  N_MCmax = Y['N_MCmax']
  W_EV = Y['W_EV']
  Sum_N = Y['Sum_N']
  Sum_N_Max = Y['Sum_N_Max']
  Smartness = Y['Smartness']
  N_Smartness = Y['N_Smartness']
#  Y = calcSRI()

  template = loader.get_template('SRI_result.html')
  context = {
    'myLevels': myLevels,
    'myDomainWeight' : myDomainWeight,
    'myImpactWeight' : myImpactWeight,
    'myServices' : myServices,
    'mySelection' : mySelection,
    'SRI' : SRI,
    'kf1': kf1,
    'kf2': kf2,
    'kf3': kf3,
    'UserSelection' : UserSelection,
    'id' : id,
    'H' : H,
    'DHW': DHW,
    'C': C,
    'V': V,
    'L': L,
    'DE': DE,
    'E': E,
    'EV': EV,
    'MC': MC,
    'Hmax': Hmax,
    'DHWmax': DHWmax,
    'Cmax': Cmax,
    'Vmax': Vmax,
    'Lmax': Lmax,
    'DEmax': DEmax,
    'Emax': Emax,
    'EVmax': EVmax,
    'MCmax': MCmax,
    'N_H': N_H,
    'N_DHW': N_DHW,
    'N_C': N_C,
    'N_V': N_V,
    'N_L': N_L,
    'N_DE': N_DE,
    'N_E': N_E,
    'W_EV' : W_EV,
    'N_EV': N_EV,
    'N_MC': N_MC,
    'N_Hmax': N_Hmax,
    'N_DHWmax': N_DHWmax,
    'N_Cmax': N_Cmax,
    'N_Vmax': N_Vmax,
    'N_Lmax': N_Lmax,
    'N_DEmax': N_DEmax,
    'N_Emax': N_Emax,
    'N_EVmax': N_EVmax,
    'N_MCmax': N_MCmax,
    'Sum_N' : Sum_N,
    'Sum_N_Max': Sum_N_Max,
    'Smartness': Smartness,
    'N_Smartness': N_Smartness
  }
  return HttpResponse(template.render(context, request))


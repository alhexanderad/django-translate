from django.shortcuts import render

from django.shortcuts import render
from django.utils.translation import gettext as _

def cars(resquest):
  
  color = _('orange')

  return render(resquest, 'cars/car.html',{'color':color})

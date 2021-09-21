from django.shortcuts import render
from django.utils.translation import gettext as _

def home(resquest):
  title = _('Homepage')

  return render(resquest, 'base/home.html',{'title':title})

from django.shortcuts import render

def home(resquest):
  return render(resquest, 'base/home.html',{})

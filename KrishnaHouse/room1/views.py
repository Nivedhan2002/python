from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import BioData

# Create your views here.

def something(request):
    return HttpResponse('Hmmmmmmmm')

def forhtml(request):
    return render(request, 'pranava.html', {'a':'Whooooo', 'ish':kunjesh()})


class kunjesh(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    State = forms.CharField(max_length = 30)
    City = forms.CharField(max_length = 30)
    About = forms.CharField()
    dob = forms.DateField()

def fordb(request):
    if request.method == 'POST':
        a = BioData(Name = request.POST.get('name'),
                     Age = request.POST.get('age'), 
                     State = request.POST.get('State'),
                      City = request.POST.get('City'),
                       About = request.POST.get('About'), 
                       DOB = request.POST.get('dob'))
        a.save()
    return HttpResponseRedirect('/room1/')
from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from Commits3.forms import AdForm
from Commits3.models import Ad


def showAllAds(request):
    today = datetime.now()
    allAds = Ad.objects.filter(expirationDate__gte=today).order_by('expirationDate')
    return render(request, 'showAllAds.html', {'AllAds': allAds})


def addAd(request):
    if request.method == 'GET':
        formAd = AdForm(request.POST or None)
        return render(request, "AdForm.html", {'formAd': formAd, })
    if request.method == 'POST':
        ad = Ad.objects.create(name=request.POST['name'],
                               description=request.POST['description'],
                               cost=request.POST['cost'])
        ad.save()
        messages.success(request, 'Dodano ogłoszenie!')
    return redirect('showAllAds')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from pymarketcap import Pymarketcap
from django.core import serializers

from .forms import Currency1

import simplejson as json


def index(request):
    if request.method == 'POST':
        form = Currency1(request.POST)

        if form.is_valid():
        	name = form.cleaned_data['name']
        	coinmarketcap = Pymarketcap()
        	coininfo_unicode = coinmarketcap.ticker(name)
        	coininfo = json.dumps(coininfo_unicode)
        	context = {'coininfo': coininfo_unicode}
        	return render(request, 'dashboard/coinprofile.html', context)

    else:
        form = Currency1()
    return render(request, 'dashboard/index.html', {'form': form})
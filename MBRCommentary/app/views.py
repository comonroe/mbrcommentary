"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *
from .forms import *
from .tables import *
from django_tables2 import RequestConfig

def home(request):
    table = COGSTable(COGS.objects.all())
    table2 = OPEXTable(OPEX.objects.all())
    RequestConfig(request, paginate={'per_page': 9000}).configure(table)
    RequestConfig(request, paginate={'per_page': 9000}).configure(table2)
    return render(request, 'app/home.html', {
        'table': table,
        'table2': table2
     })

def edit_cogs(request, OrgDetail):
    cog = COGS.objects.get(OrgDetail=OrgDetail)
    table = COGSdetailTable(COGS.objects.filter(OrgDetail=OrgDetail))
    title = 'COGS: ' + OrgDetail
    if request.method == "POST":
        form = COGSForm(request.POST, instance=cog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = COGSForm(instance=cog)
    return render(request, 'app/edit.html', {
        'form': form,
        'table': table,
        'title': title
     })

def edit_opex(request, OrgDetail):
    opex = OPEX.objects.get(OrgDetail=OrgDetail)
    table = OPEXdetailTable(OPEX.objects.filter(OrgDetail=OrgDetail))
    title = 'OPEX: ' + OrgDetail
    if request.method == "POST":
        form = COGSForm(request.POST, instance=opex)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = COGSForm(instance=opex)
    return render(request, 'app/edit.html', {
        'form': form,
        'table': table,
        'title': title
     })

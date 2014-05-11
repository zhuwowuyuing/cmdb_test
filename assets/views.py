
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_device(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DeviceForm()

    t = get_template('assets/create_device.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_device(request):
  
    list_items = Device.objects.all()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_device.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def search_device(request):
    return ;

def view_device(request, asset):
    device_instance = Device.objects.get(asset = asset)

    t=get_template('assets/view_device.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_device(request, asset):

    device_instance = Device.objects.get(asset = asset)

    form = DeviceForm(request.POST or None, instance = device_instance)

    if form.is_valid():
        form.save()

    t=get_template('assets/edit_device.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_server(request):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ServerForm()

    t = get_template('assets/create_server.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_server(request):
  
    list_items = Server.objects.all()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_server.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_server(request, asset):
    server_instance = Server.objects.get(asset = asset)

    t=get_template('assets/view_server.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_server(request, asset):

    server_instance = Server.objects.get(asset=asset)

    form = ServerForm(request.POST or None, instance = server_instance)

    if form.is_valid():
        form.save()

    t=get_template('assets/edit_server.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_usinginfo(request):
    form = UsingInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UsingInfoForm()

    t = get_template('assets/create_usinginfo.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_usinginfo(request):
  
    list_items = UsingInfo.objects.all()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_usinginfo.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_usinginfo(request, asset):
    usinginfo_instance = UsingInfo.objects.get(asset = asset)

    t=get_template('assets/view_usinginfo.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_usinginfo(request, asset):

    usinginfo_instance = UsingInfo.objects.get(asset = asset)

    form = UsingInfoForm(request.POST or None, instance = usinginfo_instance)

    if form.is_valid():
        form.save()

    t=get_template('assets/edit_usinginfo.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_finance(request):
    form = FinanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FinanceForm()

    t = get_template('assets/create_finance.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_finance(request):
  
    list_items = Finance.objects.all()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_finance.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_finance(request, asset):
    finance_instance = Finance.objects.get(asset = asset)

    t=get_template('assets/view_finance.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_finance(request, asset):

    finance_instance = Finance.objects.get(asset = asset)

    form = FinanceForm(request.POST or None, instance = finance_instance)

    if form.is_valid():
        form.save()

    t=get_template('assets/edit_finance.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_maninfo(request):
    form = ManInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ManInfoForm()

    t = get_template('assets/create_maninfo.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_maninfo(request):
  
    list_items = ManInfo.objects.all()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_maninfo.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_maninfo(request, id):
    maninfo_instance = ManInfo.objects.get(id = id)

    t=get_template('assets/view_maninfo.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_maninfo(request, id):

    maninfo_instance = ManInfo.objects.get(id=id)

    form = ManInfoForm(request.POST or None, instance = maninfo_instance)

    if form.is_valid():
        form.save()

    t=get_template('assets/edit_maninfo.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

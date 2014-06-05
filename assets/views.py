#coding=utf8
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render
# from django.views.generic.detail import DetailView
# from django.views.generic import ListView
from django.db.models import Count
from datetime import datetime
import copy

# app specific files

from models import *
from forms import *

def index(request):
    page_title='Dashboard'
    statusCount=Servers.objects.values('status').annotate(dcount=Count('status'))
    modelCount=Servers.objects.values('model').annotate(dcount=Count('model')).order_by('model')
    return render(request, "index.html", locals())


# def create_device(request):
#     form = DeviceForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = DeviceForm()
#
#     t = get_template('assets/create_device.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def list_device(request):
#
#     list_items = Device.objects.all()
#     paginator = Paginator(list_items ,15)
#
#
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#
#     try:
#         list_items = paginator.page(page)
#     except :
#         list_items = paginator.page(paginator.num_pages)
#
#     t = get_template('assets/list_device.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
# # def search_device(request):
# #     isdisplay = False
# #     if 'asset' in request.GET:
# #         isdisplay = True
# #         search_asset = request.GET.get('asset', '')
# #         list_items = Device.objects.filter(asset__icontains=search_asset)
# #         if not list_items:
# #             nodata = True
# #         paginator = Paginator(list_items ,10)
# #
# #         try:
# #             page = int(request.GET.get('page', '1'))
# #         except ValueError:
# #             page = 1
# #         try:
# #             list_items = paginator.page(page)
# #         except :
# #             list_items = paginator.page(paginator.num_pages)
# #
# #         t = get_template('assets/search_device.html')
# #         c = RequestContext(request,locals())
# #         return HttpResponse(t.render(c))
# #     else:
# #         return render(request, "assets/search_device.html")
# def search_device(request):
#     if request.method == "GET":
#         searchform = DeviceSearchForm(request.GET)
#         if searchform.is_valid():
#             data = searchform.cleaned_data
#             asset = data.get('asset','')
#             asset_old = data.get('asset_old','')
#             district        = data.get('district','')
#             company         = data.get('company','')
#             type            = data.get('type','')
#             subtype         = data.get('subtype','')
#             manufacturer    = data.get('manufacturer','')
#             model           = data.get('model','')
#             serialno    = data.get('serialno','')
#
#             list_items = Device.objects.filter(asset__icontains=asset,
#                                                asset_old__icontains=asset_old,
#                                                district__icontains = district,
#                                                company__icontains = company,
#                                                type__icontains = type,
#                                                subtype__icontains = subtype,
#                                                manufacturer__icontains = manufacturer,
#                                                model__icontains = model,
#                                                serialno__icontains = serialno)
#             paginator = Paginator(list_items ,15)
#
#             try:
#                 page = int(request.GET.get('page', '1'))
#             except ValueError:
#                 page = 1
#             try:
#                 list_items = paginator.page(page)
#             except :
#                 list_items = paginator.page(paginator.num_pages)
#
#             t = get_template('assets/search_device.html')
#             c = RequestContext(request,locals())
#             return HttpResponse(t.render(c))
#     else:
#         searchform = DeviceSearchForm()
#     return render(request, "assets/search_device.html", locals())
#
# def view_device(request, asset):
#     device_instance = Device.objects.get(asset = asset)
#
#     t=get_template('assets/view_device.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
# def edit_device(request, asset):
#
#     device_instance = Device.objects.get(asset = asset)
#
#     form = DeviceForm(request.POST or None, instance = device_instance)
#
#     if form.is_valid():
#         form.save()
#
#     t=get_template('assets/edit_device.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
# def create_server(request):
#     form = ServerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ServerForm()
#
#     t = get_template('assets/create_server.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def list_server(request):
#
#     list_items = Server.objects.all()
#     paginator = Paginator(list_items ,15)
#
#
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#
#     try:
#         list_items = paginator.page(page)
#     except :
#         list_items = paginator.page(paginator.num_pages)
#
#     t = get_template('assets/list_server.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def view_server(request, asset):
#     server_instance = Server.objects.get(asset = asset)
#
#     t=get_template('assets/view_server.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
# def edit_server(request, asset):
#
#     server_instance = Server.objects.get(asset=asset)
#
#     form = ServerForm(request.POST or None, instance = server_instance)
#
#     if form.is_valid():
#         form.save()
#
#     t=get_template('assets/edit_server.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
# def create_usinginfo(request):
#     form = UsingInfoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = UsingInfoForm()
#
#     t = get_template('assets/create_usinginfo.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def list_usinginfo(request):
#
#     list_items = UsingInfo.objects.all()
#     paginator = Paginator(list_items ,15)
#
#
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#
#     try:
#         list_items = paginator.page(page)
#     except :
#         list_items = paginator.page(paginator.num_pages)
#
#     t = get_template('assets/list_usinginfo.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def view_usinginfo(request, asset):
#     usinginfo_instance = UsingInfo.objects.get(asset = asset)
#
#     t=get_template('assets/view_usinginfo.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
# def edit_usinginfo(request, asset):
#
#     usinginfo_instance = UsingInfo.objects.get(asset = asset)
#
#     form = UsingInfoForm(request.POST or None, instance = usinginfo_instance)
#
#     if form.is_valid():
#         form.save()
#
#     t=get_template('assets/edit_usinginfo.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
# def create_finance(request):
#     form = FinanceForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = FinanceForm()
#
#     t = get_template('assets/create_finance.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def list_finance(request):
#
#     list_items = Finance.objects.all()
#     paginator = Paginator(list_items ,15)
#
#
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#
#     try:
#         list_items = paginator.page(page)
#     except :
#         list_items = paginator.page(paginator.num_pages)
#
#     t = get_template('assets/list_finance.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def view_finance(request, asset):
#     finance_instance = Finance.objects.get(asset = asset)
#
#     t=get_template('assets/view_finance.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
# def edit_finance(request, asset):
#
#     finance_instance = Finance.objects.get(asset = asset)
#
#     form = FinanceForm(request.POST or None, instance = finance_instance)
#
#     if form.is_valid():
#         form.save()
#
#     t=get_template('assets/edit_finance.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
# def create_maninfo(request):
#     form = ManInfoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ManInfoForm()
#
#     t = get_template('assets/create_maninfo.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def list_maninfo(request):
#
#     list_items = ManInfo.objects.all()
#     paginator = Paginator(list_items ,15)
#
#
#     try:
#         page = int(request.GET.get('page', '1'))
#     except ValueError:
#         page = 1
#
#     try:
#         list_items = paginator.page(page)
#     except :
#         list_items = paginator.page(paginator.num_pages)
#
#     t = get_template('assets/list_maninfo.html')
#     c = RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
#
#
# def view_maninfo(request, id):
#     maninfo_instance = ManInfo.objects.get(id = id)
#
#     t=get_template('assets/view_maninfo.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))
#
# def edit_maninfo(request, id):
#
#     maninfo_instance = ManInfo.objects.get(id=id)
#
#     form = ManInfoForm(request.POST or None, instance = maninfo_instance)
#
#     if form.is_valid():
#         form.save()
#
#     t=get_template('assets/edit_maninfo.html')
#     c=RequestContext(request,locals())
#     return HttpResponse(t.render(c))

def create_servers(request):
    page_title='新增服务器'
    form = ServersForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ServersForm()

    t = get_template('assets/create_servers.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_servers(request):
    page_title='服务器列表'
    list_items = Servers.objects.all()
    count = list_items.count()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_servers.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_servers(request, asset):
    page_title='服务器详情'
    servers_instance = Servers.objects.get(asset = asset)
    form = ServersForm(None, instance = servers_instance)
    # form.fields['asset'].widget.attrs['readonly'] = True
    for field in servers_instance._meta.get_all_field_names():
        if field != 'status':
            form.fields[field].widget.attrs['readonly'] = True
        else:
            form.fields[field].widget.attrs['disabled'] = True

    list_log = ModLog.objects.filter(asset = asset, typename=str(type(servers_instance))).order_by('-mtime')
    t=get_template('assets/view_servers.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_servers(request, asset):
    page_title='编辑服务器信息'
    servers_instance = Servers.objects.get(asset = asset)

    old_instance = copy.deepcopy(servers_instance)
    form = ServersForm(request.POST or None, instance = servers_instance)

    if form.is_valid():
        if form.has_changed():
            for filed in form.changed_data:
                log = ModLog(typename=str(type(servers_instance)),asset=servers_instance.asset, mtime= datetime.now(), field=servers_instance._meta.get_field(filed).verbose_name,
                         oldvalue=old_instance.__dict__[filed], newvalue=form.data.get(filed,''))
                log.save()

        form.save()

    t=get_template('assets/edit_servers.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def search_servers(request):
    page_title='搜索服务器'
    if request.method == "GET":
        searchform = ServersSearchForm(request.GET)
        if searchform.is_valid():
            data = searchform.cleaned_data
            asset = data.get('asset','')
            asset_old = data.get('asset_old','')
            type = data.get('type','')
            subtype = data.get('subtype','')
            manufacturer = data.get('manufacturer','')
            model = data.get('model','')
            building = data.get('building','')
            location = data.get('location','')
            consignee = data.get('consignee','')
            hostname = data.get('hostname','')
            vendor = data.get('vendor','')
            status = data.get('status','')
            if status == None or status == 'None':
                list_items = Servers.objects.filter(asset__icontains = asset,
                                                    asset_old__icontains = asset_old,
                                                    type__icontains = type,
                                                    subtype__icontains = subtype,
                                                    manufacturer__icontains = manufacturer,
                                                    model__icontains = model,
                                                    building__icontains = building,
                                                    location__icontains = location,
                                                    consignee__icontains = consignee,
                                                    hostname__icontains = hostname,
                                                    vendor__icontains = vendor
                                                    )
            else:
                list_items = Servers.objects.filter(asset__icontains = asset,
                                                    asset_old__icontains = asset_old,
                                                    type__icontains = type,
                                                    subtype__icontains = subtype,
                                                    manufacturer__icontains = manufacturer,
                                                    model__icontains = model,
                                                    building__icontains = building,
                                                    location__icontains = location,
                                                    consignee__icontains = consignee,
                                                    hostname__icontains = hostname,
                                                    vendor__icontains = vendor,
                                                    status = status
                                                    )
            count = list_items.count()
            paginator = Paginator(list_items ,15)

            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                list_items = paginator.page(page)
            except :
                list_items = paginator.page(paginator.num_pages)

            t = get_template('assets/search_servers.html')
            c = RequestContext(request,locals())
            return HttpResponse(t.render(c))
    else:
        searchform = ServersSearchForm()
    return render(request, "assets/search_servers.html", locals())

def groupbymodel_servers(request):
    page_title='按型号统计'
    modelCount=Servers.objects.values('model').annotate(dcount=Count('model')).order_by('model')
    results={}
    for item in modelCount:
        key = item['model']
        value = item['dcount']
        results[key]=value
    results=sorted(results.items())
    return render(request, "assets/groupbymodel_servers.html", locals())

def groupbystatus_servers(request):
    page_title='按使用状态统计'
    # modelCount=Servers.objects.values('status').annotate(dcount=Count('status')).order_by('status')
    modelCount={}
    for item in Status.objects.all():
        modelCount[item.status]=item.servers_set.count()

    return render(request, "assets/groupbystatus_servers.html", locals())

def create_status(request):
    page_title='添加使用状态'
    form = StatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StatusForm()

    t = get_template('assets/create_status.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_status(request):
    page_title='使用状态列表'
    list_items = Status.objects.all()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('assets/list_status.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_status(request, status):
    page_title='编辑使用状态'
    status_instance = Status.objects.get(status = status)

    form = StatusForm(request.POST or None, instance = status_instance)

    if form.is_valid():
        if form.data.get('exclusive', False) != status_instance.exclusive:
            log = ModLog(asset=status_instance.status, mtime= datetime.now(), field='exclusive',
                         oldvalue=status_instance.exclusive, newvalue=str(form.data.get('exclusive', False)))
            log.save()
        form.save()

    t=get_template('assets/edit_status.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
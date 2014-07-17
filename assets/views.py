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

from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.decorators import login_required

from .forms import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request,{'username':username}))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form': form,}))

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

@login_required
def chgpwd(request):
    page_title="修改密码"
    if request.method == 'GET':
        form = ChangepwdForm()
        return render_to_response('chgpwd.html', RequestContext(request, locals()))
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                changepwd_success=True
                return render_to_response('index.html', RequestContext(request,locals()))
            else:
                oldpassword_is_wrong=True
                return render_to_response('chgpwd.html', RequestContext(request, locals()))
        else:
            return render_to_response('chgpwd.html', RequestContext(request, locals()))


@login_required
def index(request):
    page_title='Dashboard'
    statusCount=Servers.objects.values('status').annotate(dcount=Count('status'))
    modelCount=Servers.objects.values('model').annotate(dcount=Count('model')).order_by('model')
    return render(request, "index.html", locals())


@login_required
def create_servers(request):
    page_title='新增服务器'
    form = ServersForm(request.POST or None)
    if form.is_valid():
        form.save()
        asset= form.data.get("asset")
        url = "/assets/servers/edit/%s"%(asset)
        return HttpResponseRedirect(url)

    t = get_template('assets/create_servers.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

    #
    # asset= form.cleaned_data[asset]
    # url = "assets/servers/edit/%s"%(asset)
    # return HttpResponseRedirect(url)

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

@login_required
def edit_servers(request, asset):
    page_title='编辑服务器信息'
    servers_instance = Servers.objects.get(asset = asset)

    old_instance = copy.deepcopy(servers_instance)
    form = ServersForm(request.POST or None, instance = servers_instance)
    list_log = ModLog.objects.filter(asset = asset, typename=str(type(servers_instance))).order_by('-mtime')

    if form.is_valid():
        if form.has_changed():
            for filed in form.changed_data:
                log = ModLog(typename=str(type(servers_instance)),asset=servers_instance.asset, mtime= datetime.now(),
                             field=servers_instance._meta.get_field(filed).verbose_name,
                             oldvalue=old_instance.__dict__[filed], newvalue=form.data.get(filed,''))
                log.save()

        form.save()

    t=get_template('assets/edit_servers.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required
def delete_servers(request, asset):
    Servers.objects.get(asset = asset).delete()
    searchform = ServersSearchForm()
    return HttpResponseRedirect("/assets/servers/search/",locals())
    # return render(request, "assets/search_servers.html", locals())


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


def statistic_servers(request):
    page_title='概述报表'
    modelCount=Servers.objects.values('model').annotate(dcount=Count('model')).order_by('model')
    model_statistic={}
    for item in modelCount:
        key = item['model']
        value = item['dcount']
        model_statistic[key]=value
    model_statistic=sorted(model_statistic.items())

    status_statistic={}
    for item in Status.objects.all():
        status_statistic[item.status]=item.servers_set.count()

    building_statistic={}
    buildingCnt=Servers.objects.values('building').annotate(dcount=Count('building')).order_by('building')
    for item in buildingCnt:
        key = item['building']
        value = item['dcount']
        building_statistic[key]=value
    building_statistic=sorted(building_statistic.items())

    location_statistic={}
    locationCnt=Servers.objects.values('location').annotate(dcount=Count('location')).order_by('location')
    for item in locationCnt:
        key = item['location']
        value = item['dcount']
        location_statistic[key]=value
    location_statistic=sorted(location_statistic.items())

    return render(request, "assets/statistic_servers.html", locals())

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
    status_statistic={}
    for item in Status.objects.all():
        status_statistic[item.status]=item.servers_set.count()

    return render(request, "assets/groupbystatus_servers.html", locals())

@login_required
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

@login_required
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



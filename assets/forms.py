#coding=utf8
from django import forms
from models import *



class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

class DeviceSearchForm(forms.Form):
    asset = forms.CharField(label='资产编号', max_length=60, required=False)
    asset_old = forms.CharField(label='旧资产编号', max_length=60, required=False)
    district = forms.CharField(label='所在地区', max_length=60, required=False)
    company = forms.CharField(label='账上所属公司', max_length=60, required=False)
    type = forms.CharField(label='类别', max_length=60, required=False)
    subtype = forms.CharField(label='子类别', max_length=60, required=False)
    manufacturer = forms.CharField(label='品牌', max_length=60, required=False)
    model = forms.CharField(label='型号', max_length=100, required=False)
    serialno  = forms.CharField(label='序列号', max_length=100, required=False)



class ServerForm(forms.ModelForm):

    class Meta:
        model = Server
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)



class UsingInfoForm(forms.ModelForm):

    class Meta:
        model = UsingInfo
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(UsingInfoForm, self).__init__(*args, **kwargs)



class FinanceForm(forms.ModelForm):

    class Meta:
        model = Finance
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(FinanceForm, self).__init__(*args, **kwargs)



class ManInfoForm(forms.ModelForm):

    class Meta:
        model = ManInfo
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ManInfoForm, self).__init__(*args, **kwargs)


#coding=utf8
from django import forms
from django.forms import ModelChoiceField
from models import *

#
#
# class DeviceForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Device
# 		# exclude = [] # uncomment this line and specify any field to exclude it from the form
#
# 	def __init__(self, *args, **kwargs):
# 		super(DeviceForm, self).__init__(*args, **kwargs)
#
# class ServerForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Server
# 		# exclude = [] # uncomment this line and specify any field to exclude it from the form
#
# 	def __init__(self, *args, **kwargs):
# 		super(ServerForm, self).__init__(*args, **kwargs)
#
#
#
# class UsingInfoForm(forms.ModelForm):
#
# 	class Meta:
# 		model = UsingInfo
# 		# exclude = [] # uncomment this line and specify any field to exclude it from the form
#
# 	def __init__(self, *args, **kwargs):
# 		super(UsingInfoForm, self).__init__(*args, **kwargs)
#
#
#
# class FinanceForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Finance
# 		# exclude = [] # uncomment this line and specify any field to exclude it from the form
#
# 	def __init__(self, *args, **kwargs):
# 		super(FinanceForm, self).__init__(*args, **kwargs)
#
#
#
# class ManInfoForm(forms.ModelForm):
#
# 	class Meta:
# 		model = ManInfo
# 		exclude = [] # uncomment this line and specify any field to exclude it from the form
#
# 	def __init__(self, *args, **kwargs):
# 		super(ManInfoForm, self).__init__(*args, **kwargs)

class ServersForm(forms.ModelForm):

	class Meta:
		model = Servers
		# exclude = [] # uncomment this line and specify any field to exclude it from the form

	def __init__(self, *args, **kwargs):
		super(ServersForm, self).__init__(*args, **kwargs)

class StatusForm(forms.ModelForm):

	class Meta:
		model = Status
		# exclude = [] # uncomment this line and specify any field to exclude it from the form

	def __init__(self, *args, **kwargs):
		super(StatusForm, self).__init__(*args, **kwargs)


# class DeviceSearchForm(forms.Form):
# 	asset = forms.CharField(label='资产编号', max_length=60, required=False)
# 	asset_old = forms.CharField(label='旧资产编号', max_length=60, required=False)
# 	district = forms.CharField(label='所在地区', max_length=60, required=False)
# 	company = forms.CharField(label='账上所属公司', max_length=60, required=False)
# 	type = forms.CharField(label='类别', max_length=60, required=False)
# 	subtype = forms.CharField(label='子类别', max_length=60, required=False)
# 	manufacturer = forms.CharField(label='品牌', max_length=60, required=False)
# 	model = forms.CharField(label='型号', max_length=100, required=False)
# 	serialno  = forms.CharField(label='序列号', max_length=100, required=False)


class ServersSearchForm(forms.Form):
	asset           =forms.CharField(label='资产编号', max_length=60, required=False)
	asset_old       =forms.CharField(label='旧资产编号', max_length=60, required=False)
	type            =forms.CharField(label='类别', max_length=60, required=False)
	subtype         =forms.CharField(label='子类别', max_length=60, required=False)
	manufacturer    =forms.CharField(label='品牌', max_length=60, required=False)
	model           =forms.CharField(label='型号', max_length=100, required=False)
	status		    =ModelChoiceField(label='使用状态', queryset=Status.objects.all(), required=False)
	building        =forms.CharField(label='机房(所处位置)',max_length=60, required=False)
	location        =forms.CharField(label='机柜',max_length=60, required=False)
	consignee       =forms.CharField(label='托管编号',max_length=60, required=False)
	hostname        =forms.CharField(label='主机名',max_length=60, required=False)
	vendor          =forms.CharField(label='供应商',max_length=200, required=False)


class LoginForm(forms.Form):
	username = forms.CharField(
		required=True,
		label=u"用户名",
		error_messages={'required': '请输入用户名'},
		widget=forms.TextInput(
			attrs={
				'placeholder':u"用户名",
			}
		),
	)
	password = forms.CharField(
		required=True,
		label=u"密码",
		error_messages={'required': u'请输入密码'},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':u"密码",
			}
		),
	)

	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"用户名和密码为必填项")
		else:
			cleaned_data = super(LoginForm, self).clean()

class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"原密码",
                }
        ),
        )
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"新密码",
                }
        ),
        )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"确认密码",
                }
        ),
        )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data

class ModLogSearchForm(forms.Form):
    typename        =forms.CharField(label="类型", max_length=60, required=False)
    asset           =forms.CharField(label='资产编号', max_length=60, required=False)
    moduser         =forms.CharField(label='修改人', max_length=60, required=False)
    field           =forms.CharField(label='字段名称',max_length=60, required=False)
    comment         =forms.CharField(label='备注',max_length=500, required=False)
    beforemtime     =forms.DateTimeField(label="修改于之前", required=False)
    aftermtime      =forms.DateTimeField(label="修改于之后", required=False)


from django import forms
from models import *



class DeviceForm(forms.ModelForm):
	
    class Meta:
        model = Device	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)



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


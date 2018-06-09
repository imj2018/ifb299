from django import forms

class HireForm(forms.Form):
    id = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    instrument = forms.CharField(required=True)
    days = forms.CharField(required=True)
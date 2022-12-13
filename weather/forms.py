from django import forms


class CityForm(forms.Form):
    name = forms.CharField()

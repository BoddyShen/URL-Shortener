from django import forms


class LongURLForm(forms.Form):
    long_url = forms.URLField(label='Long URL')

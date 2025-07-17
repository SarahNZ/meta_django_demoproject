from django import forms
from django.forms.widgets import NumberInput, RadioSelect

FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]

class DemoForm(forms.Form):
    name = forms.CharField(widget = forms.Textarea(attrs = {'rows': 5}))
    email = forms.EmailField(label = "Enter email address")
    reservation_date = forms.DateField(widget = NumberInput(attrs = {'type': 'date'}))
    favorite_dish = forms.ChoiceField(widget = RadioSelect, choices = FAVORITE_DISH)
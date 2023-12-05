"""Forms of the project."""
from django import forms
# Create your forms here.
class ThingsForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)

from django import forms
from random import *
from django_countries.fields import CountryField
CHOICES = [('M', 'Male'), ('F', 'Female')]

class InputForm(forms.Form):
	heard_of_cryptocurrency = forms.BooleanField(label='Have you ever heard of cryptocurrency? (Tick for yes)', required=False)
	purchased_cryptocurrency = forms.BooleanField(label='Have you ever purchased cryptocurrency? (Tick for yes)', required=False)
	consider_valid = forms.BooleanField(label='Do you consider cryptocurrency a valid form of currency? (Tick for yes)', required=False)
	advertisement_as_monetization = forms.IntegerField(label='On a scale from 1-10 (1 being bad), what is your current view of advertising as a monetisation option?', required=True, min_value=1, max_value=10)
	mining_intensity = forms.IntegerField(widget=forms.HiddenInput())
	performance_hits = forms.IntegerField(label='On a scale of 1-10 (1 being not affected), how much did you notice a performance drop on your device?', required=True, min_value=1, max_value=10)
	experience = forms.IntegerField(label='On a scale of 1-10 (1 being not affected), how much does the mining in the browser affect your browsing experience?', required=True, min_value=1, max_value=10)
	consider_solution = forms.IntegerField(label='On a scale of 1-10 (1 being a bad alternative), from your experience on this page, and the information provided above, what is your view towards cryptocurrency mining in the browser as an alternative solution to advertising?', required=True, min_value=1, max_value=10)
	sex = forms.CharField(label='What is your sex?', widget=forms.Select(choices=CHOICES))
	age = forms.IntegerField(label='What is your age?', required=True, min_value=0, max_value=125)
	country = CountryField().formfield()






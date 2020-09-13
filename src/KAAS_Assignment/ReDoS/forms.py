from django import forms
class MyForm(forms.Form):
    regexString = forms.CharField(max_length=500, label="Please enter a regular expression")
    inputString = forms.CharField(max_length=500, label="Please enter an input for the regular expression")
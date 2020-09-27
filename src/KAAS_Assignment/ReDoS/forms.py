from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label="Enter Username")
    email = forms.CharField(max_length=320, label="Enter Email Address")
class RegexForm(forms.Form):
    regexString = forms.CharField(max_length=200, label="Enter regex string")
    inputString = forms.CharField(max_length=300, label="Enter input string")
class SpaceTrimmer(forms.Form):
    spaceInput = forms.CharField(max_length=300,label="Enter string for space trimming")
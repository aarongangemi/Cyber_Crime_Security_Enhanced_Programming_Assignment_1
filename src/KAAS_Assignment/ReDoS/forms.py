## Purpose: Classes used to set attributes for each form
## Contributors: Aaron Gangemi, Kay Men Yap
from django import forms
import sys
## Max size is not set to allow for ReDoS to occur
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=sys.maxsize, label="Enter Username")
    email = forms.CharField(max_length=sys.maxsize, label="Enter Email Address")
class RegexForm(forms.Form):
    regexString = forms.CharField(max_length=200, label="Enter regex string")
    inputString = forms.CharField(max_length=sys.maxsize, label="Enter input string")
class SpaceTrimmer(forms.Form):
    spaceInput = forms.CharField(max_length=sys.maxsize,label="Enter string for space trimming")

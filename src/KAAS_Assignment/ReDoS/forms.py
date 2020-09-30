'''
Purpose: Classes used to set attributes for each form
Patch: Added max_length in order to limit the input string size
Contributors from Master: Aaron Gangemi, Kay Men Yap,

patchBranch Contributors: Sho Kogota, Alex McLeod
Changes: added max length values for inputs
'''
from django import forms
import sys
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, label="Enter Username")
    email = forms.CharField(max_length=sys.maxsize, label="Enter Email Address")
class RegexForm(forms.Form):
    regexString = forms.CharField(max_length=200, label="Enter regex string")
    inputString = forms.CharField(max_length=300, label="Enter input string")
class SpaceTrimmer(forms.Form):
    spaceInput = forms.CharField(max_length=sys.maxsize,label="Enter string for space trimming")
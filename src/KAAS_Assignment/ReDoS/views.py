from django.shortcuts import render, redirect
from django.utils.text import Truncator
from django.views import View
from .forms import RegisterForm, RegexForm, SpaceTrimmer
import re
import time
import threading
from django.http import Http404

## Purpose: The views control what the user will see including error messages.
## Also completes any regex processing
## Contributors: Aaron Gangemi, Kay Men Yap

##Purpose: To process get and post for the regex page
class Register(View):
    ## Display form
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    ##Once button is clicked, process posted form
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                ## set username and email data and test against regex
                request.session["username"] = form.cleaned_data["username"]
                usernameResult = re.search("^([a-zA-Z]+)*$", form.cleaned_data["username"])
                emailResult = re.search("^\S+@\S+\.\S+$", form.cleaned_data["email"])
                if usernameResult is None: ## if username is invalid
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": "Error: invalid username, please try again. Note: The username can only be characters from a to z uppercase or lowercase with no spaces"})
                if emailResult is None: ## if email is invalid
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": "Error: Invalid Email entered, please try again. Note: An email address must end with @<DomainName>.com"})
                else: ## if valid
                    return redirect('regextest')
## Purpose: To process the get and post for the regex testing page
class RegexTest(View):

    ##Display form for regex tester
    def get(self, request, *args, **kwargs):
        form = RegexForm()
        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"]})

    ##Once user clicks button on regex page to process regex
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                ## process form
                form = RegexForm(request.POST)
                if form.is_valid():
                    result = re.search(form.cleaned_data["regexString"], form.cleaned_data["inputString"])
                    ## if a result exists, render page with appropriate result
                    if result:
                        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"],
                                                                    "result": "Result: String found in regex"})
                    else:
                        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"],
                                                                    "result": "Result: No result"})
            except:
                return render(request, "regexchecker.html", {"form": form, "username": request.session["username"], "result": "Error: invalid regex"})
        else:
            return redirect("regextest")

## Purpose: Process get and post for space trimmer
class SpaceTrim(View):
    ## display page with space trimmer form
    def get(self, request):
        form = SpaceTrimmer()
        return render(request, "spacetrimmer.html", {"form": form, "username": request.session["username"]})
    ## If user clicks for result then call post to process result
    def post(self, request):
        if request.method == 'POST':
            form = SpaceTrimmer(request.POST)
            if form.is_valid():
                inputTrim = re.search("^[ \t]+|[ \t]+$", form.data["spaceInput"])
                if inputTrim:
                    return render(request, "spacetrimmer.html", {"form": form, "username": request.session["username"], "result": "Trimmed String: " + inputTrim.string.strip()})
                else:
                    return render(request, "spacetrimmer.html",{"form": form, "username": request.session["username"], "result": "Result: Nothing needed trimming"})
        else:
            return redirect("inputTrim")

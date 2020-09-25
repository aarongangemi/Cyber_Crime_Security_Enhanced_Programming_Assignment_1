from django.shortcuts import render, redirect
from django.utils.text import Truncator
from django.views import View
from .forms import RegisterForm, RegexForm, SpaceTrimmer
import re
import time
import threading
from django.http import Http404


# Create your views here.
class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request, *args, **kwargs):
        startTime = time.time()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                request.session["username"] = form.cleaned_data["username"]
                usernameResult = re.search("^([a-zA-Z]+)*$", form.cleaned_data["username"])
                emailResult = re.search("^\S+@\S+\.\S+$", form.cleaned_data["email"])
                if emailResult is None or usernameResult is None:
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": "Invalid username or email was entered, " +
                                                                        "please try again with no spaces"})
                else:
                    return redirect('regextest')


class RegexTest(View):

    def get(self, request, *args, **kwargs):
        form = RegexForm()
        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"]})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                form = RegexForm(request.POST)
                if form.is_valid():
                    result = re.search(form.cleaned_data["regexString"], form.cleaned_data["inputString"])
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


class SpaceTrim(View):
    def get(self, request):
        form = SpaceTrimmer()
        return render(request, "spacetrimmer.html", {"form": form, "username": request.session["username"]})

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

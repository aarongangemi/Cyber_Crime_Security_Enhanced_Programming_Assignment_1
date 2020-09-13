from django.shortcuts import render, redirect
from django.utils.text import Truncator
from django.views import View
from .forms import RegisterForm, RegexForm
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
                str = "@"*1000000
                request.session["username"] = form.cleaned_data["username"]
                result = re.search("^\S+@\S+\.\S+$", form.cleaned_data["email"])
                if result is None:
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message":"Invalid Email entered, please try again"})
                else:
                    return redirect('regextest')


class RegexTest(View):

    def get(self, request, *args, **kwargs):
        form = RegexForm()
        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"]})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = RegexForm(request.POST)
            if form.is_valid():
                result =  re.search(form.cleaned_data["regexString"], form.cleaned_data["inputString"])
                if result:
                    return render(request,"regexchecker.html",{"form": form, "username": request.session["username"], "result": "Result: String found in regex"})
                else:
                    return render(request,"regexchecker.html",{"form": form, "username": request.session["username"], "result": "Result: No result"})
        else:
            return redirect("regextest")

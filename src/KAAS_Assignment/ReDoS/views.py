from django.shortcuts import render, redirect
from django.utils.text import Truncator
from django.views import View
from .forms import RegisterForm, RegexForm
import re
import time
from .exceptionTypes import emailLengthException, emailInvalidException
from django.http import Http404


# Create your views here.
class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                str = "@"*1000000
                request.session["username"] = form.cleaned_data["username"]
                # get the input email address
                email = form.cleaned_data.get("email")
                try:
                    # if the length of the email is greater than 320 raise an exception
                    if(len(email) > 320):
                        raise emailLengthException("Error: Email address must be less than 320 characters")

                    emailValidationRegex = "^[^@]+@([^\.@]+\.[^\.@]+)+$"
                    result = re.search(emailValidationRegex, form.cleaned_data["email"])
                    if result is None:
                        raise emailInvalidException("Error: Invalid Email entered, please try again. Note: An email"
                                                    " address must end with @<DomainName>.com")

                # catch the length email exception if it occurs
                except emailLengthException as emailException:
                    errorMessage = emailException.args[0]
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": errorMessage})

                # catch email invalid exception if it occurs
                except emailInvalidException as emailException:
                    errorMessage = emailException.args[0]
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": errorMessage})
                # add exception if regex is invalid
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
                try:
                    inputRegex = form.cleaned_data["regexString"]

                    result = re.search(inputRegex, form.cleaned_data["inputString"])

                    if result:
                        return render(request,"regexchecker.html",{"form": form, "username": request.session["username"], "result": "Result: String found in regex"})
                    else:
                        return render(request,"regexchecker.html",{"form": form, "username": request.session["username"], "result": "Result: No result"})

                except Exception:
                    errorMessage = "Error: regex entered is invalid"
                    return render(request, "regexchecker.html", {"form": form, "username": request.session["username"],
                                                                 "result": errorMessage})

        else:
            return redirect("regextest")

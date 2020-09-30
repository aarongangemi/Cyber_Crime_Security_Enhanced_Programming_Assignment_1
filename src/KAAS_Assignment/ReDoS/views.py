'''
Purpose: The views control what the user will see including error messages.
Also completes any regex processing
Patch: Added exceptions that occurs when input string sizes are over threshold
here is already input size limitation set, but these exception could add defense-in-depth incase one fails
Contributors from Master: Aaron Gangemi, Kay Men Yap,

PatchBranch Contributers: Sho Kogota, Alex McLeod
Comments correspond with changes by patch branch programmers
'''
from django.shortcuts import render, redirect
from django.views import View
# rure engine used instead of re engine
import rure
from .forms import RegisterForm, RegexForm, SpaceTrimmer
from .exceptionTypes import emailLengthException, emailInvalidException, usernameInvalidException, regexInputLengthException
from .exceptionTypes import trimLengthException, usernameLengthException, inputStringLengthException

# Create your views here.

# Changes: input restrictions, regular expressions changed, rure regular expression engine used and exception handling
# added
class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                request.session["username"] = form.cleaned_data["username"]


                try:

                    username = form.cleaned_data.get("username")
                    if (len(username) > 200):
                        raise emailLengthException("Error: username must be less than or equal to 200 characters")
                    # regex changed "^([a-zA-Z]+)*$" to "^[a-zA-Z]+$" avoiding +)* that can cause catastrophic
                    # backtracking with particular input
                    usernameValidationRegex = "^[a-zA-Z]+$"
                    # rure engine used to match usernames to regex
                    usernameResult = rure.search(usernameValidationRegex, username)
                    # added exception handling where if an invalid username is entered an Exception message is thrown
                    if usernameResult is None:
                        raise usernameInvalidException("Error: invalid username, please try again. Note: The username " 
                                                       "can only be characters from a to z uppercase or lowercase with "
                                                       "no spaces")

                    # get the input email address
                    email = form.cleaned_data.get("email")
                    # if the length of the email is greater than 320 raise an exception
                    if (len(email) > 320):
                        raise emailLengthException("Error: Email address must be less than or equal to 320 characters")
                    # email regex changed from "^\S+@\S+\.\S+$" to "^[^@]+@([^\.@]+\.[^\.@]+)+$"
                    emailValidationRegex = "^[^@]+@([^\.@]+\.[^\.@]+)+$"
                    # rure engine used to match email input with regex
                    emailResult = rure.search(emailValidationRegex, email)
                    # added a raise exception if an invalid email is entered
                    if emailResult is None:
                        raise emailInvalidException("Error: Invalid Email entered, please try again. Note: An email"
                                                    " address must end with @<DomainName>.com")

                # catch length exception if the input into the text box is too large
                except usernameLengthException as lengthException:
                    errorMessage = lengthException.args[0]
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": errorMessage})
                # catch username invalid exception if it occurs
                except usernameInvalidException as invalidException:
                    errorMessage = invalidException.args[0]
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": errorMessage})

                # catch the length email exception if it occurs
                except emailLengthException as lengthException:
                    errorMessage = lengthException.args[0]
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": errorMessage})

                # catch email invalid exception if it occurs
                except emailInvalidException as invalidException:
                    errorMessage = invalidException.args[0]
                    return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": errorMessage})
                # add exception if regex is invalid
                else:
                    return redirect('regextest')
            else:
                return render(request, "register.html", {"form": RegisterForm(),
                                                             "message": "form is invalid"})


# Changes: length of input string is limited, rure engine used, exception handling added
class RegexTest(View):

    def get(self, request, *args, **kwargs):
        form = RegexForm()
        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"]})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                form = RegexForm(request.POST)
                if form.is_valid():
                    userRegex = form.cleaned_data["regexString"]
                    inputString = form.cleaned_data["inputString"]
                    # check and raise an error if length of the input regex is over 200 characters
                    if len(userRegex) > 200:
                        raise regexInputLengthException("Error: input regex must be less than or equal to 200")

                    # check and raise an error if length of string to match is too long
                    if len(inputString) > 300:
                        raise inputStringLengthException("Error: input string must be less than or equal to 300")

                    # use rure engine to match
                    result = rure.search(userRegex, inputString)
                    if result:
                        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"],
                                                                    "result": "Result: String found in regex"})
                    else:
                        return render(request, "regexchecker.html", {"form": form, "username": request.session["username"],
                                                                    "result": "Result: No result"})

            # catch length exception
            except regexInputLengthException as lengthException:
                errorMessage = lengthException[0]
                return render(request, "regexchecker.html",
                              {"form": form, "username": request.session["username"], "result": errorMessage})
            # catch length exception
            except inputStringLengthException as lengthException:
                errorMessage = lengthException[0]
                return render(request, "regexchecker.html",
                              {"form": form, "username": request.session["username"], "result": errorMessage})
            # catch exception if regex invalid
            except:
                return render(request, "regexchecker.html", {"form": form, "username": request.session["username"], "result": "Error: invalid regex"})
        else:
            return redirect("regextest")

# Changes: length of string input is limited, exception handling
class SpaceTrim(View):
    def get(self, request):
        form = SpaceTrimmer()
        return render(request, "spacetrimmer.html", {"form": form, "username": request.session["username"]})

    def post(self, request):
        if request.method == 'POST':
            form = SpaceTrimmer(request.POST)
            if form.is_valid():
                try:
                    trimData = form.data["spaceInput"]
                    # check input length
                    if len(trimData) > 300:
                        raise trimLengthException("Error: input data to trim must be less than 300 characters")
                    inputTrim = rure.search("^[ \t]+|[ \t]+$", trimData)
                    if inputTrim:
                        return render(request, "spacetrimmer.html", {"form": form,
                                                                     "username": request.session["username"],
                                                                     "result": "Trimmed String: " + form.cleaned_data["spaceInput"].strip()})
                    else:
                        return render(request, "spacetrimmer.html", {"form": form,
                                                                     "username": request.session["username"],
                                                                     "result": "Result: Nothing needed trimming"})
                # catch any errors if they occur
                except trimLengthException as lengthException:
                    errorMessage = lengthException.args[0]
                    return render(request, "spacetrimmer.html", {"form": form,
                                                                 "username": request.session["username"],
                                                                 "result": errorMessage})
        else:
            return redirect("inputTrim")

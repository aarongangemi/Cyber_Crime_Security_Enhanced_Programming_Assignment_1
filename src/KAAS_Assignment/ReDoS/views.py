from django.shortcuts import render
from django.views import View
from .forms import MyForm
# Create your views here.
class RedosPage(View):
    def get(self, request, *args, **kwargs):
        form = MyForm()
        return render(request,"index.html",{'form' : form})


    def post(self, request, *args,**kwargs):
        if request.method == 'POST':
            form = MyForm(request.POST)
            if(form.is_valid()):
                print("Input String was: " + form.cleaned_data["inputString"])
                print("Regex String was: " + form.cleaned_data["regexString"])
        return render(request, "index.html", {'form': form})
from django.shortcuts import render
from django.views import View


class RedosPage(View):
    def get(self, request, *args, **kwargs):
        return render(request,"index.html",{'form' : 1234567})

    ##def post(self, request, *args,**kwargs):


from django.http import HttpResponseRedirect
from django.shortcuts import render

def bsjtool(request):
    return render(request, 'means/bsjtool.html')

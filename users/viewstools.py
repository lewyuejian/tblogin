from django.shortcuts import render
from users.forms import DataCheck
from users.bsjtool.terminalCheck import ProtocolCheck
from django.http import JsonResponse


def bsjtool(request):
    ctx={}
    if request.POST:
        data_o=request.POST['bsjpact']
        check=ProtocolCheck()
        ctx['rlt']=check.check_bsj(data_o)
    return render(request, "means/bsjtool.html", ctx)



def check_bsj_data(request):
    ctx = {}
    if request.POST:
        data_o = request.POST['bsjpact']
        check = ProtocolCheck()
        ctx['rlt'] = check.check_bsj(data_o)
    return  render(request,"means/datacheck.html",ctx)

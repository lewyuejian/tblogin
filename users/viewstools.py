from django.shortcuts import render
from users.forms import DataCheck
from users.bsjtool.terminalCheck import ProtocolCheck
from django.http import JsonResponse


def bsjtool(request):
    """
    校验29协议数据视图方法
    :param request:
    :return:
    """
    ctx={}
    if request.POST:
        data_o=request.POST['bsjpact']
        check=ProtocolCheck()
        ctx['rlt']=check.check_bsj(data_o)
    return render(request, "means/bsjtool.html", ctx)

def gbtool(request):
    """
    校验部标协议数据视图方法
    :param request:
    :return:
    """
    ctx={}
    if request.POST:
        data_o=request.POST['gbpact']
        check=ProtocolCheck()
        ctx['rlt']=check.check_bsj(data_o)
    return render(request, "means/bsjtool.html", ctx)

def v3tool(request):
    """
    校验V3协议数据视图方法
    :param request:
    :return:
    """
    ctx={}
    if request.POST:
        data_o=request.POST['v3pact']
        check=ProtocolCheck()
        ctx['rlt']=check.check_bsj(data_o)
    return render(request, "means/bsjtool.html", ctx)

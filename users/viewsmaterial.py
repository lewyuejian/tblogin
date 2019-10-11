from django.shortcuts import render


def account(request):
    return render(request, 'material/account.html')

def data(request):
    return render(request,'material/data.html')
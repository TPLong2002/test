from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Value
from pathlib import Path

def Form(request):
    hd = 'Gửi đến X'
    p = Path(__file__).with_name('ct.txt')
    with p.open('r', encoding="utf-8") as f:
        ct = f.read()
    context = {'ct':ct, 'hd':hd}
    return render(request, 'First/New.html', context)
def ykien(request):
    if request.POST['sel'] == '1':
        messages.info(request, 'Không sao cả')
    if request.POST['sel'] == '2':
        messages.info(request, 'Qua qua nhắn tin cho mình cảm súc của bạn')
    if request.POST['sel'] == '3':
        messages.info(request, 'Tiếc quá')
    if request.POST['sel'] == '4':
        messages.info(request, 'Mình sẽ chủ động rời khỏi thế giới của bạn')
    # if Value.objects.all():
    #     vl = Value.objects.all()[0]
    #     vl.Value = request.POST['sel']
    #     vl.save()
    # else:
    #     vl = Value.objects.create(Value = request.POST['sel'])
    #     vl.save()
    vl = Value.objects.create(Value = request.POST['sel'])
    vl.save()
    return redirect('/')
def kq(request):
    # kq = Value.objects.all()[0].Value
    # Time = Value.objects.all()[0].Time
    # context = {'kq': kq, 'Time':Time}
    obj = Value.objects.all()
    context = {'obj': obj}
    return render(request, 'First/Value.html', context)


from django.shortcuts import render, redirect

def Form(request):
    ct = ''
    context = {'ct':ct}
    return render(request, 'First/New.html', context)

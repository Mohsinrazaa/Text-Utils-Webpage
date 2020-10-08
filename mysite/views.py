# This file is created by Mohsin Raza
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'defualt')
    removepunc = request.POST.get('removepunc' , 'off')
    fullcaps = request.POST.get('capitalize' , 'off')
    newline = request.POST.get('newline' , 'off')

    if removepunc == "on":
        punctations = '''!()-[]{}:;'"/,<>.\?@#$%^&*~`_'''
        analyzed = ""
        for char in djtext:
            if char not in punctations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Puntuations', 'analyzed_Text':analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to upper', 'analyzed_Text': analyzed}
        djtext = analyzed

    if(newline == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r" :
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_Text': analyzed}
        djtext = analyzed
    return render(request, 'analyze.html', params)
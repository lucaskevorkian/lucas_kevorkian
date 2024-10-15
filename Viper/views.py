from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def motor(request):
    return render(request, "motor.html")

def precio(request):
    return render(request, "precio.html")


def buscar_auto(request):
    return render(request, "buscar_auto.html")

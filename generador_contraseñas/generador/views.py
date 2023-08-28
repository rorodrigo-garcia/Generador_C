from django.shortcuts import render
import random

def about(request):
    return render(request,'generador/about.html')


def home(request):
    return render(request,'generador/home.html')

def password(request):

    caracteres = list('abcdefghijkmnñlopqrstuvwxyz')
    contraseña_generada =''
    tamaño = int(request.GET.get('length'))
   
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKMNÑLOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        caracteres.extend(list('!#$%&/*-+')) 

    if request.GET.get('number'):
        caracteres.extend(list('123456789'))

    for caracter in range(tamaño):
        contraseña_generada += random.choice(caracteres)

    return render(request, 'generador/password.html',{'password': contraseña_generada})

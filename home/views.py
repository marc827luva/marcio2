from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("A view index funcionou, Wow!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim<h1>")

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def ajudar(request):
    return render(request,'ajudar.html')

def exibiritem(request,id):
    return render(request,'exibiritem.html',{'id':id})

def perfil(request,id):
    return render(request,'perfil.html',{'id':id})



# Create your views here.

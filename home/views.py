from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("A view index funcionou, Wow!")

# Create your views here.

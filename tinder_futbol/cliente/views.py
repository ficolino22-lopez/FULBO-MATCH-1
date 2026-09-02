from django.shortcuts import render

def index_cliente(request):
    return render(request, 'cliente/index.html')
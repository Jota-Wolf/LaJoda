from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html', {})

def casas(request):
    return render(request, 'core/casas.html', {})

def depto(request):
    return render(request, 'core/departamento.html', {})

def terrenos(request):
    return render(request, 'core/terrenos.html', {})

def casa_limache(request):
    return render(request, 'core/casa-limache.html', {})

def depto_limache(request):
    return render(request, 'core/dpto-limache.html', {})

def terreno_limache(request):
    return render(request, 'core/terreno-limache.html', {})

def quienes_somos(request):
    return render(request, 'core/quienes-somos.html', {})

def contacto(request):
    return render(request, 'core/contacto.html', {})

def galeria(request):
    return render(request, 'core/galeria.html', {})
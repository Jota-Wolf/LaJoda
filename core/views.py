from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import timezone
from .models import Casa
from .models import Departamento
from .models import Terreno
# Create your views here.

class CasaLimachePageView(TemplateView):
    template_name = "core/casa-limache.html"

class CasasPageView(TemplateView):
    template_name = "core/casas.html"

    def get(self,request,*args, **kwargs):
        casas = Casa.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, self.template_name, {'casas': casas})

class ContactoPageView(TemplateView):
    template_name = "core/contacto.html"

class DepartamentoPageView(TemplateView):
    template_name = "core/departamento.html"

class DeptoLimachePageView(TemplateView):
    template_name = "core/depto-limache.html"

class GaleriaPageView(TemplateView):
    template_name = "core/galeria.html"

class IndexPageView(TemplateView):
    template_name = "core/index.html"

    def get(self,request,*args, **kwargs):
        casas = Casa.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, self.template_name, {'casas': casas})

class QuienesSomosPageView(TemplateView):
    template_name = "core/quienes-somos.html"

class TerrenoLimachePageView(TemplateView):
    template_name = "core/terreno-limache.html"

class TerrenosPageView(TemplateView):
    template_name = "core/terrenos.html"
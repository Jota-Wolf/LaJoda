from django.urls import path
from .views import CasaLimachePageView,CasaLimachePageView,ContactoPageView,DepartamentoPageView,DeptoLimachePageView,GaleriaPageView,IndexPageView,QuienesSomosPageView,TerrenoLimachePageView,TerrenosPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path("casa-limache/", CasaLimachePageView.as_view(), name="casa-limache"),
    path("casas/", CasaLimachePageView.as_view(), name="casas"),
    path("contacto/", ContactoPageView.as_view(), name="contacto"),
    path("departamento/", DepartamentoPageView.as_view(), name="departamento"),
    path("dpto-limache/", DeptoLimachePageView.as_view(), name="dpto-limache"),
    path("galeria/", GaleriaPageView.as_view(), name="galeria"),
    path("quienes-somos/", QuienesSomosPageView.as_view(), name="quienes-somos"),
    path("terreno-limache/", TerrenoLimachePageView.as_view(), name="terreno-limache"),
    path("terrenos/", TerrenosPageView.as_view(), name="terrenos"),
    
]


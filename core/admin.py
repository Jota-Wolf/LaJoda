from django.contrib import admin
from .models import Cliente
from .models import Casa
from .models import Departamento
from .models import Terreno
from .models import Galeria
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Casa)
admin.site.register(Departamento)
admin.site.register(Terreno)
admin.site.register(Galeria)
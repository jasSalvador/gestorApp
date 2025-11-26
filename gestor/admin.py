from django.contrib import admin
from .models import Organizacion, Integrante, Cuota, Gasto,ItemGasto


admin.site.register(Organizacion)
admin.site.register(Integrante)
admin.site.register(Cuota)
admin.site.register(Gasto)
admin.site.register(ItemGasto)
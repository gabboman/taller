from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Coches)
admin.site.register(Trabajadores)
admin.site.register(Trabajos)
admin.site.register(Piezas)

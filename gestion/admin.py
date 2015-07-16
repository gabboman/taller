from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Coche)
admin.site.register(Trabajador)
admin.site.register(Trabajo)
admin.site.register(Pieza)

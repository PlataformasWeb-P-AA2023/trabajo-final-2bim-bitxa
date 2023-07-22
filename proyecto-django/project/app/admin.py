from django.contrib import admin
from .models import Persona, Barrio, LocalComida, LocalRepuesto


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula')
    search_fields = ('nombres', 'apellidos', 'cedula')


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre', 'siglas')


class LocalComidaAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas', 'pago_permiso')
    search_fields = ('direccion', 'barrio__nombre', 'tipo_comida')
    list_filter = ('barrio', 'tipo_comida')

    def pago_permiso(self, obj):
        return obj.pago_permiso


class LocalRepuestoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'valor_mercaderia', 'pago_permiso')
    search_fields = ('direccion', 'barrio__nombre')
    list_filter = ('barrio',)

    def pago_permiso(self, obj):
        return obj.pago_permiso

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(LocalComida, LocalComidaAdmin)
admin.site.register(LocalRepuesto, LocalRepuestoAdmin)

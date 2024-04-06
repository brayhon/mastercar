from django.contrib import admin

#Para usar a class CAR do model precisa importar da pasta CARS do arquivo MODELS.PY da classe CAR 
from cars.models import Car, Brand

# Criei um class CarAdmin importei do Django a Class admin e escolhei o que deve aparecer no painel Admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value')
    search_fields = ('model', 'brand')

# Fazendo aparecer no painel registrando qual Class e Configurações do Admin
admin.site.register(Car, CarAdmin) 


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)
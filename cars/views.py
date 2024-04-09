from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model') #buscar todos carras quando acessar a URL /cars/
    
    search = request.GET.get('search') #Se o usuario passar o filtro Search na URL
    
    if search: #Vai retornar o Search buscado, retorna só o carro buscado
     cars = Car.objects.filter(model__icontains=search) #se contem a palavra buscada
    
    return render(
        request,
        'cars.html',
        {'cars': cars }
    )  
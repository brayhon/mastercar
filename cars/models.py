from django.db import models

class Car(models.Model):                        #Classe Car tem a Herança da class Model por padrão do Django
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.model #Dando nome do Model "MODELO DO CARRO" para SELF função padrão do Django (Clicar pra ver o que tanto tem.)
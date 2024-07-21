# my_app/models.py
from django.db import models
from django.contrib.auth.models import User

# my_app/models.py
from django.db import models

class Blockchain(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Coin(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Asset(models.Model):
    ASSET_TYPES = [
        ('currency', 'Currency'),
        ('item', 'Item'),
        # Añade otros tipos si es necesario
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ASSET_TYPES, default='currency')  # Agregar valor por defecto aquí
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Exchange(models.Model):
    from_asset = models.ForeignKey(Asset, related_name='from_asset', on_delete=models.CASCADE)
    to_asset = models.ForeignKey(Asset, related_name='to_asset', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_date = models.DateTimeField(auto_now_add=True)


class BlockchainIntegration(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()
    api_key = models.CharField(max_length=100)    


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    recommendation_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()  # Razonamiento de la recomendación

    def __str__(self):
        return f"Recommendation for {self.user} on {self.asset} and {self.coin}"
    

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, null=True, blank=True)
    preference_score = models.IntegerField() 

# my_app/models.py

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    required_assets = models.ManyToManyField(Asset, blank=True)
    required_coins = models.ManyToManyField(Coin, blank=True)

    def __str__(self):
        return self.name

# my_app/forms.py
from django import forms
from .models import Coin, Asset, BlockchainIntegration

class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['name', 'value']

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'type', 'value']

class BlockchainIntegrationForm(forms.ModelForm):
    class Meta:
        model = BlockchainIntegration
        fields = ['name', 'api_url', 'api_key']

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db import connection
from .models import UserPreference,Coin, Asset, Game
from .forms import CoinForm, AssetForm
from .models import Exchange
from .models import BlockchainIntegration
from .forms import BlockchainIntegrationForm
from .models import Asset, Coin, Recommendation
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'my_app/home.html')

def assets_list(request):
    assets = Asset.objects.all()
    return render(request, 'my_app/assets_list.html', {'assets': assets})

def coin_list(request):
    coins = Coin.objects.all()
    return render(request, 'my_app/coin_list.html', {'coins': coins})


def coin_create(request):
    if request.method == 'POST':
        form = CoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coins')
    else:
        form = CoinForm()
    return render(request, 'my_app/coin_form.html', {'form': form})

def coin_edit(request, pk):
    coin = get_object_or_404(Coin, pk=pk)
    if request.method == 'POST':
        form = CoinForm(request.POST, instance=coin)
        if form.is_valid():
            form.save()
            return redirect('coins')
    else:
        form = CoinForm(instance=coin)
    return render(request, 'my_app/coin_form.html', {'form': form})

def exchange_assets(request):
    if request.method == 'POST':
        from_asset_id = request.POST.get('from_asset')
        to_asset_id = request.POST.get('to_asset')
        amount = request.POST.get('amount')
        
        from_asset = Asset.objects.get(id=from_asset_id)
        to_asset = Asset.objects.get(id=to_asset_id)
        
        exchange = Exchange(from_asset=from_asset, to_asset=to_asset, amount=amount)
        exchange.save()
        
        return redirect('exchange_success')
    
    assets = Asset.objects.all()
    return render(request, 'my_app/exchange_assets.html', {'assets': assets})

def exchange_success(request):
    return render(request, 'my_app/exchange_success.html')

def check_coin_table(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'my_app_coin';")
        columns = cursor.fetchall()
    return JsonResponse({'columns': [col[0] for col in columns]})

def about(request):
    return render(request, 'my_app/about.html')

def contact(request):
    return render(request, 'my_app/contact.html')

def integration_list(request):
    integrations = BlockchainIntegration.objects.all()
    return render(request, 'my_app/integration_list.html', {'integrations': integrations})

def integration_create(request):
    if request.method == 'POST':
        form = BlockchainIntegrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('integration_list')
    else:
        form = BlockchainIntegrationForm()
    return render(request, 'my_app/integration_form.html', {'form': form})


@login_required
def recommendations_view(request):
    # Obtener preferencias del usuario actual
    user_preferences = UserPreference.objects.filter(user=request.user)

    # Obtener los IDs de los activos y monedas preferidos por el usuario actual
    preferred_assets = user_preferences.filter(asset__isnull=False).values_list('asset_id', flat=True)
    preferred_coins = user_preferences.filter(coin__isnull=False).values_list('coin_id', flat=True)

    # Encontrar usuarios similares basados en preferencias de activos y monedas
    similar_users = UserPreference.objects.exclude(user=request.user).filter(
        asset_id__in=preferred_assets
    ).values('user').distinct()

    # Obtener los activos y monedas preferidos por usuarios similares
    recommended_assets = Asset.objects.filter(
        userpreference__user__in=similar_users,
        id__in=preferred_assets
    ).distinct()

    recommended_coins = Coin.objects.filter(
        userpreference__user__in=similar_users,
        id__in=preferred_coins
    ).distinct()

    context = {
        'recommended_assets': recommended_assets,
        'recommended_coins': recommended_coins,
    }
    return render(request, 'my_app/recommendations.html', context)

@login_required
def game_recommendations_view(request):
    user = request.user

    # Obtener preferencias del usuario
    user_preferences = UserPreference.objects.filter(user=user)
    preferred_assets = user_preferences.filter(asset__isnull=False).values_list('asset_id', flat=True)
    preferred_coins = user_preferences.filter(coin__isnull=False).values_list('coin_id', flat=True)

    # Buscar juegos recomendados basados en los activos y monedas preferidos
    recommended_games = Game.objects.filter(
        required_assets__in=preferred_assets,
        required_coins__in=preferred_coins
    ).distinct()

    context = {
        'recommended_games': recommended_games,
    }
    return render(request, 'my_app/game_recommendations.html', context)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assets/', views.assets_list, name='assets_list'),
    path('coins/', views.coin_list, name='coin_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coin/create/', views.coin_create, name='coin_create'),
    path('coin/edit/<int:pk>/', views.coin_edit, name='coin_edit'),
    path('exchange/', views.exchange_assets, name='exchange_assets'),
    path('exchange/success/', views.exchange_success, name='exchange_success'),
    path('check_coin_table/', views.check_coin_table, name='check_coin_table'),
    path('integrations/', views.integration_list, name='integration_list'),
    path('integration/create/', views.integration_create, name='integration_create'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('game_recommendations/', views.game_recommendations_view, name='game_recommendations'),
]

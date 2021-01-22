from django.urls import path
from . import views

urlpatterns = [
    # Generic paths
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('stats/', views.my_stats, name='my_stats'),
    path('clients/', views.clients, name='clients'),
    path('faq/', views.faq, name='faq'),

    # Coach paths
    path('coach-dashboard/', views.coach_dashboard, name='coach-dashboard'),
    path('invite-players/', views.invite_players, name='invite-players'),
    path('enter-game/', views.enter_game, name='enter-game'),
    path('enter-stats/', views.enter_stats, name='enter-stats'),
    path('game-list/', views.game_list, name='game-list'),
    path('coach-dashboard-2/', views.coach_dashboard_2, name='coach-dashboard-2'),

    # Player paths
    path('player-dashboard/', views.player_dashboard, name='player-dashboard'),
    path('season-stats/', views.season_stats, name='season-stats'),
    path('team_comparison/', views.team_comparison, name='team-comparison'),
]

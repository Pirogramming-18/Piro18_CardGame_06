from django.urls import path
from . import views

app_name = "games"

urlpatterns= [
    path("", views.main_before, name="main"),
    path("login", views.login, name="login"),
    path("gamestart/<int:pk>", views.game_start, name="gamestart"),
    path("gamelist/<int:pk>", views.game_list, name="gamelist"),
    path("gameinfo/<int:pk>", views.game_info, name="gameinfo"),
    path("gamecounter/<int:pk>", views.game_counter, name="gamecounter"),
    path("gameranking", views.game_ranking, name="gameranking"),
]
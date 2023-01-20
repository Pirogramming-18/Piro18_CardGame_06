from django.urls import path
from . import views

app_name = "games"

urlpatterns= [
    path("", views.main, name="main"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("gamestart", views.game_start, name="gamestart"),
    path("gamelist", views.game_list, name="gamelist"),
    path("gameinfo/<int:pk>", views.game_info, name="gameinfo"),
    path("gameinfo/<int:pk>/delete", views.game_delete, name="gamedelete"),
    path("gamecounter/<int:pk>", views.game_counter, name="gamecounter"),
    path("gameranking", views.game_ranking, name="gameranking"),
]
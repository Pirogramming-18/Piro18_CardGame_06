from django.shortcuts import render, redirect
from server.apps.games.models import User,Game
from django.http.request import HttpRequest
import random

userkey = 3 

def main_before(request:HttpRequest, *args, **kwargs):
    pass

def main_after(request:HttpRequest, *args, **kwargs):
    pass

def login(request:HttpRequest, *args, **kwargs):
    pass

def game_start(request:HttpRequest, *args, **kwargs):
    pass

def game_list(request:HttpRequest, *args, **kwargs):
    pass

def game_info(request:HttpRequest, *args, **kwargs):
    pass

def game_counter(request:HttpRequest, *args, **kwargs):
    a = list(range(1,11))
    num = random.sample(a, 5)
    context={ "num":num, }
        
    if request.method == "POST":
        Game.objects.create(
            defend_card=request.POST["defend_card"],
        )
        user_recent = User.objects.last()
        return redirect(f"/gameinfo/{user_recent.id}")
    return render(request, "games/gamecounter.html", context=context) 

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass



import random
from django.shortcuts import render, redirect
from server.apps.games.models import User,Game
from django.http.request import HttpRequest
from .models import User, Game

userkey = 3 

def main_before(request:HttpRequest, *args, **kwargs):
    pass

def main_after(request:HttpRequest, *args, **kwargs):
    pass

def login(request:HttpRequest, *args, **kwargs):
    pass

def game_start(request:HttpRequest, pk,*args, **kwargs):
    a = list(range(0,11))
    cardnum = random.sample(a,5)
    users = User.objects.all()
    
    context = {
        "user" : users,
        "cardnum"  : cardnum
    }

    if request.method == "POST":
       Game.objects.create(
        attacker = request.POST['attcker'],
        defender = request.POST['defender'],
        attack_card = request.POST['attacker'], 
       ) 
       return redirect("/")
    
    return render("/gamestart.html",context=context)

def game_list(request:HttpRequest, *args, **kwargs):
    return render()

def game_info(request:HttpRequest, pk, *args, **kwargs):
  
    game = Game.objects.get(pk=pk)
    defender = game.defender.username
    attacker = game.attacker.username 
    attack_card = game.attack_card
    defend_card = game.defend_card
    status = game.status  

    context = {
        "attack_card" : attack_card,
        "defend_card" : defend_card,
        "attacker" : attacker,
        "defender" : defender,  
        "status" : status }

    if(status == 1):

            return render(f"gameinfo/{game.pk}",context=context )        
    if(status == 2):
            return render(f"gameinfo/{game.pk}",context=context)
    if(status == 3):
            return render(f"gameinfo/{game.pk}",context=context)

    return render(f"gameinfo/{game.pk}")

def game_counter(request:HttpRequest, *args, **kwargs):
    pass

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass



import random
from django.shortcuts import render, redirect
from .models import User, Game
from django.http.request import HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import random


def main(request:HttpRequest, *args, **kwargs):
    return render(request, "main.html")
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name='login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('/')

def game_start(request:HttpRequest,*args, **kwargs):
    a = list(range(0,11))
    cardnum = random.sample(a,5)
    users = User.objects.all()
    
    context = {
        "users" : users,
        "cardnum"  : cardnum
    }

    if request.method == "POST":
       Game.objects.create(
        attacker = User.objects.get(username=request.POST['attacker']),
        defender = User.objects.get(username=request.POST['defender']),
        attack_card = request.POST['attacker_card'], 
        status = 1,
       ) 
       return redirect("/gamelist")
    
    return render(request, template_name='game_start.html',context=context)

def game_list(request:HttpRequest, *args, **kwargs):
    return render(request, template_name='game_list.html')

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

def game_counter(request:HttpRequest, pk, *args, **kwargs):
    game = Game.objects.get(id=pk)
    defender = game.defender
    attacker = game.attacker
    attack_card = game.attack_card
    defend_card = game.defend_card

    a = list(range(1,11))
    num = random.sample(a, 5)
    context={ 
        "attacker" : attacker,
        "num" : num,
    }
    
    if request.method == "POST":
        game.defend_card=request.POST["defend_card"]
        game_rule = random.randint(1,2) # 1-> 클수록 이김, 2-> 작을수록 이김
        if (game_rule == 1) :
            if (game.attack_card > game.defend_card) :
                status = 2
                attacker.score += attack_card
                defender.score -= defend_card
            else :
                status = 3
                attacker.score -= attack_card
                defender.score += defend_card
        else :
            if (game.attack_card > game.defend_card) :
                status = 3
                attacker.score -= attack_card
                defender.score += defend_card
            else :
                status = 2
                attacker.score += attack_card
                defender.score -= defend_card
        game.status = status
        return redirect(f"/gameinfo/{game.pk}")
    return render(request, "/gamecounter.html", context=context) 

def game_ranking(request:HttpRequest, *args, **kwargs):
    users = User.objects.order_by("-score")
    context = {
        "users" : users,
    }
    return render(request, "/game_ranking.html", context=context)




import random
from django.shortcuts import render, redirect
from server.apps.games.models import User, Game
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
        "user" : users,
        "cardnum"  : cardnum
    }

    if request.method == "POST":
       Game.objects.create(
        attacker = request.POST['attcker'],
        defender = request.POST['defender'],
        attack_card = request.POST['attacker'], 
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
    user = User.objects.get(id=pk)
    game = Game.objects.get(id=pk)
    
    a = list(range(1,11))
    num = random.sample(a, 5)
    context={ 
        "user":user,
        "num":num
    }
    if request.method == "POST":
        Game.objects.create(
            defend_card=request.POST["defend_card"],
        )
        return redirect(f"/gameinfo/{user.pk}")
    return render(request, "games/gamecounter.html", context=context) 

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass



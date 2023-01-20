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
    all_game = Game.objects.all()
    allgame_reverse = all_game[::-1]
    context = {
        "allgame" : allgame_reverse,
    }
    return render(request, template_name='game_list.html', context=context)

def game_info(request:HttpRequest, pk, *args, **kwargs):
  
    game = Game.objects.get(pk=pk) 

    context = {
        "game": game}

    return render(request, "game_info.html", context=context)

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
            status = 2,
        )
        return redirect(f"/gameinfo/{user.pk}")
    return render(request, "games/gamecounter.html", context=context) 

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass

def game_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        game = Game.objects.get(id=pk)
        game.delete()
    return redirect("/gamelist")



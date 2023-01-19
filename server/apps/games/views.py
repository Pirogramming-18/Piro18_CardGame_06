from django.shortcuts import render, redirect
# from server.apps.games.models import User,Game
from django.http.request import HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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

def game_start(request:HttpRequest, *args, **kwargs):
    if request.method=="POST":
        return redirect("/gamelist")
    return render(request, template_name='game_start.html')

def game_list(request:HttpRequest, *args, **kwargs):
    return render(request, template_name='game_list.html')

def game_info(request:HttpRequest, *args, **kwargs):
    pass

def game_counter(request:HttpRequest, *args, **kwargs):
    pass

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass



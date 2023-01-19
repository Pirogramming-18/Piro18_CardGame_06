from django.shortcuts import render, redirect
from server.apps.games.models import User,Game
from django.http.request import HttpRequest

userkey = 3 

def main(request:HttpRequest, *args, **kwargs):
    return render(request, "main.html")

def login(request:HttpRequest, *args, **kwargs):
    pass

def game_start(request:HttpRequest, *args, **kwargs):
    pass

def game_list(request:HttpRequest, *args, **kwargs):
    pass

def game_info(request:HttpRequest, *args, **kwargs):
    pass

def game_counter(request:HttpRequest, *args, **kwargs):
    pass

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass



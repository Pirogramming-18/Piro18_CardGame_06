from django.shortcuts import render, redirect
from server.apps.games.models import User,Game
from django.http.request import HttpRequest

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
    pass

def game_ranking(request:HttpRequest, *args, **kwargs):
    pass



from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    score = models.IntegerField(null=True, blank=True, default=0)

class Game(models.Model):
    attacker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attack_user") # 공격자
    defender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="defend_user") # 수비자
    attack_card = models.IntegerField() # 공격자 숫자
    # 처음 공격시작시 공격자,수비자,공격자 카드는 정해지므로 일단 수비자카드와 상태는 null가능하게 설정
    defend_card = models.IntegerField(null=True, blank=True)  # 수비자 숫자  
    status = models.IntegerField() # 현재 게임 상태 1-> 진행중, 2-> 공격자가 이긴 게임, 3 -> 수비자가 이긴게임 

class Blog(models.Model):
    text = models.TextField()
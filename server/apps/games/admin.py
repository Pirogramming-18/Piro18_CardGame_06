# users/admin.py
from django.contrib import admin
from .models import Blog,Game,User

admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Game)
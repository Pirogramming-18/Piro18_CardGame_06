# users/admin.py
from django.contrib import admin
from games import models

admin.site.register(models.User)
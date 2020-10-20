from django.contrib import admin
from .models import news_data, Profile
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Profile)
admin.site.register(news_data)


from django.urls import path
from .views import *

app_name = 'blogApp'

urlpatterns = [
    path('apresentacao/', saudacao)
]

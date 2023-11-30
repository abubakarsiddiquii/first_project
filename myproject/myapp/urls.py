# myapp/urls.py

from django.urls import path
from .views import menu, kitchen

urlpatterns = [
    path('', menu, name='menu'),
    path('kitchen/', kitchen, name='kitchen'),
]




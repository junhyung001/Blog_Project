from django.urls import path

from .views import index, Board

urlpatterns=[
    path('', Board),
    path('index/', index)
]
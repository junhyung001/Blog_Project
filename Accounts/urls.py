from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'), #signup
    path('signin/', views.signup, name='signin'), #login
    path('logout/', views.signup, name='logout'), #logout
]
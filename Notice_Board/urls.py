from django.urls import path

from . import views

urlpatterns=[
    path('', views.Board),
    # 클래스를 불러오기위해 .as_view()함수를 붙임
    path('', views.Board, name="board_list"),
    path('create_board/', views.BoardCreate.as_view()),
    path('update_board/<int:pk>/', views.BoardUpdate.as_view()),
    path('delete_board/<int:pk>/', views.DeleteBoard),
    path('completed_board/<int:pk>/', views.CompletedBoard),

    path('index/', views.index),
]
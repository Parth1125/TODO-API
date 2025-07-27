from django.urls import path
from . import views

urlpatterns=[
    path('list', views.listTodo),
    path('details/<int:pk>/', views.detailListTodo)
]
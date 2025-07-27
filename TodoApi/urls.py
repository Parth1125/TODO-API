from django.urls import path
from . import views

urlpatterns=[
    path('', views.listTodo),
    path('<int:pk>/', views.detailListTodo)
]
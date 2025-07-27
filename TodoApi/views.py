from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

@api_view(['GET'])
def listTodo(request):
    todos= Todo.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailListTodo(request,pk):
    todo = Todo.objects.get(pk=pk)
    seriallizer = TodoSerializer(todo)
    return Response(seriallizer.data)
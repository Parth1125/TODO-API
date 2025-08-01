from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

@api_view(['GET',"POST"])
def listTodo(request):
    if request.method == 'GET':
        todos= Todo.objects.all()
        serializer = TodoSerializer(todos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer._errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detailListTodo(request,pk):
    todo = Todo.objects.get(pk=pk)
    seriallizer = TodoSerializer(todo)
    return Response(seriallizer.data)
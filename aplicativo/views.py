from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Item,Category,User
from .serializers import itemSerializer,categorySerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
 

# Create your views here.
@api_view(['POST'])
def create_item(request):
  items_v=itemSerializer(data=request.data)
  if Item.objects.filter(**request.data).exists():
    raise 
  if items_v.is_valid():
        items_v.save()
        return Response(items_v.data)
  
@api_view(['GET'])
def get_item(request,pk):
   try: 
      itens=Item.objects.get(pk=pk)
   except itens.DoesNotExist:
      return Response({"message":"O produto com o ID fornecido não foi encontrado."},status=status.HTTP_404_NOT_FOUND)
   serializer=itemSerializer(itens)
   return Response(serializer.data)

@api_view(['DELETE'])
def delete_item(request,pk):
   try: 
      itens=Item.objects.get(pk=pk)
   except itens.DoesNotExist:
      return Response({"message":"O item com o ID fornecido não foi encontrado."},status=status.HTTP_404_NOT_FOUND)
   itens.delete()
   return Response({"message": "Item excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_item(request,pk): 
    itens = get_object_or_404(Item, pk=pk)
    serializer = itemSerializer(instance=itens, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item atualizado com sucesso", "data": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
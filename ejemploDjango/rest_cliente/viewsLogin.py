from django.shortcuts import render
#framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
#authentication
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data =JSONParser().parse(request)
    #print(data)

    username = data['username']
    password = data['password']

    #validar usuario
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario no existe")
    
    #validar pass

    pass_valida = check_password(password,user.password)

    if not pass_valida :
        return Response("Contraseña incorrecta")

    #crear o recuperar un token 
    token, created = Token.objects.get_or_create(user=user)
    
    #retorno del token asociado al usuario
    return Response(token.key)




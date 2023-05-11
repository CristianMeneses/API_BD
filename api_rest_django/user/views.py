from django.shortcuts import render
 
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
 
from user.serializers import userSerializer
 

from user.models import user
 
class userViewSet(viewsets.ModelViewSet):    
    
    queryset = user.objects.all().order_by('user_id')
    serializer_class = userSerializer
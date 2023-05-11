from django.shortcuts import render
 
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
 
from enterprise.serializers import enterpriseSerializer
 

from enterprise.models import enterprise
 
class enterpriseViewSet(viewsets.ModelViewSet):    
    
    queryset = enterprise.objects.all().order_by('enterprise_id')
    serializer_class = enterpriseSerializer
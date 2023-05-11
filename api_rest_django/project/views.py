from django.shortcuts import render
 
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
 
from project.serializers import projectSerializer
 

from project.models import project
 
class projectViewSet(viewsets.ModelViewSet):    
    
    queryset = project.objects.all().order_by('project_id')
    serializer_class = projectSerializer
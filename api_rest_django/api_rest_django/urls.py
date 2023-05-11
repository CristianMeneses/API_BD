"""
URL configuration for api_rest_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
 
# Importamos 'DefaultRouter' de Django REST Framework y la vista 'user' 
from rest_framework.routers import DefaultRouter
from user import views as user_views
from enterprise import views as enterprise_views
from project import views as project_views

router = DefaultRouter()
router.register(r'user', user_views.userViewSet, basename='user')
router.register(r'enterprise', enterprise_views.enterpriseViewSet, basename='enterprise')
router.register(r'project', project_views.projectViewSet, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
 
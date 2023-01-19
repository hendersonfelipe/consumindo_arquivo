from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from consuarq.views import *

router = routers.DefaultRouter()
router.register('Pessoa/', PessoaViewSet)
router.register('Mulheres/Meeren/', MulheresViewSet, basename='Pessoa')
router.register('Nascimento/', NascimentoViewSet, basename='Pessoa2')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

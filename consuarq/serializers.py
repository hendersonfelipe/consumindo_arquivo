from rest_framework import serializers
from .models import *

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pessoa
        fields=['codigo', 'nome', 'sobrenome', 'sexo', 'altura', 'peso', 'nascimento', 'bairro', 'cidade', 'estado', 'numero', 'file']
    
    

    
    
    
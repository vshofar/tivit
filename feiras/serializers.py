
from rest_framework import serializers
from feiras.models import Feira


class FeiraSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Feira
        fields  = ('log', 'lat', 'set_sens', 'area_p', 'cod_dist', 'distrito', 'cod_sub_pref', 'sub_pref', 'regiao5', 
                    'regiao8', 'nome_feira','registro', 'logradouro', 'numero', 'bairro', 'referencia')

import sys
import os

# If you find a solution that does not need the two paths, please comment!
sys.path.append('/home/zack/program/prova/tivit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tivit.settings'

import django
django.setup()

from feiras.models import Feira
from feiras.serializers import FeiraSerializer


feira = Feira()


feira.log             = 1111 #models.BigIntegerField()
feira.lat             = 1111 #models.BigIntegerField()
feira.set_sens        = 1111 #models.BigIntegerField()
feira.area_p          = 1111 #models.BigIntegerField()
    
feira.cod_dist        = 11 #models.IntegerField()
feira.distrito        = 'dista' #models.CharField(max_length=100)

feira.cod_sub_pref    = 1111 #models.IntegerField()
feira.sub_pref        = 'subprefa' # models.CharField(max_length=100)

feira.regiao5         = 'r5a' #models.CharField(max_length=20)
feira.regiao8         = 'r8a' #models.CharField(max_length=20)

feira.nome_feira      = 'feira a' #models.CharField(max_length=200)
feira.registro        = 'registro a' #models.CharField(max_length=20)
    
feira.logradouro      = 'aaaaaaaaaaaaaa' #models.CharField(max_length=250)
feira.numero          = 'nnnnnnnnnnnnn' #models.CharField(max_length=50,blank=True)
feira.bairro          = 'bbbbbbbbb' #models.CharField(max_length=50)
feira.referencia      = 'rrrrrrrrrrr' #models.CharField(max_length=200,blank=True)


feira.save()



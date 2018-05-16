from django.db import models
from django.forms.models import model_to_dict
import json


class Feira(models.Model):

    '''
        Model class to manage 'Feira' Data.    
    '''

    log             = models.BigIntegerField()
    lat             = models.BigIntegerField()
    set_sens        = models.BigIntegerField()
    area_p          = models.BigIntegerField()
    
    cod_dist        = models.IntegerField()
    distrito        = models.CharField(max_length=100)

    cod_sub_pref    = models.IntegerField()
    sub_pref        = models.CharField(max_length=100)

    regiao5         = models.CharField(max_length=20)
    regiao8         = models.CharField(max_length=20)

    nome_feira      = models.CharField(max_length=200)
    registro        = models.CharField(max_length=20,unique=True)
    
    logradouro      = models.CharField(max_length=250)
    numero          = models.CharField(max_length=50,blank=True)
    bairro          = models.CharField(max_length=50)
    referencia      = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return self.nome_feira

    def toJson(self):
        dic = model_to_dict(self, fields=[field.name for field in self._meta.fields])
        return dic
        


    class Meta:
        ordering = ('id',)

    

    

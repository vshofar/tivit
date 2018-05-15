from django.db import models

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
    registro        = models.CharField(max_length=20)
    
    logradouro      = models.CharField(max_length=250)
    numero          = models.CharField(max_length=50,blank=True)
    bairro          = models.CharField(max_length=50)
    referencia      = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return self.nome_feira

    class Meta:
        ordering = ('id',)

    

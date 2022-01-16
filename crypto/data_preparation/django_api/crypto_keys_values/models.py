from django.db import models
from django.core.validators import RegexValidator

class Crypto(models.Model):
    
    chave = models.CharField(
        max_length= 255,
        validators=[RegexValidator('^[A-Z_]*$',
                               'Apenas palavras MAIÚSCULAS são permitidas.')]
                               )
    
    palavra = models.CharField(
        max_length= 255,
        validators=[RegexValidator('^[A-Z_]*$',
                               'Apenas palavras MAIÚSCULAS são permitidas.')]
                               )
    
    palavra_encriptada = models.IntegerField(null = True, blank = True, editable=True)

    def __str__(self):
        return self.chave


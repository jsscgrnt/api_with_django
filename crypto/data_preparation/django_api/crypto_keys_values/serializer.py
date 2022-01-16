from rest_framework import serializers
from crypto_keys_values.models import Crypto

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['chave', 'palavra', 'palavra_encriptada']
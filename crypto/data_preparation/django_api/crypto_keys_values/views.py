from rest_framework import viewsets
from crypto_keys_values.models import Crypto
from crypto_keys_values.serializer import CryptoSerializer

class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
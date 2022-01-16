from django.contrib import admin
from crypto_keys_values.models import Crypto

class Crypto_ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'chave', 'palavra', 'palavra_encriptada')
    list_display_links = ('id', 'chave', 'palavra')
    search_fields = ('chave', 'palavra')

admin.site.register(Crypto, Crypto_ModelAdmin)
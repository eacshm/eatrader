from django.contrib import admin

# Register your models here.
from .models import Cliente, Lancamento, Corretora, Operacao

admin.site.register(Cliente)
admin.site.register(Lancamento)
admin.site.register(Corretora)
admin.site.register(Operacao)
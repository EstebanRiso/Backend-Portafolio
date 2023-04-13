from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Asistant)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Estado)
admin.site.register(AuthPago)
admin.site.register(GiroAhorro)
admin.site.register(AuthDesbloqueo)
admin.site.register(Banco)
admin.site.register(Beneficiario)
admin.site.register(Certificado)
admin.site.register(Constructora)
admin.site.register(Proyecto)
admin.site.register(CertificadoProyecto)
admin.site.register(GiroEstado)
admin.site.register(DesbloqueoEstado)
admin.site.register(Factoring)
admin.site.register(DetallePago)
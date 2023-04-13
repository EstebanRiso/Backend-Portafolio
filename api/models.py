from django.db import models



class User(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True, unique=True)
    password = models.CharField(max_length=50, null=True)
    limite_creaciones = models.IntegerField(null=True)
    limite_consulta_espacial = models.IntegerField(null=True)



class Asistant(models.Model):
    id_voice = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    personality_promt = models.CharField(max_length=5000, null=True)



class Conversation(models.Model):
    topic = models.CharField(max_length=45, null=True)



class Message(models.Model):
    id_conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_asistant = models.ForeignKey(Asistant, to_field='id_voice', on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=2000, null=True)
    date = models.TimeField(null=True)



class Estado(models.Model):
    nombre_estado = models.CharField(max_length=255, null=True, unique=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    


class AuthPago(models.Model):
    llamado = models.IntegerField(null=True)
    linea_subsidio = models.CharField(max_length=255, null=True)
    titulo = models.CharField(max_length=255, null=True)
    tipo_autorizacion = models.CharField(max_length=255, null=True)
    consolidada = models.BooleanField(null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



class GiroAhorro(models.Model):
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    numero_autorizacion_pago = models.ForeignKey(AuthPago, on_delete=models.CASCADE, null=True)
    comuna = models.CharField(max_length=255, null=True)
    numero_resolucion = models.IntegerField(null=True)
    fecha_resolucion = models.DateField(null=True)
    fecha_emision_documento = models.DateField(null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



class AuthDesbloqueo(models.Model):
    numero_autorizacion_desbloqueo = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey('Estado', on_delete=models.SET_NULL, null=True)
    numero_autorizacion_giro = models.ForeignKey('GiroAhorro', on_delete=models.SET_NULL, null=True)
    numero_autorizacion_pago = models.ForeignKey('AuthPago', on_delete=models.SET_NULL, null=True)
    antecedentes = models.CharField(max_length=255, null=True)
    materia = models.CharField(max_length=255, null=True)
    adjuntos = models.CharField(max_length=255, null=True)
    id_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class Banco(models.Model):
    id_banco = models.IntegerField(primary_key=True)
    nombre_banco = models.CharField(max_length=45, null=True)
    id_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class Beneficiario(models.Model):
    rut_beneficiario = models.IntegerField(primary_key=True)
    id_banco = models.ForeignKey(Banco, on_delete=models.SET_NULL, null=True)
    dv_beneficiario = models.CharField(max_length=1, null=True)
    nombre_beneficiario = models.CharField(max_length=255, null=True)
    numero_cuenta = models.IntegerField(null=True)
    numero_autorizacion = models.IntegerField(null=True)
    cantidad_ahorro = models.IntegerField(null=True)
    id_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class Certificado(models.Model):
    id_certificado = models.IntegerField(primary_key=True)
    rut_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.SET_NULL, null=True)
    certificado_nombre = models.CharField(max_length=255, null=True)
    certificado_anio = models.IntegerField(null=True)
    id_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class Constructora(models.Model):
    rut_constructora = models.IntegerField(primary_key=True)
    dv_constructora = models.CharField(max_length=1, null=True)
    nombre_constructora = models.CharField(max_length=255, null=True)
    id_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class Proyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    rut_constructora = models.ForeignKey(Constructora, on_delete=models.SET_NULL, null=True)
    numero_autorizacion_pago = models.ForeignKey('AuthPago', on_delete=models.SET_NULL, null=True)
    nombre_proyecto = models.CharField(max_length=255, null=True)
    siglas_proyecto = models.CharField(max_length=45, null=True)
    id_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)



class CertificadoProyecto(models.Model):
    id_certificado_proyecto = models.IntegerField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)
    id_certificado = models.ForeignKey(Certificado, on_delete=models.SET_NULL, null=True)



class GiroEstado(models.Model):
    numero_autorizacion_giro = models.ForeignKey('GiroAhorro', on_delete=models.CASCADE)
    id_estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500, null=True, blank=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)



class DesbloqueoEstado(models.Model):
    numero_autorizacion_desbloqueo = models.ForeignKey('AuthDesbloqueo', on_delete=models.CASCADE)
    id_estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500, null=True, blank=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)



class Factoring(models.Model):
    rut_factoring = models.IntegerField(primary_key=True)
    dv_factoring = models.CharField(max_length=1, null=True, blank=True)
    nombre_factoring = models.CharField(max_length=255, null=True, blank=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)



class DetallePago(models.Model):
    numero_cheque = models.IntegerField(null=True, blank=True)
    monto = models.FloatField(null=True, blank=True)
    rut_constructora = models.ForeignKey('Constructora', on_delete=models.CASCADE, null=True, blank=True)
    rut_factoring = models.ForeignKey('Factoring', on_delete=models.CASCADE, null=True, blank=True)
    numero_autorizacion_pago = models.IntegerField(null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    pertenece = models.BooleanField(null=True, blank=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
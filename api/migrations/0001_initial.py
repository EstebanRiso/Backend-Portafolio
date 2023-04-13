# Generated by Django 4.1.7 on 2023-03-31 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistant',
            fields=[
                ('id_voice', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, null=True)),
                ('personality_promt', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthDesbloqueo',
            fields=[
                ('numero_autorizacion_desbloqueo', models.IntegerField(primary_key=True, serialize=False)),
                ('antecedentes', models.CharField(max_length=255, null=True)),
                ('materia', models.CharField(max_length=255, null=True)),
                ('adjuntos', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llamado', models.IntegerField(null=True)),
                ('linea_subsidio', models.CharField(max_length=255, null=True)),
                ('titulo', models.CharField(max_length=255, null=True)),
                ('tipo_autorizacion', models.CharField(max_length=255, null=True)),
                ('consolidada', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id_banco', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_banco', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('rut_beneficiario', models.IntegerField(primary_key=True, serialize=False)),
                ('dv_beneficiario', models.CharField(max_length=1, null=True)),
                ('nombre_beneficiario', models.CharField(max_length=255, null=True)),
                ('numero_cuenta', models.IntegerField(null=True)),
                ('numero_autorizacion', models.IntegerField(null=True)),
                ('cantidad_ahorro', models.IntegerField(null=True)),
                ('id_banco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.banco')),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id_certificado', models.IntegerField(primary_key=True, serialize=False)),
                ('certificado_nombre', models.CharField(max_length=255, null=True)),
                ('certificado_anio', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constructora',
            fields=[
                ('rut_constructora', models.IntegerField(primary_key=True, serialize=False)),
                ('dv_constructora', models.CharField(max_length=1, null=True)),
                ('nombre_constructora', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GiroAhorro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(max_length=255, null=True)),
                ('numero_resolucion', models.IntegerField(null=True)),
                ('fecha_resolucion', models.DateField(null=True)),
                ('fecha_emision_documento', models.DateField(null=True)),
                ('id_estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.estado')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('limite_creaciones', models.IntegerField(null=True)),
                ('limite_consulta_espacial', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=255, null=True)),
                ('siglas_proyecto', models.CharField(max_length=45, null=True)),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user')),
                ('numero_autorizacion_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.authpago')),
                ('rut_constructora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.constructora')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2000, null=True)),
                ('date', models.TimeField(null=True)),
                ('id_asistant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.asistant')),
                ('id_conversation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.conversation')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='GiroEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estado')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
                ('numero_autorizacion_giro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.giroahorro')),
            ],
        ),
        migrations.AddField(
            model_name='giroahorro',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='giroahorro',
            name='numero_autorizacion_pago',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.authpago'),
        ),
        migrations.CreateModel(
            name='Factoring',
            fields=[
                ('rut_factoring', models.IntegerField(primary_key=True, serialize=False)),
                ('dv_factoring', models.CharField(blank=True, max_length=1, null=True)),
                ('nombre_factoring', models.CharField(blank=True, max_length=255, null=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.CreateModel(
            name='DetallePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cheque', models.IntegerField(blank=True, null=True)),
                ('monto', models.FloatField(blank=True, null=True)),
                ('numero_autorizacion_pago', models.IntegerField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=255, null=True)),
                ('pertenece', models.BooleanField(blank=True, null=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
                ('rut_constructora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.constructora')),
                ('rut_factoring', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.factoring')),
            ],
        ),
        migrations.CreateModel(
            name='DesbloqueoEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estado')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
                ('numero_autorizacion_desbloqueo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.authdesbloqueo')),
            ],
        ),
        migrations.AddField(
            model_name='constructora',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user'),
        ),
        migrations.CreateModel(
            name='CertificadoProyecto',
            fields=[
                ('id_certificado_proyecto', models.IntegerField(primary_key=True, serialize=False)),
                ('id_certificado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.certificado')),
                ('id_proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='certificado',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='rut_beneficiario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.beneficiario'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user'),
        ),
        migrations.AddField(
            model_name='banco',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user'),
        ),
        migrations.AddField(
            model_name='authpago',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='authdesbloqueo',
            name='id_estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.estado'),
        ),
        migrations.AddField(
            model_name='authdesbloqueo',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user'),
        ),
        migrations.AddField(
            model_name='authdesbloqueo',
            name='numero_autorizacion_giro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.giroahorro'),
        ),
        migrations.AddField(
            model_name='authdesbloqueo',
            name='numero_autorizacion_pago',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.authpago'),
        ),
    ]
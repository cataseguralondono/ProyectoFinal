# Generated by Django 4.1.5 on 2023-03-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDirectorio', '0003_rename_fechacalificacion_comentario_fecha_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
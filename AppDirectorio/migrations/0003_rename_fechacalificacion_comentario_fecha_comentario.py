# Generated by Django 4.1.5 on 2023-03-10 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppDirectorio', '0002_comentario_delete_calificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='fechaCalificacion',
            new_name='fecha_comentario',
        ),
    ]
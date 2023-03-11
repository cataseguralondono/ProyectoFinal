# Generated by Django 4.1.5 on 2023-03-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDirectorio', '0004_alter_comentario_fecha_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='imagen_negocio',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]

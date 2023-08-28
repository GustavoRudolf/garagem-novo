# Generated by Django 4.2.4 on 2023-08-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0007_veiculo_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='imagem',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='imagem',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='+', to='uploader.image'),
        ),
    ]
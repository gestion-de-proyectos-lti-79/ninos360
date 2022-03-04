# Generated by Django 4.0.2 on 2022-03-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Jorge', max_length=100, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Lopez', max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ocupation',
            field=models.CharField(blank=True, choices=[('0', 'Administrador'), ('1', 'Padre'), ('2', 'NIño'), ('3', 'Padrino')], max_length=1),
        ),
    ]
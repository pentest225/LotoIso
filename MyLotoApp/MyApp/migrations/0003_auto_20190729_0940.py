# Generated by Django 2.2.3 on 2019-07-29 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20190729_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='math',
            name='idEquipe',
        ),
        migrations.RemoveField(
            model_name='math',
            name='id_equip1',
        ),
        migrations.RemoveField(
            model_name='math',
            name='id_equip2',
        ),
        migrations.AddField(
            model_name='math',
            name='idEquipe1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Equipe1', to='MyApp.Equipe'),
        ),
        migrations.AddField(
            model_name='math',
            name='idEquipe2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.Equipe', verbose_name='Equipe2'),
        ),
    ]

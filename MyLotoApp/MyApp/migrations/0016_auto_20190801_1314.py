# Generated by Django 2.2.3 on 2019-08-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0015_remove_equipe_idsport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='cote',
            field=models.FloatField(null=True),
        ),
    ]
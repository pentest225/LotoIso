# Generated by Django 2.2.3 on 2019-08-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0016_auto_20190801_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='parier',
            name='gainParie',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='parier',
            name='idVictoir',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0023_auto_20190802_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parier',
            name='gainParie',
            field=models.FloatField(null=True),
        ),
    ]

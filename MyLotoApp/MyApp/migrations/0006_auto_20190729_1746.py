# Generated by Django 2.2.3 on 2019-07-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_auto_20190729_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='logo',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

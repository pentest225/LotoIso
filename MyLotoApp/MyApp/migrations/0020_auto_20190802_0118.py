# Generated by Django 2.2.3 on 2019-08-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0019_auto_20190802_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='scoreEq1',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='math',
            name='scoreEq2',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
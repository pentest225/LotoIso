# Generated by Django 2.2.3 on 2019-07-30 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20190729_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sport',
            old_name='Nom',
            new_name='nom',
        ),
    ]
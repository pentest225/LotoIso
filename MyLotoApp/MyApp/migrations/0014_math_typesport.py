# Generated by Django 2.2.3 on 2019-07-31 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0013_auto_20190731_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='math',
            name='typeSport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='typeMath', to='MyApp.Sport'),
        ),
    ]

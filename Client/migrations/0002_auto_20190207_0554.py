# Generated by Django 2.0 on 2019-02-07 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_license_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='Agent.Agent'),
        ),
    ]

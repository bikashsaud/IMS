# Generated by Django 2.0 on 2019-02-04 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agent', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Form_number', models.IntegerField(unique=True)),
                ('Branch_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default=None, max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('Temporary_Address', models.CharField(max_length=200)),
                ('Permanent_address', models.CharField(max_length=200)),
                ('Contact_number', models.IntegerField()),
                ('Email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('Nationality', models.CharField(max_length=200)),
                ('Education_level', models.CharField(choices=[('see', 'SEE'), ('Bachelors', 'BACHELORS'), ('Master', 'MASTER')], default=None, max_length=200)),
                ('Citizenship', models.FileField(blank=True, default='No file uploaded', null=True, upload_to='uploads/')),
                ('Citizenship_number', models.IntegerField(unique=True)),
                ('Company_name', models.CharField(max_length=200)),
                ('Company_location', models.CharField(max_length=200)),
                ('Income_source', models.BigIntegerField()),
                ('Fathers_name', models.CharField(max_length=200)),
                ('Mothers_name', models.CharField(max_length=200)),
                ('Grandfathers_name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('client_license_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='Agent.Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

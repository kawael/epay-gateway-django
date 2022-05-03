# Generated by Django 3.2.7 on 2022-05-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoiceNumber', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('backUrl', models.CharField(max_length=200)),
                ('webhookUrl', models.CharField(max_length=200)),
                ('amount', models.FloatField(max_length=75)),
                ('discount', models.IntegerField(max_length=3)),
                ('mode', models.CharField(choices=[('CIB', 'CIB'), ('EDAHABIA', 'EDAHABIA')], default='EDAHABIA', max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chargily.client')),
            ],
        ),
    ]
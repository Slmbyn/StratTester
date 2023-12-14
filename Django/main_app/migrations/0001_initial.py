# Generated by Django 5.0 on 2023-12-14 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.CharField(choices=[('5', '5min ORB'), ('SR', 'S/R Break'), ('EC', '10/20 ema cross')], max_length=2)),
                ('ticker', models.CharField(max_length=4)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PL_percent', models.IntegerField()),
                ('PL_abs', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('entry_price', models.IntegerField()),
                ('exit_price', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.test')),
            ],
        ),
    ]

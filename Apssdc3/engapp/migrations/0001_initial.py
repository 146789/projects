# Generated by Django 3.0.8 on 2020-09-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collageaname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('roll', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
            ],
        ),
    ]

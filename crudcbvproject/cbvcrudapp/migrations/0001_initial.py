# Generated by Django 3.0.8 on 2020-09-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=80)),
                ('lastName', models.CharField(max_length=80)),
                ('Tscore', models.FloatField()),
            ],
        ),
    ]

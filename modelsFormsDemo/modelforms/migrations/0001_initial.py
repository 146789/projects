# Generated by Django 3.0.8 on 2020-09-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('assignedTo', models.CharField(max_length=50)),
                ('priroity', models.IntegerField()),
            ],
        ),
    ]

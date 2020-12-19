# Generated by Django 3.0.8 on 2020-09-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=40)),
                ('f_age', models.IntegerField()),
                ('f_empid', models.IntegerField()),
                ('f_phno', models.IntegerField()),
                ('f_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('roll', models.CharField(max_length=20)),
                ('phno', models.IntegerField()),
            ],
        ),
    ]
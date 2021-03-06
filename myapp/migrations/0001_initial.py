# Generated by Django 2.2.8 on 2020-01-08 03:01

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
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.2.8 on 2020-01-14 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200114_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='batch',
        ),
        migrations.AddField(
            model_name='student',
            name='batch_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.Batch'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerApp', '0009_auto_20201129_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

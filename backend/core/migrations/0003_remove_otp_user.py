# Generated by Django 5.1.3 on 2025-01-07 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='user',
        ),
    ]

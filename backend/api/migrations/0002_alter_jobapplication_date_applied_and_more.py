# Generated by Django 5.1.3 on 2024-11-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='date_applied',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryHello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

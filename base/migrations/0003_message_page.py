# Generated by Django 5.2 on 2025-05-08 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post'),
        ),
    ]

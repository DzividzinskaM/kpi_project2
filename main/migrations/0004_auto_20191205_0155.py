# Generated by Django 2.2.6 on 2019-12-04 23:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191204_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
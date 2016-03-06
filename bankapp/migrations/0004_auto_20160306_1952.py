# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_transaction_destination_account_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-transaction_time']},
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 6, 19, 52, 20, 402916, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

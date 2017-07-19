# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20170719_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='organisation',
            field=models.ForeignKey(blank=True, to='addresses.Organisation', on_delete=django.db.models.deletion.SET_NULL, help_text='Organisation Name', null=True),
        ),
    ]

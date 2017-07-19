# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(choices=[('Ms', 'Ms'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Mr', 'Mr'), ('Master', 'Master'), ('Mx', 'Mx')], help_text='Title', max_length=4, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(help_text='Address 1', max_length=100)),
                ('address_line2', models.CharField(max_length=100, help_text='Address 2', blank=True)),
                ('address_line3', models.CharField(max_length=100, help_text='Address 3', blank=True)),
                ('address_city', models.CharField(help_text='City', max_length=50)),
                ('address_county', models.CharField(help_text='County', max_length=50)),
                ('address_postcode', models.CharField(help_text='Postcode', max_length=10)),
                ('telephone', models.CharField(max_length=12, help_text='Telephone Number', blank=True)),
                ('email', models.EmailField(max_length=100, help_text='Email Address', blank=True)),
                ('org_name', models.CharField(help_text='Organisation Name', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(help_text='Address 1', max_length=100)),
                ('address_line2', models.CharField(max_length=100, help_text='Address 2', blank=True)),
                ('address_line3', models.CharField(max_length=100, help_text='Address 3', blank=True)),
                ('address_city', models.CharField(help_text='City', max_length=50)),
                ('address_county', models.CharField(help_text='County', max_length=50)),
                ('address_postcode', models.CharField(help_text='Postcode', max_length=10)),
                ('telephone', models.CharField(max_length=12, help_text='Telephone Number', blank=True)),
                ('email', models.EmailField(max_length=100, help_text='Email Address', blank=True)),
                ('title', models.CharField(choices=[('Ms', 'Ms'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Mr', 'Mr'), ('Master', 'Master'), ('Mx', 'Mx')], max_length=3, help_text='Title', blank=True)),
                ('firstname', models.CharField(help_text='First Name', max_length=50)),
                ('middlename', models.CharField(max_length=100, help_text='Middle Name(s)', blank=True)),
                ('surname', models.CharField(help_text='Surname', max_length=50)),
                ('organisation', models.ForeignKey(to='addresses.Organisation', help_text='Organisation Name')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

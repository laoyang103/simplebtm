# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bus_tag_1', models.CharField(default=b'', max_length=100)),
                ('bus_tag_2', models.CharField(default=b'', max_length=100)),
                ('bus_tag_3', models.CharField(default=b'', max_length=100)),
                ('bus_tag_4', models.CharField(default=b'', max_length=100)),
                ('bus_tag_5', models.CharField(default=b'', max_length=100)),
                ('bus_tag_6', models.CharField(default=b'', max_length=100)),
                ('bus_tag_7', models.CharField(default=b'', max_length=100)),
                ('bus_tag_8', models.CharField(default=b'', max_length=100)),
                ('bus_tag_9', models.CharField(default=b'', max_length=100)),
                ('bus_tag_10', models.CharField(default=b'', max_length=100)),
                ('bus_tag_11', models.CharField(default=b'', max_length=100)),
                ('bus_tag_12', models.CharField(default=b'', max_length=100)),
                ('bus_tag_13', models.CharField(default=b'', max_length=100)),
                ('bus_tag_14', models.CharField(default=b'', max_length=100)),
                ('bus_tag_15', models.CharField(default=b'', max_length=100)),
                ('bus_tag_16', models.CharField(default=b'', max_length=100)),
                ('bus_tag_17', models.CharField(default=b'', max_length=100)),
                ('bus_tag_18', models.CharField(default=b'', max_length=100)),
                ('bus_tag_19', models.CharField(default=b'', max_length=100)),
            ],
        ),
    ]

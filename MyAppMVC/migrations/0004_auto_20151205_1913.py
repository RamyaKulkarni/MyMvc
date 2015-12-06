# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAppMVC', '0003_auto_20151205_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.ImageField(blank=True, upload_to='images/heros'),
        ),
    ]

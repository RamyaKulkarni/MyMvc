# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAppMVC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.ImageField(upload_to=''),
        ),
    ]

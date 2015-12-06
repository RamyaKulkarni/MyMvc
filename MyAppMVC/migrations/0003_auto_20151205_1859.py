# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAppMVC', '0002_auto_20151203_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.ImageField(upload_to='/images/'),
        ),
    ]

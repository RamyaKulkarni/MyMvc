# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('hero_image', models.ImageField(upload_to='/images/')),
                ('category', models.CharField(max_length=50)),
                ('body_text', models.TextField()),
            ],
        ),
    ]

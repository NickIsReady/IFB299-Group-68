# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteMain', '0004_auto_20171028_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industry',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industry',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mall',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mall',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museum',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museum',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zoo',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zoo',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1.0, max_digits=9),
            preserve_default=False,
        ),
    ]
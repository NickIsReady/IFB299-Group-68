# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-31 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websiteMain', '0007_review_college'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review_hotel',
            old_name='library',
            new_name='hotel',
        ),
        migrations.RenameField(
            model_name='review_industry',
            old_name='library',
            new_name='industry',
        ),
        migrations.RenameField(
            model_name='review_mall',
            old_name='library',
            new_name='mall',
        ),
        migrations.RenameField(
            model_name='review_museum',
            old_name='library',
            new_name='museum',
        ),
        migrations.RenameField(
            model_name='review_park',
            old_name='library',
            new_name='park',
        ),
        migrations.RenameField(
            model_name='review_restaurant',
            old_name='library',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='review_zoo',
            old_name='library',
            new_name='zoo',
        ),
    ]

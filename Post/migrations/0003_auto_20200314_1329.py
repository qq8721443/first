# Generated by Django 3.0.4 on 2020-03-14 04:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20200308_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='context',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

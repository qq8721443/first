# Generated by Django 3.0.4 on 2020-03-14 04:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20200314_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='context',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
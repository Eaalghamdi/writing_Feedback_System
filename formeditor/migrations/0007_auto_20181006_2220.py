# Generated by Django 2.1.2 on 2018-10-06 22:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formeditor', '0006_auto_20181006_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

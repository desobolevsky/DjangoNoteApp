# Generated by Django 3.1 on 2020-09-05 08:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000),
        ),
    ]

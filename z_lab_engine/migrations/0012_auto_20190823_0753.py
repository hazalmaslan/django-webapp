# Generated by Django 2.2.4 on 2019-08-23 07:53

from django.db import migrations, models
import z_lab_engine.models


class Migration(migrations.Migration):

    dependencies = [
        ('z_lab_engine', '0011_remove_file_hashes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=z_lab_engine.models.get_upload_path),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-26 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('z_lab_engine', '0003_auto_20190725_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hash',
            old_name='update_tags',
            new_name='upload_tags',
        ),
    ]

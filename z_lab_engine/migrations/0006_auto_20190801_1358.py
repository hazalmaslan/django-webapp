# Generated by Django 2.2.3 on 2019-08-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_lab_engine', '0005_auto_20190730_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='hash',
            name='magic_header',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='hash',
            name='vt_score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
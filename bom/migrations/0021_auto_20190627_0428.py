# Generated by Django 2.2.2 on 2019-06-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bom', '0020_auto_20190627_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partrevision',
            name='attribute',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partrevision',
            name='value',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]

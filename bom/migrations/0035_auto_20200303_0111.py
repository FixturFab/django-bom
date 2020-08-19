# Generated by Django 2.2.9 on 2020-03-03 01:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bom', '0034_auto_20200222_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='number_class_code_len',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(2),
                                                                     django.core.validators.MaxValueValidator(16)]),
        ),
        migrations.AddField(
            model_name='organization',
            name='number_variation_len',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(0),
                                                                     django.core.validators.MaxValueValidator(16)]),
        ),
        migrations.AlterField(
            model_name='organization',
            name='number_item_len',
            field=models.PositiveIntegerField(default=4, validators=[django.core.validators.MinValueValidator(3),
                                                                     django.core.validators.MaxValueValidator(128)]),
        ),
        migrations.AlterField(
            model_name='partclass',
            name='code',
            field=models.CharField(max_length=16, validators=[
                django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]

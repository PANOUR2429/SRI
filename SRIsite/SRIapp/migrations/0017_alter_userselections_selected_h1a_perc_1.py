# Generated by Django 4.2.13 on 2024-08-06 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRIapp', '0016_rename_selected_c1a_perc_2_level_userselections_selected_c1a_perc2_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselections',
            name='selected_H1a_Perc_1',
            field=models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)]),
        ),
    ]
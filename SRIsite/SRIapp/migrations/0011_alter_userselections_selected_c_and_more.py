# Generated by Django 4.2.13 on 2024-07-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRIapp', '0010_alter_userselections_selected_c1a_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselections',
            name='selected_C',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DE',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DHW',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_EV',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_L',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V',
            field=models.BooleanField(default=True),
        ),
    ]

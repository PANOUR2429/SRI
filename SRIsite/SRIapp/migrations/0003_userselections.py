# Generated by Django 4.2.13 on 2024-06-01 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRIapp', '0002_alter_levels_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_building_type', models.CharField(max_length=200)),
                ('selected_zone', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-09 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRIapp', '0008_user_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DomainControl',
        ),
        migrations.DeleteModel(
            name='User_test',
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRIapp', '0005_test_s_h_test_s_h1a_l_userselections_selected_c_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testtype', models.CharField(max_length=200)),
            ],
        ),
    ]
# Generated by Django 4.2.13 on 2024-07-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRIapp', '0011_alter_userselections_selected_c_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselections',
            name='selected_C1a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C1b_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C1c_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C1d_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C1f_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C1g_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C2a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C2b_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C3_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_C4_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DE1_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DE2_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DE4_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DHW1a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DHW1b_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DHW1d_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DHW2b_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_DHW3_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E11_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E12_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E2_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E3_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E4_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E5_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_E8_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_EV15_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_EV16_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_EV17_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H1a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H1b_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H1c_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H1d_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H1f_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H2a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H2b_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H2d_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H3_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_H4_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_L1a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_L2_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC13_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC25_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC28_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC29_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC30_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC3_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC4_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_MC9_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V1a_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V1c_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V2c_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V2d_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V3_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_V6_level',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_building_type',
            field=models.CharField(choices=[('Residential', 'Residential'), ('Non - Residential', 'Non - Residential')], default='Residential', max_length=100),
        ),
        migrations.AlterField(
            model_name='userselections',
            name='selected_zone',
            field=models.CharField(choices=[('North Europe', 'North Europe'), ('West Europe', 'West Europe'), ('North-East Europe', 'North-East Europe'), ('South Europe', 'South Europe'), ('South-East Europe', 'South-East Europe')], default='South Europe', max_length=100),
        ),
    ]

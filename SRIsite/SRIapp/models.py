from django.db import models


# Create your models here.
class DomainWeight(models.Model):
    building_type = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    dw_cr1 = models.FloatField()
    dw_cr2 = models.FloatField()
    dw_cr3 = models.FloatField()
    dw_cr4 = models.FloatField()
    dw_cr5 = models.FloatField()
    dw_cr6 = models.FloatField()
    dw_cr7 = models.FloatField()


class ImpactWeight(models.Model):
    building_type = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    imp_cr1 = models.FloatField()
    imp_cr2 = models.FloatField()
    imp_cr3 = models.FloatField()
    imp_cr4 = models.FloatField()
    imp_cr5 = models.FloatField()
    imp_cr6 = models.FloatField()
    imp_cr7 = models.FloatField()


class Levels(models.Model):
    code = models.CharField(max_length=200)
    level_desc = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    score_cr1 = models.FloatField()
    score_cr2 = models.FloatField()
    score_cr3 = models.FloatField()
    score_cr4 = models.FloatField()
    score_cr5 = models.FloatField()
    score_cr6 = models.FloatField()
    score_cr7 = models.FloatField()
    level = models.FloatField()
    mandatory = models.FloatField()
    domain = models.CharField(max_length=200)


class Services(models.Model):
    domain = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    service_group = models.CharField(max_length=200)
    service_desc = models.CharField(max_length=200)

class UserSelections(models.Model):
    # possible building types: Residential, Non - Residential
    selected_building_type = models.CharField(max_length=200)
    # possible zones : North Europe, West Europe, North-East Europe, South Europe, South-East Europe
    selected_zone = models.CharField(max_length=200)
    # user selection for H (Heating
    selected_H = models.BooleanField(null=True)
    selected_H1a_level = models.PositiveIntegerField(null=True)  # max 4
    selected_H1b_level = models.PositiveIntegerField(null=True)  # max 3
    selected_H1c_level = models.PositiveIntegerField(null=True)  # max 2
    selected_H1d_level = models.PositiveIntegerField(null=True)  # max 4
    selected_H1f_level = models.PositiveIntegerField(null=True)  # max 3
    selected_H2a_level = models.PositiveIntegerField(null=True)  # max 2
    selected_H2b_level = models.PositiveIntegerField(null=True)  # max 3
    selected_H2d_level = models.PositiveIntegerField(null=True)  # max 4
    selected_H3_level = models.PositiveIntegerField(null=True)  # max 4
    selected_H4_level = models.PositiveIntegerField(null=True)   # max 4

    # user selection for DHW (Domestic Hot Water)
    selected_DHW = models.BooleanField(null=True)
    selected_DHW1a_level = models.PositiveIntegerField(null=True)  # max 3
    selected_DHW1b_level = models.PositiveIntegerField(null=True)  # max 3
    selected_DHW1d_level = models.PositiveIntegerField(null=True)  # max 3
    selected_DHW2b_level = models.PositiveIntegerField(null=True)  # max 4
    selected_DHW3_level = models.PositiveIntegerField(null=True)  # max 4
    # user selection for C (Cooling)
    selected_C = models.BooleanField(null=True)
    selected_C1a_level = models.PositiveIntegerField(null=True)  # max 4
    selected_C1b_level = models.PositiveIntegerField(null=True)  # max 3
    selected_C1c_level = models.PositiveIntegerField(null=True)  # max 2
    selected_C1d_level = models.PositiveIntegerField(null=True)  # max 4
    selected_C1f_level = models.PositiveIntegerField(null=True)  # max 2
    selected_C1g_level = models.PositiveIntegerField(null=True)  # max 3
    selected_C2a_level = models.PositiveIntegerField(null=True)  # max 3
    selected_C2b_level = models.PositiveIntegerField(null=True)  # max 4
    selected_C3_level = models.PositiveIntegerField(null=True)  # max 4
    selected_C4_level = models.PositiveIntegerField(null=True)  # max 4
    # user selection for V (Ventilation)
    selected_V = models.BooleanField(null=True)
    selected_V1a_level = models.PositiveIntegerField(null=True)  # max 4
    selected_V1c_level = models.PositiveIntegerField(null=True)  # max 4
    selected_V2c_level = models.PositiveIntegerField(null=True)  # max 2
    selected_V2d_level = models.PositiveIntegerField(null=True)  # max 3
    selected_V3_level = models.PositiveIntegerField(null=True)  # max 3
    selected_V6_level = models.PositiveIntegerField(null=True)  # max 3
    # user selection for L (Lighting)
    selected_L = models.BooleanField(null=True)
    selected_L1a_level = models.PositiveIntegerField(null=True)  # max 3
    selected_L2_level = models.PositiveIntegerField(null=True)  # max 4
    # user selection for DE (Dynamic Building Envelope)
    selected_DE = models.BooleanField(null=True)
    selected_DE1_level = models.PositiveIntegerField(null=True)  # max 4
    selected_DE2_level = models.PositiveIntegerField(null=True)  # max 3
    selected_DE4_level = models.PositiveIntegerField(null=True)  # max 4
    # user selection for E (Electricity)
    selected_E = models.BooleanField(null=True)
    selected_E2_level = models.PositiveIntegerField(null=True)  # max 4
    selected_E3_level = models.PositiveIntegerField(null=True)  # max 4
    selected_E4_level = models.PositiveIntegerField(null=True)  # max 3
    selected_E5_level = models.PositiveIntegerField(null=True)  # max 2
    selected_E8_level = models.PositiveIntegerField(null=True)  # max 3
    selected_E11_level = models.PositiveIntegerField(null=True)  # max 4
    selected_E12_level = models.PositiveIntegerField(null=True)  # max 4
    # user selection for EV (Electrical Vehicle Charging)
    selected_EV = models.BooleanField(null=True)
    selected_EV15_level = models.PositiveIntegerField(null=True)  # max 4
    selected_EV16_level = models.PositiveIntegerField(null=True)  # max 2
    selected_EV17_level = models.PositiveIntegerField(null=True)  # max 2
    # user selection for MC (Monitoring and Control)
    selected_MC = models.BooleanField(null=True)
    selected_MC3_level = models.PositiveIntegerField(null=True)  # max 3
    selected_MC4_level = models.PositiveIntegerField(null=True)  # max 3
    selected_MC9_level = models.PositiveIntegerField(null=True)  # max 2
    selected_MC13_level = models.PositiveIntegerField(null=True)  # max 3
    selected_MC25_level = models.PositiveIntegerField(null=True)  # max 2
    selected_MC28_level = models.PositiveIntegerField(null=True)  # max 2
    selected_MC29_level = models.PositiveIntegerField(null=True)  # max 4
    selected_MC30_level = models.PositiveIntegerField(null=True)  # max 3


class test(models.Model):
    s_type = models.CharField(max_length=200)
    s_zone = models.CharField(max_length=200)
    s_H = models.BooleanField(null=True)
    s_H1a_l = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.name




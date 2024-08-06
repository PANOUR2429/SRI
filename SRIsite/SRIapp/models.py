from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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


# possible building types: Residential, Non - Residential
building_type_choice = (('Residential','Residential'), ('Non - Residential','Non - Residential'))

# possible zones : North Europe, West Europe, North-East Europe, South Europe, South-East Europe
zones_choice = (
        ('North Europe','North Europe'),
        ('West Europe','West Europe'),
        ('North-East Europe','North-East Europe'),
        ('South Europe','South Europe'),
        ('South-East Europe','South-East Europe')
)

# user selection for H (Heating)
H_choice = (
        ('0','0'),
        ('1','1'),
)

H1a_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H1a_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H1b_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

H1b_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

H1c_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

H1c_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

H1d_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H1d_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H1f_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

H1f_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

H2a_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

H2a_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)


H2b_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

H2b_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

H2d_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H2d_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


H3_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H3_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


H4_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

H4_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


# user selection for DHW (Domestic Hot Water)
DHW_choice = (
        ('0','0'),
        ('1','1'),
)

DHW_choice2 = (
        ('0','0'),
        ('1','1'),
)

DHW1a_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

DHW1a_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


DHW1b_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

DHW1b_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


DHW1d_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

DHW1d_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


DHW2b_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

DHW2b_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


DHW3_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

DHW3_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


# user selection for C (Cooling)
C_choice = (
        ('0','0'),
        ('1','1'),
)

C_choice2 = (
        ('0','0'),
        ('1','1'),
)

C1a_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C1a_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C1b_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

C1b_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

C1c_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

C1c_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

C1d_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C1d_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


C1f_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

C1f_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)


C1g_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

C1g_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

C2a_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

C2a_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

C2b_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C2b_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C3_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C3_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C4_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

C4_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


# user selection for V (Ventilation)
V_choice = (
        ('0','0'),
        ('1','1'),
)

V_choice2 = (
        ('0','0'),
        ('1','1'),
)

V1a_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

V1a_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

V1c_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

V1c_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

V2c_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

V2c_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

V2d_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

V2d_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

V3_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

V3_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

V6_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

V6_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


# user selection for L (Lighting)
L_choice = (
        ('0','0'),
        ('1','1'),
)

L_choice2 = (
        ('0','0'),
        ('1','1'),
)

L1a_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

L1a_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

L2_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

L2_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


# user selection for DE (Dynamic Building Envelope)
DE_choice = (
        ('0','0'),
        ('1','1'),
)

DE_choice2 = (
        ('0','0'),
        ('1','1'),
)


DE1_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

DE1_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


DE2_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

DE2_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


DE4_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

DE4_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)



# user selection for E (Electricity)
E_choice = (
        ('0','0'),
        ('1','1'),
)

E_choice2 = (
        ('0','0'),
        ('1','1'),
)

E2_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

E2_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

E3_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

E3_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

E4_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

E4_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


E5_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

E5_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

E8_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

E8_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

E11_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

E11_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


E12_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

E12_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


# user selection for EV (Electrical Vehicle Charging)
EV_choice = (
        ('0','0'),
        ('1','1'),
)

EV_choice2 = (
        ('0','0'),
        ('1','1'),
)


EV15_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

EV15_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

EV16_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

EV16_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

EV17_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

EV17_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)


# user selection for MC (Monitoring and Control)
MC_choice = (
        ('0','0'),
        ('1','1'),
)

MC_choice2 = (
        ('0','0'),
        ('1','1'),
)

MC3_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

MC3_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

MC4_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

MC4_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

MC9_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

MC9_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

MC13_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


MC13_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


MC25_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

MC25_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

MC28_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)

MC28_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2')
)


MC29_choice  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)

MC29_choice2  = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
)


MC30_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)

MC30_choice2 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3')
)


class UserSelections(models.Model):
    # possible building types: Residential, Non - Residential
    selected_building_type = models.CharField(max_length=100, choices= building_type_choice, default='Residential')
    # possible zones : North Europe, West Europe, North-East Europe, South Europe, South-East Europe
    selected_zone = models.CharField(max_length=100, choices= zones_choice, default='South Europe')
    # user selection for H (Heating
    selected_H = models.BooleanField(default=True)
    selected_H1a = models.BooleanField(default=True)
    selected_H1b = models.BooleanField(default=True)
    selected_H1c = models.BooleanField(default=True)
    selected_H1d = models.BooleanField(default=True)
    selected_H1f = models.BooleanField(default=True)
    selected_H2a = models.BooleanField(default=True)
    selected_H2b = models.BooleanField(default=True)
    selected_H2d = models.BooleanField(default=True)
    selected_H3 = models.BooleanField(default=True)
    selected_H4 = models.BooleanField(default=True)
    selected_H1a_level = models.CharField(max_length=100, choices=H1a_choice, default='0')  # max 4
    selected_H1b_level = models.CharField(max_length=100, choices=H1b_choice, default='0')  # max 3
    selected_H1c_level = models.CharField(max_length=100, choices=H1c_choice, default='0')  # max 2
    selected_H1d_level = models.CharField(max_length=100, choices=H1d_choice, default='0')  # max 4
    selected_H1f_level = models.CharField(max_length=100, choices=H1f_choice, default='0')  # max 3
    selected_H2a_level = models.CharField(max_length=100, choices=H2a_choice, default='0')  # max 2
    selected_H2b_level = models.CharField(max_length=100, choices=H2b_choice, default='0')  # max 3
    selected_H2d_level = models.CharField(max_length=100, choices=H2d_choice, default='0')  # max 4
    selected_H3_level = models.CharField(max_length=100, choices=H3_choice, default='0')  # max 4
    selected_H4_level = models.CharField(max_length=100, choices=H4_choice, default='0')   # max 4
    selected_H1a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H1b_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H1c_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H1d_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H1f_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H2a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H2b_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H2d_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H3_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H4_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_H1a_Perc2_level = models.CharField(max_length=100, choices=H1a_choice2, default='0')  # max 4
    selected_H1b_Perc2_level = models.CharField(max_length=100, choices=H1b_choice2, default='0')  # max 3
    selected_H1c_Perc2_level = models.CharField(max_length=100, choices=H1c_choice2, default='0')  # max 2
    selected_H1d_Perc2_level = models.CharField(max_length=100, choices=H1d_choice2, default='0')  # max 4
    selected_H1f_Perc2_level = models.CharField(max_length=100, choices=H1f_choice2, default='0')  # max 3
    selected_H2a_Perc2_level = models.CharField(max_length=100, choices=H2a_choice2, default='0')  # max 2
    selected_H2b_Perc2_level = models.CharField(max_length=100, choices=H2b_choice2, default='0')  # max 3
    selected_H2d_Perc2_level = models.CharField(max_length=100, choices=H2d_choice2, default='0')  # max 4
    selected_H3_Perc2_level = models.CharField(max_length=100, choices=H3_choice2, default='0')  # max 4
    selected_H4_Perc2_level = models.CharField(max_length=100, choices=H4_choice2, default='0')   # max 4

    # user selection for DHW (Domestic Hot Water)
    selected_DHW = models.BooleanField(default=True)
    selected_DHW1a = models.BooleanField(default=True)
    selected_DHW1b = models.BooleanField(default=True)
    selected_DHW1d = models.BooleanField(default=True)
    selected_DHW2b = models.BooleanField(default=True)
    selected_DHW3 = models.BooleanField(default=True)
    selected_DHW1a_level = models.CharField(max_length=100, choices=DHW1a_choice, default='0')  # max 3
    selected_DHW1b_level = models.CharField(max_length=100, choices=DHW1b_choice, default='0')  # max 3
    selected_DHW1d_level = models.CharField(max_length=100, choices=DHW1d_choice, default='0')  # max 3
    selected_DHW2b_level = models.CharField(max_length=100, choices=DHW2b_choice, default='0')  # max 4
    selected_DHW3_level = models.CharField(max_length=100, choices=DHW3_choice, default='0')  # max 4
    selected_DHW1a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DHW1b_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DHW1d_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DHW2b_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DHW3_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DHW1a_Perc2_level = models.CharField(max_length=100, choices=DHW1a_choice2, default='0')  # max 3
    selected_DHW1b_Perc2_level = models.CharField(max_length=100, choices=DHW1b_choice2, default='0')  # max 3
    selected_DHW1d_Perc2_level = models.CharField(max_length=100, choices=DHW1d_choice2, default='0')  # max 3
    selected_DHW2b_Perc2_level = models.CharField(max_length=100, choices=DHW2b_choice2, default='0')  # max 4
    selected_DHW3_Perc2_level = models.CharField(max_length=100, choices=DHW3_choice2, default='0')  # max 4

    # user selection for C (Cooling)
    selected_C = models.BooleanField(default=True)
    selected_C1a = models.BooleanField(default=True)
    selected_C1b = models.BooleanField(default=True)
    selected_C1c = models.BooleanField(default=True)
    selected_C1d = models.BooleanField(default=True)
    selected_C1f = models.BooleanField(default=True)
    selected_C1g = models.BooleanField(default=True)
    selected_C2a = models.BooleanField(default=True)
    selected_C2b = models.BooleanField(default=True)
    selected_C3 = models.BooleanField(default=True)
    selected_C4 = models.BooleanField(default=True)
    selected_C1a_level = models.CharField(max_length=100, choices=C1a_choice, default='0')  # max 4
    selected_C1b_level = models.CharField(max_length=100, choices=C1b_choice, default='0')  # max 3
    selected_C1c_level = models.CharField(max_length=100, choices=C1c_choice, default='0')  # max 2
    selected_C1d_level = models.CharField(max_length=100, choices=C1d_choice, default='0')  # max 4
    selected_C1f_level = models.CharField(max_length=100, choices=C1f_choice, default='0')  # max 2
    selected_C1g_level = models.CharField(max_length=100, choices=C1g_choice, default='0')  # max 3
    selected_C2a_level = models.CharField(max_length=100, choices=C2a_choice, default='0')  # max 3
    selected_C2b_level = models.CharField(max_length=100, choices=C2b_choice, default='0')  # max 4
    selected_C3_level = models.CharField(max_length=100, choices=C3_choice, default='0')  # max 4
    selected_C4_level = models.CharField(max_length=100, choices=C4_choice, default='0')  # max 4
    selected_C1a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C1b_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C1c_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C1d_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C1f_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C1g_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C2a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C2b_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C3_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C4_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_C1a_Perc2_level = models.CharField(max_length=100, choices=C1a_choice2, default='0')  # max 4
    selected_C1b_Perc2_level = models.CharField(max_length=100, choices=C1b_choice2, default='0')  # max 3
    selected_C1c_Perc2_level = models.CharField(max_length=100, choices=C1c_choice2, default='0')  # max 2
    selected_C1d_Perc2_level = models.CharField(max_length=100, choices=C1d_choice2, default='0')  # max 4
    selected_C1f_Perc2_level = models.CharField(max_length=100, choices=C1f_choice2, default='0')  # max 2
    selected_C1g_Perc2_level = models.CharField(max_length=100, choices=C1g_choice2, default='0')  # max 3
    selected_C2a_Perc2_level = models.CharField(max_length=100, choices=C2a_choice2, default='0')  # max 3
    selected_C2b_Perc2_level = models.CharField(max_length=100, choices=C2b_choice2, default='0')  # max 4
    selected_C3_Perc2_level = models.CharField(max_length=100, choices=C3_choice2, default='0')  # max 4
    selected_C4_Perc2_level = models.CharField(max_length=100, choices=C4_choice2, default='0')  # max 4

    # user selection for V (Ventilation)
    selected_V = models.BooleanField(default=True)
    selected_V1a = models.BooleanField(default=True)
    selected_V1c = models.BooleanField(default=True)
    selected_V2c = models.BooleanField(default=True)
    selected_V2d = models.BooleanField(default=True)
    selected_V3 = models.BooleanField(default=True)
    selected_V6 = models.BooleanField(default=True)
    selected_V1a_level = models.CharField(max_length=100, choices=V1a_choice, default='0')  # max 4
    selected_V1c_level = models.CharField(max_length=100, choices=V1c_choice, default='0')  # max 4
    selected_V2c_level = models.CharField(max_length=100, choices=V2c_choice, default='0')  # max 2
    selected_V2d_level = models.CharField(max_length=100, choices=V2d_choice, default='0')  # max 3
    selected_V3_level = models.CharField(max_length=100, choices=V3_choice, default='0')  # max 3
    selected_V6_level = models.CharField(max_length=100, choices=V6_choice, default='0')  # max 3
    selected_V1a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_V1c_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_V2c_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_V2d_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_V3_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_V6_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_V1a_Perc2_level = models.CharField(max_length=100, choices=V1a_choice2, default='0')  # max 4
    selected_V1c_Perc2_level = models.CharField(max_length=100, choices=V1c_choice2, default='0')  # max 4
    selected_V2c_Perc2_level = models.CharField(max_length=100, choices=V2c_choice2, default='0')  # max 2
    selected_V2d_Perc2_level = models.CharField(max_length=100, choices=V2d_choice2, default='0')  # max 3
    selected_V3_Perc2_level = models.CharField(max_length=100, choices=V3_choice2, default='0')  # max 3
    selected_V6_Perc2_level = models.CharField(max_length=100, choices=V6_choice2, default='0')  # max 3

    # user selection for L (Lighting)
    selected_L = models.BooleanField(default=True)
    selected_L1a = models.BooleanField(default=True)
    selected_L2 = models.BooleanField(default=True)
    selected_L1a_level = models.CharField(max_length=100, choices=L1a_choice, default='0')  # max 3
    selected_L2_level = models.CharField(max_length=100, choices=L2_choice, default='0')  # max 4
    selected_L1a_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_L2_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_L1a_Perc2_level = models.CharField(max_length=100, choices=L1a_choice2, default='0')  # max 3
    selected_L2_Perc2_level = models.CharField(max_length=100, choices=L2_choice2, default='0')  # max 4

    # user selection for DE (Dynamic Building Envelope)
    selected_DE = models.BooleanField(default=True)
    selected_DE1 = models.BooleanField(default=True)
    selected_DE2 = models.BooleanField(default=True)
    selected_DE4 = models.BooleanField(default=True)
    selected_DE1_level = models.CharField(max_length=100, choices=DE1_choice, default='0')  # max 4
    selected_DE2_level = models.CharField(max_length=100, choices=DE2_choice, default='0')  # max 3
    selected_DE4_level = models.CharField(max_length=100, choices=DE4_choice, default='0')  # max 4
    selected_DE1_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DE2_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DE4_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_DE1_Perc2_level = models.CharField(max_length=100, choices=DE1_choice2, default='0')  # max 4
    selected_DE2_Perc2_level = models.CharField(max_length=100, choices=DE2_choice2, default='0')  # max 3
    selected_DE4_Perc2_level = models.CharField(max_length=100, choices=DE4_choice2, default='0')  # max 4

    # user selection for E (Electricity)
    selected_E = models.BooleanField(default=True)
    selected_E2 = models.BooleanField(default=True)
    selected_E3 = models.BooleanField(default=True)
    selected_E4 = models.BooleanField(default=True)
    selected_E5 = models.BooleanField(default=True)
    selected_E8 = models.BooleanField(default=True)
    selected_E11 = models.BooleanField(default=True)
    selected_E12 = models.BooleanField(default=True)
    selected_E2_level = models.CharField(max_length=100, choices=E2_choice, default='0')  # max 4
    selected_E3_level = models.CharField(max_length=100, choices=E3_choice, default='0')  # max 4
    selected_E4_level = models.CharField(max_length=100, choices=E4_choice, default='0')  # max 3
    selected_E5_level = models.CharField(max_length=100, choices=E5_choice, default='0')  # max 2
    selected_E8_level = models.CharField(max_length=100, choices=E8_choice, default='0')  # max 3
    selected_E11_level = models.CharField(max_length=100, choices=E11_choice, default='0')  # max 4
    selected_E12_level = models.CharField(max_length=100, choices=E12_choice, default='0')  # max 4
    selected_E2_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E3_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E4_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E5_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E8_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E11_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E12_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_E2_Perc2_level = models.CharField(max_length=100, choices=E2_choice2, default='0')  # max 4
    selected_E3_Perc2_level = models.CharField(max_length=100, choices=E3_choice2, default='0')  # max 4
    selected_E4_Perc2_level = models.CharField(max_length=100, choices=E4_choice2, default='0')  # max 3
    selected_E5_Perc2_level = models.CharField(max_length=100, choices=E5_choice2, default='0')  # max 2
    selected_E8_Perc2_level = models.CharField(max_length=100, choices=E8_choice2, default='0')  # max 3
    selected_E11_Perc2_level = models.CharField(max_length=100, choices=E11_choice2, default='0')  # max 4
    selected_E12_Perc2_level = models.CharField(max_length=100, choices=E12_choice2, default='0')  # max 4

    # user selection for EV (Electrical Vehicle Charging)
    selected_EV = models.BooleanField(default=True)
    selected_EV15 = models.BooleanField(default=True)
    selected_EV16 = models.BooleanField(default=True)
    selected_EV17 = models.BooleanField(default=True)
    selected_EV15_level = models.CharField(max_length=100, choices=EV15_choice, default='0')  # max 4
    selected_EV16_level = models.CharField(max_length=100, choices=EV16_choice, default='0')  # max 2
    selected_EV17_level = models.CharField(max_length=100, choices=EV17_choice, default='0')  # max 2
    selected_EV15_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_EV16_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_EV17_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_EV15_Perc2_level = models.CharField(max_length=100, choices=EV15_choice2, default='0')  # max 4
    selected_EV16_Perc2_level = models.CharField(max_length=100, choices=EV16_choice2, default='0')  # max 2
    selected_EV17_Perc2_level = models.CharField(max_length=100, choices=EV17_choice2, default='0')  # max 2

    # user selection for MC (Monitoring and Control)
    selected_MC = models.BooleanField(default=True)
    selected_MC3 = models.BooleanField(default=True)
    selected_MC4 = models.BooleanField(default=True)
    selected_MC9 = models.BooleanField(default=True)
    selected_MC13 = models.BooleanField(default=True)
    selected_MC25 = models.BooleanField(default=True)
    selected_MC28 = models.BooleanField(default=True)
    selected_MC29 = models.BooleanField(default=True)
    selected_MC30 = models.BooleanField(default=True)
    selected_MC3_level = models.CharField(max_length=100, choices=MC3_choice, default='0')  # max 3
    selected_MC4_level = models.CharField(max_length=100, choices=MC4_choice, default='0')  # max 3
    selected_MC9_level = models.CharField(max_length=100, choices=MC9_choice, default='0')  # max 2
    selected_MC13_level = models.CharField(max_length=100, choices=MC13_choice, default='0')  # max 3
    selected_MC25_level = models.CharField(max_length=100, choices=MC25_choice, default='0')  # max 2
    selected_MC28_level = models.CharField(max_length=100, choices=MC28_choice, default='0')  # max 2
    selected_MC29_level = models.CharField(max_length=100, choices=MC29_choice, default='0')  # max 4
    selected_MC30_level = models.CharField(max_length=100, choices=MC30_choice, default='0')  # max 3
    selected_MC3_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC4_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC9_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC13_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC25_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC28_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC29_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC30_Perc_1 = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    selected_MC3_Perc2_level = models.CharField(max_length=100, choices=MC3_choice2, default='0')  # max 3
    selected_MC4_Perc2_level = models.CharField(max_length=100, choices=MC4_choice2, default='0')  # max 3
    selected_MC9_Perc2_level = models.CharField(max_length=100, choices=MC9_choice2, default='0')  # max 2
    selected_MC13_Perc2_level = models.CharField(max_length=100, choices=MC13_choice2, default='0')  # max 3
    selected_MC25_Perc2_level = models.CharField(max_length=100, choices=MC25_choice2, default='0')  # max 2
    selected_MC28_Perc2_level = models.CharField(max_length=100, choices=MC28_choice2, default='0')  # max 2
    selected_MC29_Perc2_level = models.CharField(max_length=100, choices=MC29_choice2, default='0')  # max 4
    selected_MC30_Perc2_level = models.CharField(max_length=100, choices=MC30_choice2, default='0')  # max 3

class test(models.Model):
    s_type = models.CharField(max_length=200)
    s_zone = models.CharField(max_length=200)
    s_H = models.BooleanField(null=True)
    s_H1a_l = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.name




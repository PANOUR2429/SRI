from django import forms
from .models import *

# possible building types: Residential, Non - Residential
building_type_choice = (('selection1','Residential'), ('selection2','Non - Residential'))
class ControlForm(forms.ModelForm):
    class Meta:
        model = UserSelections
        fields = [
            'selected_building_type',
            'selected_zone',
            'selected_H',
            'selected_H1a_level', 'selected_H1b_level', 'selected_H1c_level',
            'selected_H1d_level', 'selected_H1f_level',
            'selected_H2a_level', 'selected_H2b_level',
            'selected_H2d_level', 'selected_H3_level', 'selected_H4_level',
            'selected_DHW',
            'selected_DHW1a_level', 'selected_DHW1b_level', 'selected_DHW1d_level',
            'selected_DHW2b_level', 'selected_DHW3_level',
            'selected_DHW',
            'selected_DHW1d_level', 'selected_DHW2b_level', 'selected_DHW3_level',
            'selected_C',
            'selected_C1a_level', 'selected_C1b_level', 'selected_C1c_level',
            'selected_C1d_level', 'selected_C1f_level',
            'selected_C1g_level', 'selected_C2a_level', 'selected_C2b_level', 'selected_C3_level',
            'selected_C4_level',
            'selected_V',
            'selected_V1a_level', 'selected_V1c_level', 'selected_V2c_level', 'selected_V2d_level',
            'selected_V3_level', 'selected_V6_level',
            'selected_L',
            'selected_L1a_level', 'selected_L2_level',
            'selected_DE',
            'selected_DE1_level', 'selected_DE2_level', 'selected_DE4_level',
            'selected_E',
            'selected_E2_level', 'selected_E3_level', 'selected_E4_level',
            'selected_E5_level', 'selected_E8_level',
            'selected_E11_level', 'selected_E12_level',
            'selected_EV',
            'selected_EV15_level', 'selected_EV16_level', 'selected_EV17_level',
            'selected_MC',
            'selected_MC3_level', 'selected_MC4_level', 'selected_MC9_level', 'selected_MC13_level',
            'selected_MC25_level', 'selected_MC28_level', 'selected_MC29_level', 'selected_MC30_level',
        ]

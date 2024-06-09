from django import forms
from .models import *

class ControlForm(forms.ModelForm):
    class Meta:
        model = UserSelections
        fields = [
            'selected_building_type', 'selected_zone',
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
        widgets = {
            'selected_building_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'building type', 'style': 'width: 300px;'}),
            'selected_zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zone', 'style': 'width: 300px;'}),
            'selected_H': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_H1a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H1b_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H1c_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H1d_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H1f_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H2a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H2b_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H2d_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H3_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_H4_level':  forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_DHW': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_DHW1a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_DHW1b_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_DHW1d_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),
            'selected_DHW2b_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_DHW3_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            # user selection for C (Cooling)
            'selected_C': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_C1a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_C1b_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_C1c_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_C1d_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_C1f_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_C1g_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_C2a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_C2b_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_C3_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_C4_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            # user selection for V (Ventilation)
            'selected_V': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_V1a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_V1c_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_V2c_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_V2d_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_V3_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_V6_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            # user selection for L (Lighting)
            'selected_L': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_L1a_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_L2_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            # user selection for DE (Dynamic Building Envelope)
            'selected_DE': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_DE1_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_DE2_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_DE4_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            # user selection for E (Electricity)
            'selected_E': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_E2_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_E3_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_E4_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_E5_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_E8_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_E11_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_E12_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            # user selection for EV (Electrical Vehicle Charging)
            'selected_EV': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_EV15_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_EV16_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_EV17_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            # user selection for MC (Monitoring and Control)
            'selected_MC': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'role': 'switch', 'id': 'flexSwitchCheck4'}),
            'selected_MC3_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_MC4_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_MC9_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_MC13_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
            'selected_MC25_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_MC28_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 2
            'selected_MC29_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 4
            'selected_MC30_level': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100px;'}),  # max 3
        }

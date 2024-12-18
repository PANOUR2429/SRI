from django import forms
from .models import *

# possible building types: Residential, Non - Residential
building_type_choice = (('selection1','Residential'), ('selection2','Non - Residential'))
class ControlForm(forms.ModelForm):

    selected_H = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H (Heating):"
    )

    selected_H1a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H1a (Heat emission control):"
    )

    selected_H1b = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H1b (Emission control for TABS (heating mode)):"
    )

    selected_H1c = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H1c (Control of distribution fluid temperature (supply or return air flow or water flow):"
    )

    selected_H1d = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H1d (Control of distribution pumps in networks):"
    )

    selected_H1f = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H1f (Thermal Energy Storage (TES) for building heating (excluding TABS)):"
    )

    selected_H2a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H2a (Heat generator control (all except heat pumps)):"
    )

    selected_H2b = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H2b (Heat generator control (for heat pumps)):"
    )

    selected_H2d = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H2d (Sequencing in case of different heat generators):"
    )

    selected_H3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H3 (Report information regarding heating system performance):"
    )

    selected_H4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="H4 (Flexibility and grid interaction):"
    )

    selected_DHW = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DHW (Domestic Hot Water):"
    )

    selected_DHW1a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DHW1a (Control of DHW storage charging (with direct electr. heating or integrated electr. heat pump)):"
    )

    selected_DHW1b = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DHW1b (Control of DHW storage charging (using hot water generation)):"
    )

    selected_DHW1d = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DHW1d (Control of DHW storage charging (with solar collector and supplymentary heat generation)):"
    )

    selected_DHW2b = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DHW2b (Sequencing in case of different DHW generators):"
    )

    selected_DHW3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DHW3 (Report information regarding domestic hot water performance):"
    )

    selected_C = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C (Cooling) :"
    )

    selected_C1a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C1a (Cooling emission control):"
    )

    selected_C1b = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C1b (Emission control for TABS (cooling mode)):"
    )

    selected_C1c = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C1c (Control of distribution network chilled water temperature (supply or return)):"
    )

    selected_C1f = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C1f (Interlock: avoiding simultaneous heating and cooling in the same room):"
    )

    selected_C1g = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C1g (Control of Thermal Energy Storage (TES) operation):"
    )

    selected_C2a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C2a (Generator control for cooling):"
    )

    selected_C2b = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C2b (Sequencing of different cooling generators):"
    )

    selected_C3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C3 (Report information regarding cooling system performance):"
    )

    selected_C4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="C4 (Flexibility and grid interaction):"
    )

    selected_V = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V (Ventilation)"
    )

    selected_V1a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V1a (Supply air flow control at the room level):"
    )

    selected_V1c = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V1c (Air flow or pressure control at the air handler level):"
    )

    selected_V2c = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V2c (Heat recovery control: prevention of overheating):"
    )

    selected_V2d = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V2d (Supply air temperature control at the air handling unit level): "
    )

    selected_V3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V3 (Free cooling with mechanical ventilation system):"
    )

    selected_V6 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="V6 (Reporting information regarding IAQ):"
    )

    selected_L = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="L (Lighting) :"
    )

    selected_L1a = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="L1a (Occupancy control for indoor lighting):"
    )
    selected_L2 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="L2 (Control artificial lighting power based on daylight levels):"
    )

    selected_DE = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DE (Dynamic Building Envelope) :"
    )

    selected_DE1 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DE1 (Window solar shading control):"
    )
    selected_DE2 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DE2 (Window open/closed control, combined ):"
    )
    selected_DE4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="DE4 (Reporting information regarding performance of dynamic building envelope systems):"
    )



    selected_E = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E (Electricity) :"
    )

    selected_E2 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E2 (Reporting information regarding local electricity generation):"
    )
    selected_E3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E3 (Storage of (locally generated) electricity):"
    )
    selected_E4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E4 (Optimizing self-consumption of locally generated electricity):"
    )
    selected_E5 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E5 (Control of combined heat and power plant (CHP)):"
    )
    selected_E8 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E8 (Support of (micro)grid operation modes):"
    )
    selected_E11 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E11 (Reporting information regarding energy storage):"
    )
    selected_E12 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="E12 (Reporting information regarding electricity consumption):"
    )


    selected_EV = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="EV (Electrical Vehicle Charging) :"
    )

    selected_EV15 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="EV15 (EV Charging Capacity):"
    )

    selected_EV16 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="EV16 (EV Charging Grid balancing):"
    )

    selected_EV17 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="EV17 (EV charging information and connectivity):"
    )

    selected_MC = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC (Monitoring and Control) :"
    )

    selected_MC3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC3 (Run time management of HVAC systems):"
    )

    selected_MC4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC4 (Detecting faults of technical building systems and providing support to the diagnosis of these faults):"
    )

    selected_MC9 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC9 (Occupancy detection: connected services):"
    )

    selected_MC13 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC13 (Central reporting of TBS performance and energy use):"
    )

    selected_MC25 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC25 (Smart Grid Integration):"
    )

    selected_MC28 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC28 (Reporting information regarding demand side management performance and operation):"
    )

    selected_MC29 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC29 (Override of DSM control):"
    )

    selected_MC30 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'switch'}),
        label="MC30 (Single platform for automated control & coordination between TBS + energy flow optimization based on occupancy, weather and grid):"
    )



    class Meta:
        model = UserSelections
        fields = [
            'selected_building_type',
            'selected_zone',
            'selected_H',
            'selected_H1a',
            'selected_H1a_Perc_1',
            'selected_H1a_level',
            'selected_H1a_Perc2_level',
            'selected_H1b',
            'selected_H1b_Perc_1',
            'selected_H1b_level',
            'selected_H1b_Perc2_level',
            'selected_H1c',
            'selected_H1c_Perc_1',
            'selected_H1c_level',
            'selected_H1c_Perc2_level',
            'selected_H1d',
            'selected_H1d_Perc_1',
            'selected_H1d_level',
            'selected_H1d_Perc2_level',
            'selected_H1f',
            'selected_H1f_Perc_1',
            'selected_H1f_level',
            'selected_H1f_Perc2_level',
            'selected_H2a',
            'selected_H2a_Perc_1',
            'selected_H2a_level',
            'selected_H2a_Perc2_level',
            'selected_H2b',
            'selected_H2b_Perc_1',
            'selected_H2b_level',
            'selected_H2b_Perc2_level',
            'selected_H2d',
            'selected_H2d_Perc_1',
            'selected_H2d_level',
            'selected_H2d_Perc2_level',
            'selected_H3',
            'selected_H3_Perc_1',
            'selected_H3_level',
            'selected_H3_Perc2_level',
            'selected_H4',
            'selected_H4_Perc_1',
            'selected_H4_level',
            'selected_H4_Perc2_level',
            'selected_DHW',
            'selected_DHW1a',
            'selected_DHW1a_Perc_1',
            'selected_DHW1a_level',
            'selected_DHW1a_Perc2_level',
            'selected_DHW1b',
            'selected_DHW1b_Perc_1',
            'selected_DHW1b_level',
            'selected_DHW1b_Perc2_level',
            'selected_DHW1d',
            'selected_DHW1d_Perc_1',
            'selected_DHW1d_level',
            'selected_DHW1d_Perc2_level',
            'selected_DHW2b',
            'selected_DHW2b_Perc_1',
            'selected_DHW2b_level',
            'selected_DHW2b_Perc2_level',
            'selected_DHW3',
            'selected_DHW3_Perc_1',
            'selected_DHW3_level',
            'selected_DHW3_Perc2_level',
            'selected_C',
            'selected_C1a',
            'selected_C1a_Perc_1',
            'selected_C1a_level',
            'selected_C1a_Perc2_level',
            'selected_C1b',
            'selected_C1b_Perc_1',
            'selected_C1b_level',
            'selected_C1b_Perc2_level',
            'selected_C1c',
            'selected_C1c_Perc_1',
            'selected_C1c_level',
            'selected_C1c_Perc2_level',
            'selected_C1d',
            'selected_C1d_Perc_1',
            'selected_C1d_level',
            'selected_C1d_Perc2_level',
            'selected_C1f',
            'selected_C1f_Perc_1',
            'selected_C1f_level',
            'selected_C1f_Perc2_level',
            'selected_C1g',
            'selected_C1g_Perc_1',
            'selected_C1g_level',
            'selected_C1g_Perc2_level',
            'selected_C2a',
            'selected_C2a_Perc_1',
            'selected_C2a_level',
            'selected_C2a_Perc2_level',
            'selected_C2b',
            'selected_C2b_Perc_1',
            'selected_C2b_level',
            'selected_C2b_Perc2_level',
            'selected_C3',
            'selected_C3_Perc_1',
            'selected_C3_level',
            'selected_C3_Perc2_level',
            'selected_C4',
            'selected_C4_Perc_1',
            'selected_C4_level',
            'selected_C4_Perc2_level',
            'selected_V',
            'selected_V1a',
            'selected_V1a_Perc_1',
            'selected_V1a_level',
            'selected_V1a_Perc2_level',
            'selected_V1c',
            'selected_V1c_Perc_1',
            'selected_V1c_level',
            'selected_V1c_Perc2_level',
            'selected_V2c',
            'selected_V2c_Perc_1',
            'selected_V2c_level',
            'selected_V2c_Perc2_level',
            'selected_V2d',
            'selected_V2d_Perc_1',
            'selected_V2d_level',
            'selected_V2d_Perc2_level',
            'selected_V3',
            'selected_V3_Perc_1',
            'selected_V3_level',
            'selected_V3_Perc2_level',
            'selected_V6',
            'selected_V6_Perc_1',
            'selected_V6_level',
            'selected_V6_Perc2_level',
            'selected_L',
            'selected_L1a',
            'selected_L1a_Perc_1',
            'selected_L1a_level',
            'selected_L1a_Perc2_level',
            'selected_L2',
            'selected_L2_Perc_1',
            'selected_L2_level',
            'selected_L2_Perc2_level',
            'selected_DE',
            'selected_DE1',
            'selected_DE1_Perc_1',
            'selected_DE1_level',
            'selected_DE1_Perc2_level',
            'selected_DE2',
            'selected_DE2_Perc_1',
            'selected_DE2_level',
            'selected_DE2_Perc2_level',
            'selected_DE4',
            'selected_DE4_Perc_1',
            'selected_DE4_level',
            'selected_DE4_Perc2_level',
            'selected_E',
            'selected_E2',
            'selected_E2_Perc_1',
            'selected_E2_level',
            'selected_E2_Perc2_level',
            'selected_E3',
            'selected_E3_Perc_1',
            'selected_E3_level',
            'selected_E3_Perc2_level',
            'selected_E4',
            'selected_E4_Perc_1',
            'selected_E4_level',
            'selected_E4_Perc2_level',
            'selected_E5',
            'selected_E5_Perc_1',
            'selected_E5_level',
            'selected_E5_Perc2_level',
            'selected_E8',
            'selected_E8_Perc_1',
            'selected_E8_level',
            'selected_E8_Perc2_level',
            'selected_E11',
            'selected_E11_Perc_1',
            'selected_E11_level',
            'selected_E11_Perc2_level',
            'selected_E12',
            'selected_E12_Perc_1',
            'selected_E12_level',
            'selected_E12_Perc2_level',
            'selected_EV',
            'selected_EV15',
            'selected_EV15_Perc_1',
            'selected_EV15_level',
            'selected_EV15_Perc2_level',
            'selected_EV16',
            'selected_EV16_Perc_1',
            'selected_EV16_level',
            'selected_EV16_Perc2_level',
            'selected_EV17',
            'selected_EV17_Perc_1',
            'selected_EV17_level',
            'selected_EV17_Perc2_level',
            'selected_MC',
            'selected_MC3',
            'selected_MC3_Perc_1',
            'selected_MC3_level',
            'selected_MC3_Perc2_level',
            'selected_MC4',
            'selected_MC4_Perc_1',
            'selected_MC4_level',
            'selected_MC4_Perc2_level',
            'selected_MC9',
            'selected_MC9_Perc_1',
            'selected_MC9_level',
            'selected_MC9_Perc2_level',
            'selected_MC13',
            'selected_MC13_Perc_1',
            'selected_MC13_level',
            'selected_MC13_Perc2_level',
            'selected_MC25',
            'selected_MC25_Perc_1',
            'selected_MC25_level',
            'selected_MC25_Perc2_level',
            'selected_MC28',
            'selected_MC28_Perc_1',
            'selected_MC28_level',
            'selected_MC28_Perc2_level',
            'selected_MC29',
            'selected_MC29_Perc_1',
            'selected_MC29_level',
            'selected_MC29_Perc2_level',
            'selected_MC30',
            'selected_MC30_Perc_1',
            'selected_MC30_level',
            'selected_MC30_Perc2_level',

        ]





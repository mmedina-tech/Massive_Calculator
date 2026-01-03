#!/usr/bin/env python3
#
# Resistive_Inductive_Capacitive_Parallel.py
#
# Python implementation of the resistive/inductive/capacitive formula set.
#

from .FormulaBase import *

class Resistive_Inductive_Capacitive_Parallel(FormulaBase):
    def __init__(self, name):
        super(Resistive_Inductive_Capacitive_Parallel, self).__init__(name)
        self.name = name
        self.error_msg = "Can not be a negative square root"
        self.PI = pi

        self.function_strings = {
            1 : "Impedance using Resistance, Inductive Reactance, and Capacitive Reactance",
            2 : "Volt Amps using Total Volts and Total Amps",
            3 : "Impedance using Total Volt and Total Amps",
            4 : "Volt Amps using Total Amps and Impedance",
            5 : "Total Volts using Total Amps and Impedance",
            6 : "Impedance using Total Volts and Volt Amps",
            7 : "Volt Amps using Total Volts and Impedance",
            8 : "Total Volts using Volt Amps and Total Amps",
            9 : "Impedance using Volt Amps and Total Amps",
            10 : "Volt Amps using Inductive Reactance, Capacitive Reactance, and Watts",
            11 : "Total Volts using Volt Amps and Impedance",
            12 : "Impedance using Resistance and Power Factor",
            13 : "Volt Amps using Watts and Power Factor",
            14 : "Total Amps using Resistor Amps, Inductor Amps, and Capacitor Amps",
            15 : "Power Factor using Impedance and Resistance",
            16 : "Inductor Volts using Inductor Amps and Inductive Reactance",
            17 : "Total Amps using Total Volts and Impedance",
            18 : "Power Factor using Watts and Volt Amps",
            19 : "Inductor Volts using Inductor VARs and Inductor Amps",
            20 : "Total Amps using Volt Amps and Total Volts",
            21 : "Power Factor using Resistor Amps and Total Amps",
            22 : "Inductor Volts using Inductor VARs and Inductive Reactance",
            23 : "Total Amps using Volt Amps and Impedance",
            24 : "Power Factor using CoSine and Theta Angle",
            25 : "Total Amps using Resistor Amps and Power Factor",
            26 : "Inductor Amps using Inductor Volts and Inductive Reactance",
            27 : "Inductor Amps using Inductor VARs and Inductor Volts",
            28 : "Indcutor Amps using Inductor VARs and Inductive Reactance",
            29 : "Inductor VARs using Inductor Volts and Inductive Reactance",
            30 : "Inductor VARs using Inductor Amps and Inductive Reactance",
            31 : "Inductor VARs using Inductor Volts and Inductor Amps",
            32 : "Capacitor VARs using Capacitor Volts and Capacitive Reactance",
            33 : "Capacitor VARs using Capacitor Amps and Capacitive Reactance",
            34 : "Capacitor VARs using Capacitor Volts and Capacitor Amps",
            35 : "Inductive Reactance using Inductor Volts and Inductor Amps",
            36 : "Resistor Volts using Resistor Amps and Resistance",
            37 : "Resistor Amps using Total Amps, Inductor Amps, and Capcitor Amps",
            38 : "Inductive Reactance using Frequency and Inductor Rating",
            39 : "Resistor Volts using Watts and Resistance",
            40 : "Resistor Amps using Resistor Volts and Resistance",
            41 : "Inductive Reactance using Inductor Volts and Inductor VARs",
            42 : "Resistor Volts using Watts and Resistor Amps",
            43 : "Resistor Amps using Watts and Resistor Volts",
            44 : "Inductive Reactance using Inductor VARs and Inductor Amps",
            45 : "Resistance using Resistor Volts and Resistor Amps",
            46 : "Resistor Amps using Watts and Resistance",
            47 : "Watts using Volt Amps, Inductor VARs, and Capacitor VARs",
            48 : "Resistor Amps using Total Amps and Power Factor",
            49 : "Resistance using Watts and Resistor Amps",
            50 : "Watts using Volt Amps and Power Factor",
            51 : "Capacitor Volts using Capacitor VARs and Capacitor Amps",
            52 : "Resistance using Impedance and Power Factor",
            53 : "Watts using Resistor Volts and Resistor Amps",
            54 : "Capacitor Volts using Capacitor Amps and Capacitive Reactance",
            55 : "Resistance using Resistor Volts and Watts",
            56 : "Watts using Resistor Volts and Resistance",
            57 : "Capacitor Volts using Capacitor VARs and Capacitive Reactance",
            58 : "Resistance using Impedance, Inductive Reactance, and Capacitive Reactance",
            59 : "Watts using Resistor Amps using Resistance",
            60 : "Inductor Rating using Inductive Reactance and Frequency",
            61 : "Capacitor Amps using Capacitor VARs and Capacitive Reactance",
            62 : "Capacitor Amps using Capacitor VARs and Capacitor Volts",
            63 : "Capacitive Reactance using Capacitor VARs and Capacitor Amps",
            64 : "Capacitive Reactance using Capacitor Volts and Capacitor Amps",
            65 : "Capacitive Reactance using Capacitor Volts and Capacitor VARs",
            66 : "Capacitor Rating using Frequency and Capacitive Reactance",
        }

        self.function_list = OrderedDict([
            (self.function_strings[1], self.form_1),
            (self.function_strings[2], self.form_2),
            (self.function_strings[3], self.form_3),
            (self.function_strings[4], self.form_4),
            (self.function_strings[5], self.form_5),
            (self.function_strings[6], self.form_6),
            (self.function_strings[7], self.form_7),
            (self.function_strings[8], self.form_8),
            (self.function_strings[9], self.form_9),
            (self.function_strings[10], self.form_10),
            (self.function_strings[11], self.form_11),
            (self.function_strings[12], self.form_12),
            (self.function_strings[13], self.form_13),
            (self.function_strings[14], self.form_14),
            (self.function_strings[15], self.form_15),
            (self.function_strings[16], self.form_16),
            (self.function_strings[17], self.form_17),
            (self.function_strings[18], self.form_18),
            (self.function_strings[19], self.form_19),
            (self.function_strings[20], self.form_20),
            (self.function_strings[21], self.form_21),
            (self.function_strings[22], self.form_22),
            (self.function_strings[23], self.form_23),
            (self.function_strings[24], self.form_24),
            (self.function_strings[25], self.form_25),
            (self.function_strings[26], self.form_26),
            (self.function_strings[27], self.form_27),
            (self.function_strings[28], self.form_28),
            (self.function_strings[29], self.form_29),
            (self.function_strings[30], self.form_30),
            (self.function_strings[31], self.form_31),
            (self.function_strings[32], self.form_32),
            (self.function_strings[33], self.form_33),
            (self.function_strings[34], self.form_34),
            (self.function_strings[35], self.form_35),
            (self.function_strings[36], self.form_36),
            (self.function_strings[37], self.form_37),
            (self.function_strings[38], self.form_38),
            (self.function_strings[39], self.form_39),
            (self.function_strings[40], self.form_40),
            (self.function_strings[41], self.form_41),
            (self.function_strings[42], self.form_42),
            (self.function_strings[43], self.form_43),
            (self.function_strings[44], self.form_44),
            (self.function_strings[45], self.form_45),
            (self.function_strings[46], self.form_46),
            (self.function_strings[47], self.form_47),
            (self.function_strings[48], self.form_48),
            (self.function_strings[49], self.form_49),
            (self.function_strings[50], self.form_50),
            (self.function_strings[51], self.form_51),
            (self.function_strings[52], self.form_52),
            (self.function_strings[53], self.form_53),
            (self.function_strings[54], self.form_54),
            (self.function_strings[55], self.form_55),
            (self.function_strings[56], self.form_56),
            (self.function_strings[57], self.form_57),
            (self.function_strings[58], self.form_58),
            (self.function_strings[59], self.form_59),
            (self.function_strings[60], self.form_60),
            (self.function_strings[61], self.form_61),
            (self.function_strings[62], self.form_62),
            (self.function_strings[63], self.form_63),
            (self.function_strings[64], self.form_64),
            (self.function_strings[65], self.form_65),
            (self.function_strings[66], self.form_66),
        ])

        self.functionInputs = {
            self.function_strings[1]: OrderedDict([
                ("number_input", "Resistance (input): "),
                ("number_input2", "Inductive Reactance (input): "),
                ("number_input3", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[2]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[3]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[4]: OrderedDict([
                ("number_input", "Total Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[5]: OrderedDict([
                ("number_input", "Total Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[6]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Volt Amps (input): "),
            ]),
            self.function_strings[7]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[8]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[9]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[10]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Capacitor VARs (input): "),
                ("number_input3", "Watts (input): "),
            ]),
            self.function_strings[11]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[12]: OrderedDict([
                ("number_input", "Resistance (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[13]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[14]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Inductor Amps (input): "),
                ("number_input3", "Capacitor Amps (input): "),
            ]),
            self.function_strings[15]: OrderedDict([
                ("number_input", "Impedance (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[16]: OrderedDict([
                ("number_input", "Inductor Amps (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[17]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[18]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Volt Amps (input): "),
            ]),
            self.function_strings[19]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[20]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Total Volts (input): "),
            ]),
            self.function_strings[21]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[22]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[23]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[24]: OrderedDict([
                ("number_input", "Theta Angle (input): "),
            ]),
            self.function_strings[25]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[26]: OrderedDict([
                ("number_input", "Indcutor Volts (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[27]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Inductor Volts (input): "),
            ]),
            self.function_strings[28]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[29]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[30]: OrderedDict([
                ("number_input", "Inductor Amps (input): "),
                ("number_input2", "Indcutive Reactance (input): "),
            ]),
            self.function_strings[31]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[32]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[33]: OrderedDict([
                ("number_input", "Capacitor Amps (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[34]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[35]: OrderedDict([
                ("number_input", "Indcutor Volts (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[36]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[37]: OrderedDict([
                ("number_input", "Total Amps (input): "),
                ("number_input2", "Inductor Amps (input): "),
                ("number_input3", "Capacitor Amps (input): "),
            ]),
            self.function_strings[38]: OrderedDict([
                ("number_input", "Frequency (input): "),
                ("number_input2", "Inductor Rating (input): "),
            ]),
            self.function_strings[39]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[40]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[41]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductor VARs (input): "),
            ]),
            self.function_strings[42]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[43]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resisitor Volts (input): "),
            ]),
            self.function_strings[44]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[45]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[46]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[47]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Inductor VARs (input): "),
                ("number_input3", "Capacitor VARs (input): "),
            ]),
            self.function_strings[48]: OrderedDict([
                ("number_input", "Total Amps (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[49]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[50]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[51]: OrderedDict([
                ("number_input", "Capcitor VARs (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[52]: OrderedDict([
                ("number_input", "Impedance (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[53]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[54]: OrderedDict([
                ("number_input", "Capacitor Amps (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[55]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Watts (input): "),
            ]),
            self.function_strings[56]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[57]: OrderedDict([
                ("number_input", "Inductor VARs (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[58]: OrderedDict([
                ("number_input", "Impedance (input): "),
                ("number_input2", "Inductive Reactance (input): "),
                ("number_input3", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[59]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[60]: OrderedDict([
                ("number_input", "Inductive Reactance (input): "),
                ("number_input2", "Frequency (input): "),
            ]),
            self.function_strings[61]: OrderedDict([
                ("number_input", "Capacitor VARs (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[62]: OrderedDict([
                ("number_input", "Capacitor VARs (input): "),
                ("number_input2", "Capacitor Volts (input): "),
            ]),
            self.function_strings[63]: OrderedDict([
                ("number_input", "Capacitor VARs (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[64]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[65]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitor VARs (input): "),
            ]),
            self.function_strings[66]: OrderedDict([
                ("number_input", "Frequency (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
        }

        self.formula_list = {
            self.function_strings[1]: {"Formula:<br>" : "sqrt((1 / R)<sup>2</sup> + (1 / X<sub>L</sub> - 1 / X<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[2]: {"Formula:<br>" : "E<sub>T</sub> * I<sub>T</sub>"},
            self.function_strings[3]: {"Formula:<br>" : "E<sub>T</sub> / I<sub>T</sub>"},
            self.function_strings[4]: {"Formula:<br>" : "I<sup>2</sup><sub>T</sub> * Z"},
            self.function_strings[5]: {"Formula:<br>" : "I<sub>T</sub> * Z"},
            self.function_strings[6]: {"Formula:<br>" : "E<sup>2</sup><sub>T</sub> / VA"},
            self.function_strings[7]: {"Formula:<br>" : "E<sup>2</sup><sub>T</sub> / Z"},
            self.function_strings[8]: {"Formula:<br>" : "VA / I<sub>T</sub>"},
            self.function_strings[9]: {"Formula:<br>" : "VA / I<sup>2</sup><sub>T</sub>"},
            self.function_strings[10]: {"Formula:<br>" : "sqrt( (VARs<sub>L</sub> - VARs<sub>C</sub>)<sup>2</sup> + P<sup>2</sup>)"},
            self.function_strings[11]: {"Formula:<br>" : "sqrt( VA + Z )"},
            self.function_strings[12]: {"Formula:<br>" : "R * PF"},
            self.function_strings[13]: {"Formula:<br>" : "P / PF"},
            self.function_strings[14]: {"Formula:<br>" : "sqrt( I<sub>R</sub><sup>2</sup> + (I<sub>L</sub> - I<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[15]: {"Formula:<br>" : "Z / R"},
            self.function_strings[16]: {"Formula:<br>" : "I<sub>L</sub> * X<sub>L</sub>"},
            self.function_strings[17]: {"Formula:<br>" : "E<sub>T</sub> / Z"},
            self.function_strings[18]: {"Formula:<br>" : "P / VA"},
            self.function_strings[19]: {"Formula:<br>" : "VARs<sub>L</sub> / I<sub>L</sub>"},
            self.function_strings[20]: {"Formula:<br>" : "VA / E<sub>T</sub>"},
            self.function_strings[21]: {"Formula:<br>" : "I<sub>R</sub> / I<sub>T</sub>"},
            self.function_strings[22]: {"Formula:<br>" : "sqrt( VARs<sub>L</sub> * X<sub>L</sub> )"},
            self.function_strings[23]: {"Formula:<br>" : "sqrt( VA / Z )"},
            self.function_strings[24]: {"Formula:<br>" : "cos(Angle Theta)"},
            self.function_strings[25]: {"Formula:<br>" : "I<sub>R</sub> / PF"},
            self.function_strings[26]: {"Formula:<br>" : "E<sub>L</sub> / X<sub>L</sub>"},
            self.function_strings[27]: {"Formula:<br>" : "VARs<sub>L</sub> / E<sub>L</sub>"},
            self.function_strings[28]: {"Formula:<br>" : "sqrt( VARs<sub>L</sub> / X<sub>L</sub> )"},
            self.function_strings[29]: {"Formula:<br>" : "E<sub>L</sub><sup>2</sup> / X<sub>L</sub>"},
            self.function_strings[30]: {"Formula:<br>" : "I<sub>L</sub><sup>2</sup> * X<sub>L</sub>"},
            self.function_strings[31]: {"Formula:<br>" : "E<sub>L</sub> * I<sub>L</sub>"},
            self.function_strings[32]: {"Formula:<br>" : "E<sub>C</sub><sup>2</sup> / X<sub>C</sub>"},
            self.function_strings[33]: {"Formula:<br>" : "I<sub>C</sub><sup>2</sup> * X<sub>C</sub>"},
            self.function_strings[34]: {"Formula:<br>" : "E<sub>C</sub> * I<sub>C</sub>"},
            self.function_strings[35]: {"Formula:<br>" : "E<sub>L</sub> / I<sub>L</sub>"},
            self.function_strings[36]: {"Formula:<br>" : "I<sub>R</sub> * R"},
            self.function_strings[37]: {"Formula:<br>" : "sqrt( I<sub>T</sub><sup>2</sup> - (I<sub>L</sub> - I<sub>C</sub>)<sup>2</sup> )"},
            self.function_strings[38]: {"Formula:<br>" : "2 * PI * f * L"},
            self.function_strings[39]: {"Formula:<br>" : "sqrt( P * R )"},
            self.function_strings[40]: {"Formula:<br>" : "E<sub>R</sub> / R"},
            self.function_strings[41]: {"Formula:<br>" : "E<sub>L</sub><sup>2</sup> / VARs<sub>L</sub>"},
            self.function_strings[42]: {"Formula:<br>" : "P / I<sub>R</sub>"},
            self.function_strings[43]: {"Formula:<br>" : "P / E<sub>R</sub>"},
            self.function_strings[44]: {"Formula:<br>" : "VARs<sub>L</sub> / I<sub>L</sub><sup>2</sup>"},
            self.function_strings[45]: {"Formula:<br>" : "E<sub>R</sub> / I<sub>R</sub>"},
            self.function_strings[46]: {"Formula:<br>" : "sqrt( P / R )"},
            self.function_strings[47]: {"Formula:<br>" : "sqrt( VA<sup>2</sup> - (VARs<sub>L</sub> - VARs<sub>C</sub>)<sup>2</sup> )"},
            self.function_strings[48]: {"Formula:<br>" : "I<sub>T</sub> * PF"},
            self.function_strings[49]: {"Formula:<br>" : "P / I<sub>R</sub><sup>2</sup>"},
            self.function_strings[50]: {"Formula:<br>" : "VA * PF"},
            self.function_strings[51]: {"Formula:<br>" : "VARs<sub>C</sub> / I<sub>C</sub>"},
            self.function_strings[52]: {"Formula:<br>" : "Z / PF"},
            self.function_strings[53]: {"Formula:<br>" : "E<sub>R</sub> * I<sub>R</sub>"},
            self.function_strings[54]: {"Formula:<br>" : "I<sub>C</sub> * X<sub>C</sub>"},
            self.function_strings[55]: {"Formula:<br>" : "E<sub>R</sub><sup>2</sup> / P"},
            self.function_strings[56]: {"Formula:<br>" : "E<sub>R</sub><sup>2</sup> / R"},
            self.function_strings[57]: {"Formula:<br>" : "sqrt( VARs<sub>C</sub> * X<sub>C</sub> )"},
            self.function_strings[58]: {"Formula:<br>" : "sqrt( (1 / Z)<sup>2</sup> - ( 1 / X<sub>L</sub> - 1 / X<sub>C</sub> )<sup>2</sup> )"},
            self.function_strings[59]: {"Formula:<br>" : "I<sub>R</sub><sup>2</sup> * R"},
            self.function_strings[60]: {"Formula:<br>" : "X<sub>L</sub> / (2 * PI * f)"},
            self.function_strings[61]: {"Formula:<br>" : "sqrt( VARs<sub>C</sub> / X<sub>C</sub> )"},
            self.function_strings[62]: {"Formula:<br>" : "VARs<sub>C</sub> / E<sub>C</sub>"},
            self.function_strings[63]: {"Formula:<br>" : "VARs<sub>C</sub> / I<sub>C</sub><sup>2</sup>"},
            self.function_strings[64]: {"Formula:<br>" : "E<sub>C</sub> / I<sub>C</sub>"},
            self.function_strings[65]: {"Formula:<br>" : "E<sub>C</sub><sup>2</sup> / VARs<sub>C</sub>"},
            self.function_strings[66]: {"Formula:<br>" : "1 / (2 * PI * f * X<sub>C</sub>)"},
        }

    def _prompt_inputs(self, title):
        args_out = [title] + list(self.functionInputs[title].values())
        return self.prompt(args_out)

    def form_1(self):
        title = self.function_strings[1]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = (pow(1/num,2)) + (pow((1/num2) - (1/num3),2))
        if  result <= 0 :
            return (self.error_msg, '')
        result = 1/(sqrt(result))
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_2(self):
        title = self.function_strings[2]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_3(self):
        title = self.function_strings[3]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_4(self):
        title = self.function_strings[4]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_5(self):
        title = self.function_strings[5]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_6(self):
        title = self.function_strings[6]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_7(self):
        title = self.function_strings[7]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_8(self):
        title = self.function_strings[8]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_9(self):
        title = self.function_strings[9]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2,2)
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_10(self):
        title = self.function_strings[10]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = (pow(num - num2, 2)) + (pow(num3,2))
        if  result <= 0 :
            return (self.error_msg, '')
        result = sqrt(result)
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_11(self):
        title = self.function_strings[11]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2)
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_12(self):
        title = self.function_strings[12]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_13(self):
        title = self.function_strings[13]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_14(self):
        title = self.function_strings[14]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = (pow(num,2)) + (pow(num2 - num3,2))
        if  result <= 0 :
            return (self.error_msg, '')
        result =  sqrt( result )
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_15(self):
        title = self.function_strings[15]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_16(self):
        title = self.function_strings[16]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_17(self):
        title = self.function_strings[17]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_18(self):
        title = self.function_strings[18]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_19(self):
        title = self.function_strings[19]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_20(self):
        title = self.function_strings[20]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_21(self):
        title = self.function_strings[21]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_22(self):
        title = self.function_strings[22]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_23(self):
        title = self.function_strings[23]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_24(self):
        title = self.function_strings[24]
        args = self._prompt_inputs(title)
        num = args
        result = cos( num )
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_25(self):
        title = self.function_strings[25]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_26(self):
        title = self.function_strings[26]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_27(self):
        title = self.function_strings[27]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_28(self):
        title = self.function_strings[28]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_29(self):
        title = self.function_strings[29]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_30(self):
        title = self.function_strings[30]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_31(self):
        title = self.function_strings[31]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_32(self):
        title = self.function_strings[32]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def form_33(self):
        title = self.function_strings[33]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def form_34(self):
        title = self.function_strings[34]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def form_35(self):
        title = self.function_strings[35]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_36(self):
        title = self.function_strings[36]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_37(self):
        title = self.function_strings[37]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = (pow(num,2)) - (pow(num2 - num3, 2))
        if  result <= 0 :
            return (self.error_msg, '')
        result = sqrt(result)
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_38(self):
        title = self.function_strings[38]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = 2 * self.PI * num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_39(self):
        title = self.function_strings[39]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_40(self):
        title = self.function_strings[40]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_41(self):
        title = self.function_strings[41]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_42(self):
        title = self.function_strings[42]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_43(self):
        title = self.function_strings[43]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_44(self):
        title = self.function_strings[44]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2,2)
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_45(self):
        title = self.function_strings[45]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_46(self):
        title = self.function_strings[46]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_47(self):
        title = self.function_strings[47]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = (pow(num,2)) - (pow(num2 - num3, 2))
        if  result <= 0 :
            return (self.error_msg, '')
        result = sqrt( result )
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_48(self):
        title = self.function_strings[48]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_49(self):
        title = self.function_strings[49]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2,2)
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_50(self):
        title = self.function_strings[50]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_51(self):
        title = self.function_strings[51]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_52(self):
        title = self.function_strings[52]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_53(self):
        title = self.function_strings[53]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_54(self):
        title = self.function_strings[54]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_55(self):
        title = self.function_strings[55]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_56(self):
        title = self.function_strings[56]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_57(self):
        title = self.function_strings[57]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_58(self):
        title = self.function_strings[58]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = pow((1/num),2) - pow((1/num2) - (1/num3),2)
        if  result <= 0 :
            return (self.error_msg, '')
        result = 1 / sqrt( result )
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_59(self):
        title = self.function_strings[59]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_60(self):
        title = self.function_strings[60]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / (2 * self.PI * num2)
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Rating'))

    def form_61(self):
        title = self.function_strings[61]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_62(self):
        title = self.function_strings[62]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_63(self):
        title = self.function_strings[63]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2,2)
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_64(self):
        title = self.function_strings[64]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_65(self):
        title = self.function_strings[65]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_66(self):
        title = self.function_strings[66]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = 1 / (2 * self.PI * num * num2)
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Rating'))

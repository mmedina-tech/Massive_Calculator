#!/usr/bin/env python3
#
# Resistive_Inductive_Capacitive_Series.py
#
# Python implementation of the resistive/inductive/capacitive formula set.
#

from .FormulaBase import *

class Resistive_Inductive_Capacitive_Series(FormulaBase):
    def __init__(self, name):
        super(Resistive_Inductive_Capacitive_Series, self).__init__(name)
        self.name = name
        self.error_msg = "Can not be a negative square root"
        self.PI = pi

        self.function_strings = {
            1 : "Total Volts using Resistor Volts, Inductor Volts, and Capacitor Volts",
            2 : "Total Volts using Total Amps and Impedance",
            3 : "Total Volts using Volt Amps and Total Amps",
            4 : "Total Volts using Resistor Volts and Power Factor",
            5 : "Volt Amps using Total Volts and Total Amps",
            6 : "Volt Amps using Total Amps and Impedance",
            7 : "Volt Amps using Watts and Power Factor",
            8 : "Volt Amps using Total Volts and Impedance",
            9 : "Volt Amps using Watts, Inductor VAR's, and Capacitor VAR's",
            10 : "Watts using Resistor Volts and Resistor Amps",
            11 : "Watts using Volt Amps, Inductor VAR's, and Capacitor VAR's",
            12 : "Watts using Resistor Volts and Resistance",
            13 : "Watts using Resistor Amps and Resistance",
            14 : "Watts using Volt Amps and Power Factor",
            15 : "Impedance using Resistance, Inductive Reactance, and Capacitive Reactance",
            16 : "Impedance using Total Volts and Total Amps",
            17 : "Impedance using Volt Amps and Total Amps",
            18 : "Impedance using Resistance and Power Factor",
            19 : "Power Factor using Resistance and Impedance",
            20 : "Power Factor using Watts and Volt Amps",
            21 : "Power Factor using Resistor Volts and Total Volts",
            22 : "Power Factor using CoSine and Theta Angle",
            23 : "Capacitor Amps using Capacitor Volts and Capacitive Reactance",
            24 : "Capacitor Amps using Capacitor VAR's and Capacitor Volts",
            25 : "Capacitor Amps using Capacitor VAR's and Capacitive Reactance",
            26 : "Resistor Volts using Resistor Amps and Resistance",
            27 : "Resistor Volts using Watts and Resistor Amps",
            28 : "Total Volts using Volt Amps and Impedance",
            29 : "Total Amps using Total Volts and Impedance",
            30 : "Total Amps using Volt Amps and Total Volts",
            31 : "Total Amps using Volt Amps and Impedance",
            32 : "Resistor Amps using Resistor Volts and Resistance",
            33 : "Resistor Amps using Watts and Resistor Volts",
            34 : "Resistor Amps using Watts and Resistance",
            35 : "Resistance using Impedance, Inductive Reactance, and Capacitive Reactance",
            36 : "Resistance using Resistor Volts and Resistor Amps",
            37 : "Resistance using Resistor Volts and Watts",
            38 : "Resistance using Impedance and Power Factor",
            39 : "Resistance using Watts and Resistor Amps",
            40 : "Capacitor Volts using Capacitor Amps and Capacitive Reactance",
            41 : "Capacitor VAR's using Capacitor Amps and Capacitive Reactance",
            42 : "Capacitor VAR's using Capacitor Volts and Capacitive Reactance",
            43 : "Capacitor VAR's using Capacitor Volts and Capacitor Amps",
            44 : "Inductive Reactance using Inductor Volts and Inductor Amps",
            45 : "Inductive Reactance using Inductor Volts and Inductor VAR's",
            46 : "Inductive Reactance using Frequency and Inductor Reactance",
            47 : "Inductive Reactance using Inductor VAR's and Inductor Amps",
            48 : "Inductor Volts using Inductor Amps and Inductive Reactance",
            49 : "Inductor VAR's using Inductor Volts and Inductor Amps",
            50 : "Resistor Volts using Total Volts, Inductor Volts, and Capacitor Volts",
            51 : "Resistor Volts using Total Volts and Power Factor",
            52 : "Resistor Volts using Watts and Resistance",
            53 : "Inductor Amps using Inductor Volts and Inductive Reactance",
            54 : "Inductor Amps using Inductor VAR's and Inductor Volts",
            55 : "Inductor Amps using Inductor VAR's and Inductive Reactance",
            56 : "Inductor Volts using Inductor VAR's and Inductive Reactance",
            57 : "Inductor VAR's using Inductor Volts and Inductive Reactance",
            58 : "Capacitor Volts using Capacitor VAR's and Capacitive Reactance",
            59 : "Capacitor Volts using Capacitor VAR's and Capacitor Amps",
            60 : "Capacitive Reactance using Frequency and Capacitor Rating",
            61 : "Capacitive Reactance using Capacitor Volts and Capacitor VAR's",
            62 : "Capacitive Reactance using Capacitor Volts and Capacitor Amps",
            63 : "Capacitive Reactance using Capacitor VAR's and Capacitor Amps",
            64 : "Capacitor Rating using Frequency and Capacitive Reactance",
            65 : "Inductor Volts using Inductor VAR's and Inductor Amps",
            66 : "Inductor VAR's using Inductor Amps and Inductive Reactance",
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
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Inductor Votls (input): "),
                ("number_input3", "Capacitor Votls (input): "),
            ]),
            self.function_strings[2]: OrderedDict([
                ("number_input", "Total Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[3]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[4]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[5]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[6]: OrderedDict([
                ("number_input", "Total Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[7]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[8]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[9]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Inductor VAR's (input): "),
                ("number_input3", "Capacitor VAR's (input): "),
            ]),
            self.function_strings[10]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[11]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Inductor VAR's (input): "),
                ("number_input3", "Capacitor VAR's (input): "),
            ]),
            self.function_strings[12]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[13]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[14]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[15]: OrderedDict([
                ("number_input", "Resistance (input): "),
                ("number_input2", "Inductive Reactance (input): "),
                ("number_input3", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[16]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[17]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Total Amps (input): "),
            ]),
            self.function_strings[18]: OrderedDict([
                ("number_input", "Resistance (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[19]: OrderedDict([
                ("number_input", "Resistance (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[20]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Volt Amps (input): "),
            ]),
            self.function_strings[21]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Total Volts (input): "),
            ]),
            self.function_strings[22]: OrderedDict([
                ("number_input", "Theta Angle (input): "),
            ]),
            self.function_strings[23]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[24]: OrderedDict([
                ("number_input", "Capacitor VAR's (input): "),
                ("number_input2", "Capacitor Volts (input): "),
            ]),
            self.function_strings[25]: OrderedDict([
                ("number_input", "Capacitor VAR's (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[26]: OrderedDict([
                ("number_input", "Resistor Amps (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[27]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[28]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[29]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[30]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Total Volts (input): "),
            ]),
            self.function_strings[31]: OrderedDict([
                ("number_input", "Volt Amps (input): "),
                ("number_input2", "Impedance (input): "),
            ]),
            self.function_strings[32]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[33]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistor Volts (input): "),
            ]),
            self.function_strings[34]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[35]: OrderedDict([
                ("number_input", "Impedance (input): "),
                ("number_input2", "Inductive Reactance (input): "),
                ("number_input3", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[36]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[37]: OrderedDict([
                ("number_input", "Resistor Volts (input): "),
                ("number_input2", "Watts (input): "),
            ]),
            self.function_strings[38]: OrderedDict([
                ("number_input", "Impedance (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[39]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistor Amps (input): "),
            ]),
            self.function_strings[40]: OrderedDict([
                ("number_input", "Capacitor Amps (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[41]: OrderedDict([
                ("number_input", "Capacitor Amps (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[42]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[43]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[44]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[45]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductor VAR's (input): "),
            ]),
            self.function_strings[46]: OrderedDict([
                ("number_input", "Frequency (input): "),
                ("number_input2", "Inductor Rating (input): "),
            ]),
            self.function_strings[47]: OrderedDict([
                ("number_input", "Inductor VAR's (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[48]: OrderedDict([
                ("number_input", "Inductor Amps (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[49]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[50]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Inductor Volts (input): "),
                ("number_input3", "Capacitor Volts (input): "),
            ]),
            self.function_strings[51]: OrderedDict([
                ("number_input", "Total Volts (input): "),
                ("number_input2", "Power Factor (input): "),
            ]),
            self.function_strings[52]: OrderedDict([
                ("number_input", "Watts (input): "),
                ("number_input2", "Resistance (input): "),
            ]),
            self.function_strings[53]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[54]: OrderedDict([
                ("number_input", "Inductor VAR's (input): "),
                ("number_input2", "Inductor Volts (input): "),
            ]),
            self.function_strings[55]: OrderedDict([
                ("number_input", "Inductor VAR's (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[56]: OrderedDict([
                ("number_input", "Inductor VAR's (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[57]: OrderedDict([
                ("number_input", "Inductor Volts (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
            self.function_strings[58]: OrderedDict([
                ("number_input", "Capacitor VAR's (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[59]: OrderedDict([
                ("number_input", "Capacitor VAR's (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[60]: OrderedDict([
                ("number_input", "Frequency (input): "),
                ("number_input2", "Capacitor Rating (input): "),
            ]),
            self.function_strings[61]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitor VAR's (input): "),
            ]),
            self.function_strings[62]: OrderedDict([
                ("number_input", "Capacitor Volts (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[63]: OrderedDict([
                ("number_input", "Capacitor VAR's (input): "),
                ("number_input2", "Capacitor Amps (input): "),
            ]),
            self.function_strings[64]: OrderedDict([
                ("number_input", "Frequency (input): "),
                ("number_input2", "Capacitive Reactance (input): "),
            ]),
            self.function_strings[65]: OrderedDict([
                ("number_input", "Inductor VAR's (input): "),
                ("number_input2", "Inductor Amps (input): "),
            ]),
            self.function_strings[66]: OrderedDict([
                ("number_input", "Inductor Amps (input): "),
                ("number_input2", "Inductive Reactance (input): "),
            ]),
        }

        self.formula_list = {
            self.function_strings[1]: {"Formula:<br>" : "sqrt(E<sup>2</sup><sub>R</sub> + (E<sub>L</sub> - E<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[2]: {"Formula:<br>" : "I<sub>T</sub> * Z"},
            self.function_strings[3]: {"Formula:<br>" : "VA / I<sub>T</sub>"},
            self.function_strings[4]: {"Formula:<br>" : "E<sub>R</sub> / PF"},
            self.function_strings[5]: {"Formula:<br>" : "E<sub>T</sub> * I<sub>T</sub>"},
            self.function_strings[6]: {"Formula:<br>" : "I<sub>T</sub><sup>2</sup> * Z"},
            self.function_strings[7]: {"Formula:<br>" : "P / PF"},
            self.function_strings[8]: {"Formula:<br>" : "E<sub>T</sub><sup>2</sup> / Z"},
            self.function_strings[9]: {"Formula:<br>" : "sqrt(P<sup>2</sup> + (VARs<sub>L</sub> - VARs<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[10]: {"Formula:<br>" : "E<sub>R</sub> * I<sub>R</sub>"},
            self.function_strings[11]: {"Formula:<br>" : "sqrt(VA<sup>2</sup> + (VARs<sub>L</sub> - VARs<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[12]: {"Formula:<br>" : "E<sub>R</sub><sup>2</sup> / R"},
            self.function_strings[13]: {"Formula:<br>" : "I<sub>R</sub><sup>2</sup> * R"},
            self.function_strings[14]: {"Formula:<br>" : "VA * PF"},
            self.function_strings[15]: {"Formula:<br>" : "sqrt(R<sup>2</sup> + (X<sub>L</sub> - X<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[16]: {"Formula:<br>" : "E<sub>T</sub> / I<sub>T</sub>"},
            self.function_strings[17]: {"Formula:<br>" : "VA / I<sub>T</sub><sup>2</sup>"},
            self.function_strings[18]: {"Formula:<br>" : "R / PF"},
            self.function_strings[19]: {"Formula:<br>" : "R / Z"},
            self.function_strings[20]: {"Formula:<br>" : "P / VA"},
            self.function_strings[21]: {"Formula:<br>" : "E<sub>R</sub> / E<sub>T</sub>"},
            self.function_strings[22]: {"Formula:<br>" : "CoSine(Theta Angle)"},
            self.function_strings[23]: {"Formula:<br>" : "E<sub>C</sub> / X<sub>C</sub>"},
            self.function_strings[24]: {"Formula:<br>" : "VARs<sub>C</sub> / E<sub>C</sub>"},
            self.function_strings[25]: {"Formula:<br>" : "sqrt(VARs<sub>C</sub> / X<sub>C</sub>)"},
            self.function_strings[26]: {"Formula:<br>" : "I<sub>R</sub> * R"},
            self.function_strings[27]: {"Formula:<br>" : "P / I<sub>R</sub>"},
            self.function_strings[28]: {"Formula:<br>" : "sqrt(VAR * Z)"},
            self.function_strings[29]: {"Formula:<br>" : "E<sub>T</sub> / Z"},
            self.function_strings[30]: {"Formula:<br>" : "VA / E<sub>T</sub>"},
            self.function_strings[31]: {"Formula:<br>" : "sqrt(VA / Z)"},
            self.function_strings[32]: {"Formula:<br>" : "E<sub>R</sub> / R"},
            self.function_strings[33]: {"Formula:<br>" : "P / E<sub>R</sub>"},
            self.function_strings[34]: {"Formula:<br>" : "sqrt(P / R)"},
            self.function_strings[35]: {"Formula:<br>" : "sqrt(Z<sup>2</sup> - (X<sub>L</sub> - X<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[36]: {"Formula:<br>" : "E<sub>R</sub> / I<sub>R</sub>"},
            self.function_strings[37]: {"Formula:<br>" : "E<sub>R</sub><sup>2</sup> / P"},
            self.function_strings[38]: {"Formula:<br>" : "Z * PF"},
            self.function_strings[39]: {"Formula:<br>" : "P / I<sub>R</sub><sup>2</sup>"},
            self.function_strings[40]: {"Formula:<br>" : "I<sub>C</sub> * X<sub>C</sub>"},
            self.function_strings[41]: {"Formula:<br>" : "I<sub>C</sub><sup>2</sup> * X<sub>C</sub>"},
            self.function_strings[42]: {"Formula:<br>" : "E<sub>C</sub><sup>2</sup> / X<sub>C</sub>"},
            self.function_strings[43]: {"Formula:<br>" : "E<sub>C</sub> * I<sub>C</sub>"},
            self.function_strings[44]: {"Formula:<br>" : "E<sub>L</sub> / I<sub>L</sub>"},
            self.function_strings[45]: {"Formula:<br>" : "E<sub>L</sub><sup>2</sup> / VARs<sub>L</sub>"},
            self.function_strings[46]: {"Formula:<br>" : "2 * PI * F * L"},
            self.function_strings[47]: {"Formula:<br>" : "VARs<sub>L</sub> / I<sub>L</sub><sup>2</sup>"},
            self.function_strings[48]: {"Formula:<br>" : "I<sub>L</sub> * X<sub>L</sub>"},
            self.function_strings[49]: {"Formula:<br>" : "E<sub>L</sub> * I<sub>L</sub>"},
            self.function_strings[50]: {"Formula:<br>" : "sqrt(E<sub>T</sub><sup>2</sup> - (E<sub>L</sub> - E<sub>C</sub>)<sup>2</sup>)"},
            self.function_strings[51]: {"Formula:<br>" : "E<sub>T</sub> * PF"},
            self.function_strings[52]: {"Formula:<br>" : "sqrt(P * R)"},
            self.function_strings[53]: {"Formula:<br>" : "E<sub>L</sub> / X<sub>L</sub>"},
            self.function_strings[54]: {"Formula:<br>" : "VARs<sub>L</sub> / E<sub>L</sub>"},
            self.function_strings[55]: {"Formula:<br>" : "sqrt(VARs<sub>L</sub> / X<sub>L</sub>)"},
            self.function_strings[56]: {"Formula:<br>" : "sqrt(VARs<sub>L</sub> *  X<sub>L</sub>)"},
            self.function_strings[57]: {"Formula:<br>" : "E<sub>L</sub><sup>2</sup> / X<sub>L</sub>"},
            self.function_strings[58]: {"Formula:<br>" : "sqrt(VARs<sub>C</sub> * X<sub>C</sub>)"},
            self.function_strings[59]: {"Formula:<br>" : "VARs<sub>C</sub> / I<sub>C</sub>"},
            self.function_strings[60]: {"Formula:<br>" : "1 / (2 * PI * F * C)"},
            self.function_strings[61]: {"Formula:<br>" : "E<sub>C</sub><sup>2</sup> / VARs<sub>C</sub>"},
            self.function_strings[62]: {"Formula:<br>" : "E<sub>C</sub> / I<sub>C</sub>"},
            self.function_strings[63]: {"Formula:<br>" : "VARs<sub>C</sub> / I<sub>C</sub><sup>2</sup>"},
            self.function_strings[64]: {"Formula:<br>" : "1 /( 2 * PI * F X<sub>C</sub> )"},
            self.function_strings[65]: {"Formula:<br>" : "VARs<sub>L</sub> / I<sub>L</sub>"},
            self.function_strings[66]: {"Formula:<br>" : "I<sub>L</sub><sup>2</sup> * X<sub>L</sub>"},
        }

    def _prompt_inputs(self, title):
        args_out = [title] + list(self.functionInputs[title].values())
        return self.prompt(args_out)

    def form_1(self):
        title = self.function_strings[1]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = sqrt( pow(num, 2) + (pow(num2 - num3, 2)))
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_2(self):
        title = self.function_strings[2]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_3(self):
        title = self.function_strings[3]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_4(self):
        title = self.function_strings[4]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_5(self):
        title = self.function_strings[5]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_6(self):
        title = self.function_strings[6]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_7(self):
        title = self.function_strings[7]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_8(self):
        title = self.function_strings[8]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_9(self):
        title = self.function_strings[9]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = sqrt(pow(num, 2) + (num2 - pow(num3, 2)))
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_10(self):
        title = self.function_strings[10]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_11(self):
        title = self.function_strings[11]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = pow(num, 2) - pow(num2 - num3, 2)
        if  result <= 0 :
            return (self.error_msg, '')
        result = sqrt(result)
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_12(self):
        title = self.function_strings[12]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_13(self):
        title = self.function_strings[13]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_14(self):
        title = self.function_strings[14]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_15(self):
        title = self.function_strings[15]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = pow(num, 2) + pow(num2 - num3, 2)
        if  result <= 0 :
            return (self.error_msg, '')
        result =  sqrt(result)
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_16(self):
        title = self.function_strings[16]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_17(self):
        title = self.function_strings[17]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2, 2)
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_18(self):
        title = self.function_strings[18]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_19(self):
        title = self.function_strings[19]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_20(self):
        title = self.function_strings[20]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_21(self):
        title = self.function_strings[21]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_22(self):
        title = self.function_strings[22]
        args = self._prompt_inputs(title)
        num = args
        result = cos( num )
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_23(self):
        title = self.function_strings[23]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_24(self):
        title = self.function_strings[24]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_25(self):
        title = self.function_strings[25]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_26(self):
        title = self.function_strings[26]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_27(self):
        title = self.function_strings[27]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_28(self):
        title = self.function_strings[28]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_29(self):
        title = self.function_strings[29]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_30(self):
        title = self.function_strings[30]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_31(self):
        title = self.function_strings[31]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_32(self):
        title = self.function_strings[32]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_33(self):
        title = self.function_strings[33]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_34(self):
        title = self.function_strings[34]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_35(self):
        title = self.function_strings[35]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = pow(num, 2) - pow(num2 - num3, 2)
        if  result <= 0 :
            return (self.error_msg, '')
        result = sqrt(result)
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_36(self):
        title = self.function_strings[36]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_37(self):
        title = self.function_strings[37]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_38(self):
        title = self.function_strings[38]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_39(self):
        title = self.function_strings[39]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2,2)
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_40(self):
        title = self.function_strings[40]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_41(self):
        title = self.function_strings[41]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def form_42(self):
        title = self.function_strings[42]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def form_43(self):
        title = self.function_strings[43]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def form_44(self):
        title = self.function_strings[44]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_45(self):
        title = self.function_strings[45]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_46(self):
        title = self.function_strings[46]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = 1 / (2 * self.PI * num * num2)
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_47(self):
        title = self.function_strings[47]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2,2)
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_48(self):
        title = self.function_strings[48]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_49(self):
        title = self.function_strings[49]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_50(self):
        title = self.function_strings[50]
        args = self._prompt_inputs(title)
        num, num2, num3 = args
        result = pow(num, 2) - pow(num2 - num3, 2)
        if  result <= 0 :
            return (self.error_msg, '')
        result = sqrt(result)
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_51(self):
        title = self.function_strings[51]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num * num2
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_52(self):
        title = self.function_strings[52]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_53(self):
        title = self.function_strings[53]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_54(self):
        title = self.function_strings[54]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_55(self):
        title = self.function_strings[55]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num / num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_56(self):
        title = self.function_strings[56]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_57(self):
        title = self.function_strings[57]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num,2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_58(self):
        title = self.function_strings[58]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = sqrt( num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_59(self):
        title = self.function_strings[59]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_60(self):
        title = self.function_strings[60]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = 1/( 2 * self.PI * num * num2 )
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_61(self):
        title = self.function_strings[61]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_62(self):
        title = self.function_strings[62]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_63(self):
        title = self.function_strings[63]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / pow(num2, 2)
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_64(self):
        title = self.function_strings[64]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = 1/ (2 * self.PI * num * num2)
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Rating'))

    def form_65(self):
        title = self.function_strings[65]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = num / num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_66(self):
        title = self.function_strings[66]
        args = self._prompt_inputs(title)
        num, num2 = args
        result = pow(num, 2) * num2
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

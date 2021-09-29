#!/usr/bin/python 
#
# ResistiveInductance_series.py
#
# Copyright 2020 Marcus Medina <mmedina@src.com>
#
# This program is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#


from FormulaBase import *

class ResistiveInductance_series(FormulaBase):
    def __init__(self):
        super(ResistiveInductance_series, self).__init__(name)
        self.name = name
        self.error_msg = "Can not be a negative square root"

#{{{___ Function Titles _____________________________________________________________________________

        self.function_strings = {
            #55 Functions
            1 : 'Impedance using Resistance and Inductive Reactance',
            2 : 'Impedance using Resistance and Power Factor',
            3 : 'Impedance using Total Volts and Total Amps',
            4 : 'Impedance using Total Volts and Volt Amps',
            5 : 'Impedance using Volt Amps and Total Volts',
            6 : "Inductor Amps using Inductor VAR's and Inductive Reactance",
            7 : "Inductor Amps using Inductor VAR's and Inductor Volts",
            8 : 'Inductor Amps using Inductor Volts and Inductive Reactance',
            9 : 'Inductor Rating using Inductive Reactance and Frequency',
            10 : 'Inductive Reactance using Frequency and Inductor Rating',
            11 : "Inductive Reactance using Inductor VAR's and Inductor Amps",
            12 : 'Inductive Reactance using Impedance and Resistance',
            13 : 'Inductive Reactance using Inductor Volts and Inductor Amps',
            14 : "Inductive Reactance using Inductor Volts and Inductor VAR's",
            15 : "Inductor VAR's using Inductor Amps and Inductive Reactance",
            16 : "Inductor VAR's using Inductor Volts and Inductor Amps",
            17 : "Inductor VAR's using Inductor Volts and Inductive Reactance",
            18 : "Inductor VAR's using Volt Amps and Watts",
            19 : 'Inductor Volts using Inductor Amps and Inductive Reactance',
            20 : "Inductor Volts using Inductor VAR's and Inductive Reactance",
            21 : "Inductor Volts using Inductor VAR's and Inductor Amps",
            22 : 'Inductor Volts using Total Volts and Resistor Volts',
            23 : 'Power Factor using CoSine and Theta Angle',
            24 : 'Power Factor using Resistance and Impedance',
            25 : 'Power Factor using Resistor Volts and Total Volts',
            26 : 'Power Factor using Watts and Volt Amps',
            27 : 'Resistance using Impedance and Inductive Reactance',
            28 : 'Resistance using Impedance and Power Factor',
            29 : 'Resistance using Resistor Volts and Resistor Amps',
            30 : 'Resistance using Resistor Volts and Watts',
            31 : 'Resistance using Watts and Resistor Amps',
            32 : 'Resistor Amps using Resistor Volts and Resistance',
            33 : 'Resistor Amps using Watts and Resistor Volts',
            34 : 'Resistor Amps using Watts and Resistance',
            35 : 'Resistor Volts using Resistor Amps and Resistance',
            36 : 'Resistor Volts using Total Volts and Inductor Volts',
            37 : 'Resistor Volts using Total Volts and Power Factor',
            38 : 'Resistor Volts using Watts and Resistance',
            39 : 'Resistor Volts using Watts and Resistor Amps',
            40 : 'Total Amps using Total Volts and Impedance',
            41 : 'Total Amps using Volt Amps and Total Volts',
            42 : 'Total Volts using Resistor Volts and Inductor Volts',
            43 : 'Total Volts using Resistor Volts and Power Factor',
            44 : 'Total Volts using Total Amps and Impedance',
            45 : 'Total Volts using Volt Amps and Total Amps',
            46 : 'Volt Amps using Total Amps and Impedance',
            47 : 'Volt Amps using Total Volts and Total Amps',
            48 : 'Volt Amps using Total Volts and Impedance',
            49 : "Volt Amps using Watts and Inductor VAR's",
            50 : 'Volt Amps using Watts and Power Factor',
            51 : 'Watts using Resistor Amps and Resistance',
            52 : 'Watts using Resistor Volts and Resistor Amps',
            53 : 'Watts using Resistor Volts and Resistance',
            54 : "Watts using Volt Amps and Inductor VAR's",
            55 : 'Watts using Volt Amps and Power Factor',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_impedance),
                (self.function_strings[2], self.form_impedance4),
                (self.function_strings[3], self.form_impedance2),
                (self.function_strings[4], self.form_impedance5),
                (self.function_strings[5], self.form_impedance3),
                (self.function_strings[6], self.form_iAmps3),
                (self.function_strings[7], self.form_iAmps2),
                (self.function_strings[8], self.form_iAmps),
                (self.function_strings[9], self.form_inductor),
                (self.function_strings[10], self.form_iReactance5),
                (self.function_strings[11], self.form_iReactance4),
                (self.function_strings[12], self.form_iReactance),
                (self.function_strings[13], self.form_iReactance2),
                (self.function_strings[14], self.form_iReactance3),
                (self.function_strings[15], self.form_VAR4),
                (self.function_strings[16], self.form_VAR2),
                (self.function_strings[17], self.form_VAR3),
                (self.function_strings[18], self.form_VAR),
                (self.function_strings[19], self.form_inductance),
                (self.function_strings[20], self.form_inductance3),
                (self.function_strings[21], self.form_inductance4),
                (self.function_strings[22], self.form_inductance2),
                (self.function_strings[23], self.form_powerFactor4),
                (self.function_strings[24], self.form_powerFactor),
                (self.function_strings[25], self.form_powerFactor3),
                (self.function_strings[26], self.form_powerFactor2),
                (self.function_strings[27], self.form_resistance),
                (self.function_strings[28], self.form_resistance4),
                (self.function_strings[29], self.form_resistance2),
                (self.function_strings[30], self.form_resistance5),
                (self.function_strings[31], self.form_resistance3),
                (self.function_strings[32], self.form_rAmps),
                (self.function_strings[33], self.form_rAmps2),
                (self.function_strings[34], self.form_rAmps3),
                (self.function_strings[35], self.form_rVolts),
                (self.function_strings[36], self.form_rVolts4),
                (self.function_strings[37], self.form_rVolts5),
                (self.function_strings[38], self.form_rVolts2),
                (self.function_strings[39], self.form_rVolts3),
                (self.function_strings[40], self.form_tAmps),
                (self.function_strings[41], self.form_tAmps2),
                (self.function_strings[42], self.form_tVolts),
                (self.function_strings[43], self.form_tVolts4),
                (self.function_strings[44], self.form_tVolts2),
                (self.function_strings[45], self.form_tVolts3),
                (self.function_strings[46], self.form_va2),
                (self.function_strings[47], self.form_va),
                (self.function_strings[48], self.form_va3),
                (self.function_strings[49], self.form_va4),
                (self.function_strings[50], self.form_va5),
                (self.function_strings[51], self.form_watts4),
                (self.function_strings[52], self.form_watts),
                (self.function_strings[53], self.form_watts3),
                (self.function_strings[54], self.form_watts2),
                (self.function_strings[55], self.form_watts5),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[1]:OrderedDict(
                [
                    ("number_input" , "Resistance (input): "),
                    ("number_input2" , "Inductive Reactance (input): ")
                ]
            ),
            self.function_strings[2]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[3]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[4]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Volt Amps: ')
                    ]
            ),
            self.function_strings[5]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Volts: ')
                    ]
            ),
            self.function_strings[6]:OrderedDict(
                [
                    ("number_input" , "Inductor VAR's (input): "),
                    ("number_input2" , "Inductive Reactance (input): ")
                ]
            ),
            self.function_strings[7]:OrderedDict(
                [
                    ("number_input" , "Inductor VAR's (input): "),
                    ("number_input2" , "Inductor Volts (input): ")
                ]
            ),
            self.function_strings[8]:OrderedDict(
                [
                    ("number_input" , "Inductor Volts (input): "),
                    ("number_input2" , "Inductive Reactance (input): ")
                ]
            ),
            self.function_strings[9]:OrderedDict(
                    [
                            ('number_input', 'Inductive Reactance: '),
                            ('number_input2', 'Frequency: ')
                    ]
            ),
            self.function_strings[10]:OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Inductor Rating: ')
                    ]
            ),
            self.function_strings[11]:OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[12]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[12]:OrderedDict(
                [
                    ("number_input" , "Impedance (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            self.function_strings[13]:OrderedDict(
                    [
                            ('numebr_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[14]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            self.function_strings[15]:OrderedDict(
                    [
                            ('number_input', 'Inductor Amps: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[16]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[17]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[18]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            self.function_strings[19]:OrderedDict(
                    [
                            ('number_input', 'Inductor Amps: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[20]:OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[21]:OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[22]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            self.function_strings[23]:OrderedDict(
                    [
                            ('number_input', 'CoSine: '),
                            ('number_input2', 'Theta Angle: ')
                    ]
            ),
            self.function_strings[24]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[25]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Total Volts: ')
                    ]
            ),
            self.function_strings[26]:OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Volt Amps (input): ")
                ]
            ),
            self.function_strings[27]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[28]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[29]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[30]:OrderedDict(
                    [
                            ('number_input',  'Resistor Volts: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            self.function_strings[31]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps')
                    ]
            ),
            self.function_strings[32]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[33]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            self.function_strings[34]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[35]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[36]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Inductor Volts: ')
                    ]
            ),
            self.function_strings[37]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[38]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[39]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('numebr_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[40]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[41]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Volts: ')
                    ]
            ),
            self.function_strings[42] : OrderedDict(
                [
                    ('number_input', 'Resistor Volts: '),
                    ('number_input2', 'Inductor Volts: ')
                ]
            ),
            self.function_strings[43] : OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[44] : OrderedDict(
                [
                    ('number_input', 'Total Amps: '),
                    ('number_input2', 'Impedance: ')
                ]
            ),
            self.function_strings[45] : OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[46]:OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[47]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[48]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[49]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            self.function_strings[50]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[51]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[52]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[53]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[54]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            self.function_strings[55]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{              #self.form_impedance),
                '' : 'sqrt(Resistance^2 + Inductive Reactance^2)'
            },
            self.function_strings[2]:{                     #self.form_impedance4),
                '' : 'Resistance / Power Factor'
            },
            self.function_strings[3]:{                      #self.form_impedance2),
                '' : 'Total Volts / Total Amps'
            },
            self.function_strings[4]:{                       #self.form_impedance5),
                '' : 'Total Volts / Volt Amps'
            },
            self.function_strings[5]:{                       #self.form_impedance3),
                '' : 'Volt Amps / Total Volts'
            },
            self.function_strings[6]:{      #self.form_iAmps3),
                '' : "sqrt(Inductor VAR's / Inductive Reactance)"
            },
            self.function_strings[7]:{           #self.form_iAmps2),
                '' : "Inductor VAR's / Inductor Volts"
            },
            self.function_strings[8]:{      #self.form_iAmps),
                '' : "Inductor Volts / Inductive Reactance"
            },
            self.function_strings[9]:{         #self.form_inductor),
                '' : 'Inductive Reactance / (2 * 3.14 * Frequency)'
            },
            self.function_strings[10]:{         #self.form_iReactance5),
                '' : '2 * 3.14 * Frequency * Inductor Rating'
            },
            self.function_strings[11]:{      #self.form_iReactance4),
                '' : "Inductor VAR's / Inductor Amps^2"
            },
            self.function_strings[12]:{              #self.form_iReactance),
                '' : 'sqrt(Impedance^2 - Resistance^2)'
            },
            self.function_strings[13]:{      #self.form_iReactance2),
                '' : 'Inductor Volts / Inductor Amps'
            },
            self.function_strings[14]:{     #self.form_iReactance3),
                '' : "Inductor Volts^2 / Inductor VAR's"
            },
            self.function_strings[15]:{      #self.form_VAR4),
                '' : 'Inductor Amps^2 * Inductive Reactance'
            },
            self.function_strings[16]:{           #self.form_VAR2),
                '' : 'Inductor Volts * Inductor Amps'
            },
            self.function_strings[17]:{     #self.form_VAR3),
                '' : 'Inductor Volts^2 / Inductive Reactance'
            },
            self.function_strings[18]:{                        #self.form_VAR),
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
            self.function_strings[19]:{      #self.form_inductance),
                '' : 'Inductor Amps * Inductive Reactance'
            },
            self.function_strings[20]:{     #self.form_inductance3),
                '' : "sqrt(Inductor VAR's * Inductive Reactance)"
            },
            self.function_strings[21]:{           #self.form_inductance4),
                '' : "Inductor VAR's / Inductor Amps"
            },
            self.function_strings[22]:{             #self.form_inductance2),
                '' : "sqrt(Total Volts^2 - Resistor Volts^2)"
            },
            self.function_strings[23]:{                       #self.form_powerFactor4),
                '' : 'CoSine * Theta Angle'
            },
            self.function_strings[24]:{                     #self.form_powerFactor),
                '' : 'Resistance / Impedance'
            },
            self.function_strings[25]:{               #self.form_powerFactor3),
                '' : 'Resistor Volts / Total Volts'
            },
            self.function_strings[26]:{                          #self.form_powerFactor2),
                '' : "Watts / Volt Amps"
            },
            self.function_strings[27]:{              #self.form_resistance),
                '' : 'sqrt(Impedance^2 - Inductive Reactance^2)'
            },
            self.function_strings[28]:{                     #self.form_resistance4),
                '' : 'Impedance / Power Factor^2'
            },
            self.function_strings[29]:{               #self.form_resistance2),
                '' : 'Resistor Volts / Resistor Amps'
            },
            self.function_strings[30]:{                       #self.form_resistance5),
                '' : 'Resistor Volts * Watts'
            },
            self.function_strings[31]:{                        #self.form_resistance3),
                '' : "Watts^2 / Resistor Amps"
            },
            self.function_strings[32]:{               #self.form_rAmps),
                '' : 'Resistor Volts / Resistance'
            },
            self.function_strings[33]:{                    #self.form_rAmps2),
                '' : "Watts / Resistor Volts"
            },
            self.function_strings[34]:{                        #self.form_rAmps3),
                '' : 'sqrt(Watts / Resistance)'
            },
            self.function_strings[35]:{               #self.form_rVolts),
                '' : 'Resistor Amps * Resistance'
            },
            self.function_strings[36]:{             #self.form_rVolts4),
                '' : 'sqrt(Total Volts^2 - Inductor Volts^2)'
            },
            self.function_strings[37]:{               #self.form_rVolts5),
                '' : "Total Volts * Power Factor"
            },
            self.function_strings[38]:{                       #self.form_rVolts2),
                '' : 'sqrt(Watts * Resistance)'
            },
            self.function_strings[39]:{                    #self.form_rVolts3),
                '' : 'Watts / Resistor Amps'
            },
            self.function_strings[40]:{                      #self.form_tAmps),
                '' : 'Total Volts / Impedance'
            },
            self.function_strings[41]:{                      #self.form_tAmps2),
                '' : 'Volt Amps / Total Volts'
            },
            self.function_strings[42]:{             #self.form_tVolts),
                '' : 'sqrt(Resistor Volts^2 + Inductor Volts^2)'
            },
            self.function_strings[43]:{               #self.form_tVolts4),
                '' : 'Resistor Volts / Power Factor'
            },
            self.function_strings[44]:{                      #self.form_tVolts2),
                '' : 'Total Amps * Impedance'
            },
            self.function_strings[45]:{                      #self.form_tVolts3),
                '' : 'Volt Amps / Total Amps'
            },
            self.function_strings[46]:{                        #self.form_va2),
                '' : 'Total Amps^2 * Impedance'
            },
            self.function_strings[47]:{                      #self.form_va),
                '' : 'Total Volts * Total Amps'
            },
            self.function_strings[48]:{                       #self.form_va3),
                '' : 'Total Volts^2 / Impedance'
            },
            self.function_strings[49]:{                        #self.form_va4),
                '' : "sqrt(Watts^2 + Inductor VAR's^2)"
            },
            self.function_strings[50]:{                          #self.form_va5),
                '' : 'Watts / Power Factor'
            },
            self.function_strings[51]:{                        #self.form_watts4),
                '' : 'Resistor Amps^2 * Resistance'
            },
            self.function_strings[52]:{                    #self.form_watts),
                '' : 'Resistor Volts * Resistor Amps'
            },
            self.function_strings[53]:{                       #self.form_watts3),
                '' : 'Resistor Volts^2 / Resistance'
            },
            self.function_strings[54]:{                        #self.form_watts2),
                '' : "sqrt(Volt Amps^2 - Inductor VAR'^2)"
            },
            self.function_strings[55]:{                          #self.form_watts5),
                '' : 'Volt Amps * Power Factor'
            },
        }

#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def form_impedance(self):
        title = self.function_strings[1]
        arg1 = "Enter Resistance"
        arg2 = "Enter Inductive Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1] ** 2))
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_impedance4(self):
        title = self.function_strings[2]
        arg1 = "Enter Resistance"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_impedance2(self):
        title = self.function_strings[3]
        arg1 = "Enter Total Volts"
        arg2 = "Enter Total Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_impedance5(self):
        title = self.function_strings[4]
        arg1 = "Enter Total Volts"
        arg2 = "Enter Volt Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_impedance3(self):
        title = self.function_strings[5]
        arg1 = "Enter Volt Amps"
        arg2 = "Enter Total Volts"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_iAmps3(self):
        title = self.function_strings[6]
        arg1 = "Enter Inductor VAR's"
        arg2 = "Enter Inductive Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_iAmps2(self):
        title = self.function_strings[7]
        arg1 = "Enter Inductor VAR's"
        arg2 = "Inductor Volts"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_iAmps(self):
        title = self.function_strings[8]
        arg1 = "Enter Inductor Volts"
        arg2 = "Enter Inductive Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_inductor(self):
        title = self.function_strings[9]
        arg1 = "Enter Inductive Reactance"
        arg2 = "Enter Frequency"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (2*3.14*argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Size'))

    def form_iReactance5(self):
        title = self.function_strings[10]
        arg1 = "Enter Frequency"
        arg2 = "Enter Inductor Rating"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = 2*3.14*argsIn[0]*argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance4(self):
        title = self.function_strings[11]
        arg1 = "Enter Inductor VAR's"
        arg2 = "Enter Inductor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance(self):
        try:
            title = self.function_strings[12]
            arg1 = "Enter Impedance"
            arg2 = "Enter Resistance"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
            return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance Rating'))
        except(Exception):
            return (self.error_msg, '')

    def form_iReactance2(self):
        title = self.function_strings[13]
        arg1 = "Enter Inductor Volts"
        arg2 = "Enter Inductor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance3(self):
        title = self.function_strings[14]
        arg1 = "Enter Inductor Volts"
        arg2 = "Enter Inductor VAR's"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_VAR4(self):
        title = self.function_strings[15]
        arg1 = "Enter Inductor Amps"
        arg2 = "Enter Inductive Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Inductor VAR'"))

    def form_VAR2(self):
        title = self.function_strings[16]
        arg1 = "Enter Inductor Volts"
        arg2 = "Enter Inductor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Inductor VAR'"))

    def form_VAR3(self):
        title = self.function_strings[17]
        arg1 = "Enter Inductor Volts"
        arg2 = "Enter Inductuve Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Inductor VAR'"))

    def form_VAR(self):
        try:
            title = self.function_strings[18]
            arg1 = "Enter Volt Amps"
            arg2 = "Enter Watts"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
            return (self.prec(result, 4), self.pluralize(result, "Inductor VAR'"))
        except(Exception):
            return (self.error_msg, '')

    def form_inductance(self):
        title = self.function_strings[19]
        arg1 = "Enter Inductor Amps"
        arg2 = "Enter Inductive Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_inductance3(self):
        title = self.function_strings[20]
        arg1 = "Enter Inductor VAR's"
        arg2 = "Enter Inductive Reactance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_inductance4(self):
        title = self.function_strings[21]
        arg1 = "Enter Inductor VAR's"
        arg2 = "Enter Inductor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_inductance2(self):
        try:
            title = self.function_strings[22]
            arg1 = "Enter Total Volts"
            arg2 = "Enter Resistor Volts"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] **2) - (argsIn[1] **2))
            return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))
        except(Exception):
            return (self.error_msg, '')

    def form_powerFactor4(self):
        title = self.function_strings[23]
        arg1 = "Enter CoSine"
        arg2 = "Enter Theta Angle"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_powerFactor(self):
        title = self.function_strings[24]
        arg1 = 'Enter Resistance'
        arg2 = 'Enter Impedance'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_powerFactor3(self):
        title = self.function_strings[25]
        arg1 = 'Enter Resistor Volts'
        arg2 = 'Enter Total Volts'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_powerFactor2(self):
        title = self.function_strings[26]
        arg1 = 'Enter Watts'
        arg2 = 'Enter Volt Amps'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))
        
    def form_resistance(self):
        try:
            title = self.function_strings[27]
            arg1 = "Enter Impedance"
            arg2 = "Enter Inductive Reactance"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
            return (self.prec(result, 4), self.pluralize(result, 'Resistance'))
        except(Exception):
            return (self.error_msg, '')

    def form_resistance4(self):
        title = self.function_strings[28]
        arg1 = "Enter Impedance"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[0] ** 2)
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_resistance2(self):
        title = self.function_strings[29]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Resistor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_resistance5(self):
        title = self.function_strings[30]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Watts"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_resistance3(self):
        title = self.function_strings[31]
        arg1 = "Enter Watts"
        arg2 = "Enter Resistor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))
    
    def form_rAmps(self):
        title = self.function_strings[32]
        arg1 = "Enter Total Volts"
        arg2 = "Enter Inductor Volts"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_rAmps2(self):
        title = self.function_strings[33]
        arg1 = "Enter Total Volts"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_rAmps3(self):
        title = self.function_strings[34]
        arg1 = "Enter Watts"
        arg2 = "Enter Resistance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_rVolts(self):
        title = self.function_strings[35]
        arg1 = "Enter Watts"
        arg2 = "Enter Resistor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts4(self):
        try:
            title = self.function_strings[36]
            arg1 = "Enter Total Volts"
            arg2 = "Enter Impedance"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
            return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))
        except(Exception):
            return (self.error_msg, '')

    def form_rVolts5(self):
        title = self.function_strings[37]
        arg1 = "Enter Volt Amps"
        arg2 = "Enter Total Volts"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts2(self):    
        title = self.function_strings[38]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Inductor Volts"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts3(self):
        title = self.function_strings[39]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_tAmps(self):
        title = self.function_strings[40]
        arg1 = "Enter Total Amps"
        arg2 = "Enter Impedance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_tAmps2(self):
        title = self.function_strings[41]
        arg1 = "Enter Volt Amps"
        arg2 = "Enter Total Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_tVolts(self):
        title = self.function_strings[42]
        arg1 = "Enter Total Amps"
        arg2 = "Enter Impedance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0] ** 2) + ((argsIn[1] ** 2)))
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))
        
    def form_tVolts4(self):
        title = self.function_strings[43]
        arg1 = "Enter Total Volts"
        arg2 = "Enter Total Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))
        
    def form_tVolts2(self):
        title = self.function_strings[44]
        arg1 = "Enter Total Volts"
        arg2 = "Enter Impedance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))
        
    def form_tVolts3(self):
        title = self.function_strings[45]
        arg1 = "Enter Watts"
        arg2 = "Enter Inductor VAR's"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))
        
    def form_va2(self):
        title = self.function_strings[46]
        arg1 = "Enter Watts"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_va(self):
        title = self.function_strings[47]
        arg1 = "Enter Resistor Amps"
        arg2 = "Enter Resistance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_va3(self):
        title = self.function_strings[48]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Resistor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_va4(self):
        title = self.function_strings[49]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Resistance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_va5(self):
        title = self.function_strings[50]
        arg1 = "Enter Watts"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_watts4(self):
        title = self.function_strings[51]
        arg1 = "Enter Resistor Amps"
        arg2 = "Enter Resistance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_watts(self):
        title = self.function_strings[52]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Resistor Amps"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_watts3(self):
        title = self.function_strings[53]
        arg1 = "Enter Resistor Volts"
        arg2 = "Enter Resistance"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] **2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_watts2(self):
        try:
            title = self.function_strings[54]
            arg1 = "Enter Volt Amps"
            arg2 = "Enter Inductor VAR's"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
            return (self.prec(result, 4), self.pluralize(result, 'Watt'))
        except(Exception):
            return (self.error_msg, '')

    def form_watts5(self):
        title = self.function_strings[55]
        arg1 = "Enter Volt Amps"
        arg2 = "Enter Power Factor"
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

#}}}_________________________________________________________________________________________
        

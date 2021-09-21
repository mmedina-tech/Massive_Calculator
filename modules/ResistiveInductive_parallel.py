#!/usr/bin/python
#
# ResistiveInductive_parallel.py
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

class ResistiveInductive_parallel(FormulaBase):
    def __init__(self):
        super(ResistiveInductive_parallel, self).__init__()
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            #56 Function Titles
            1 : 'Impedance using Resistance and Inductive Reactance',
            2 : 'Impedance using Total Volts and Total Amps',
            3 : 'Impedance using Total Volts and Volt Amps',
            4 : 'Impedance using Volt Amps and Total Amps',
            5 : 'Impedance using Resistance and Power Factor',
            6 : 'Inductive Reactance using Frequency and Inductor Rating',
            7 : 'Inductive Reactance using Impedance and Resistance',
            8 : "Inductive Reactance using Inductor VAR's and Inductor Amps",
            9 : 'Inductive Reactance using Inductor Volts and Inductor Amps',
            10 : "Inductive Reactance using Inductor Volts and Inductor VAR's",
            11 : "Inductor Amps using Inductor VAR's and Inductor Volts",
            12 : "Inductor Amps using Inductor VAR's and Inductive Reactance",
            13 : 'Inductor Amps using Inductor Volts and Inductive Reactance',
            14 : 'Inductor Amps using Total Amps and Resistor Amps',
            15 : 'Inductor Rating using Inductive Reactance and Frequency',
            16 : "Inductor VAR's using Inductor Amps and Inductive Reactance",
            17 : "Inductor VAR's using Inductor Volts and Inductor Amps",
            18 : "Inductor VAR's using Inductor Volts and Inductive Reactance",
            19 : "Inductor VAR's using Volt Amps and Watts",
            20 : "Inductor Volts using Inductor VAR's and Inductive Reactance",
            21 : 'Inductor Volts using Inductor Amps and Inductive Reactance',
            22 : "Inductor Volts using Inductor VAR's and Inductor Amps",
            23 : 'Power Factor using CoSine and Theta Angle',
            24 : 'Power Factor using Impedance and Resistance',
            25 : 'Power Factor using Resistor Amps and Total Amps',
            26 : 'Power Factor using Watts and Volt Amps',
            27 : 'Resistance using Impedance and Inductive Reactance',
            28 : 'Resistance using Impedance and Power Factor',
            29 : 'Resistance using Resistor Volts and Resistor Amps',
            30 : 'Resistance using Watts and Resistor Amps',
            31 : 'Resistor Amps using Resistor Volts and Resistance',
            32 : 'Resistor Amps using Total Amps and Inductor Amps',
            33 : 'Resistor Amps using Total Amps and Power Factor',
            34 : 'Resistor Amps using Watts and Resistance',
            35 : 'Resistor Amps using Watts and Resistor Volts',
            36 : 'Resistor Volts using Resistor Amps and Resistance',
            37 : 'Resistor Volts using Watts and Resistance',
            38 : 'Resistor Volts using Watts and Resistor Amps',
            39 : 'Total Amps using Resistor Amps and Inductor Amps',
            40 : 'Total Amps using Resistor Amps and Power Factor',
            41 : 'Total Amps using Total Volts and Impedance',
            42 : 'Total Amps using Volt Amps and Total Volts',
            43 : 'Total Amps using Volt Amps and Impedance',
            44 : 'Total Volts using Total Amps and Impedance',
            45 : 'Total Volts using Volt Amps and Impedance',
            46 : 'Total Volts using Volt Amps and Total Amps',
            47 : 'Volt Amps using Total Amps and Impedance',
            48 : 'Volt Amps using Total Volts and Impedance',
            49 : 'Volt Amps using Total Volts and Total Amps',
            50 : "Volt Amps using Watts and Inductor VAR's",
            51 : 'Volt Amps using Watts and Power Factor',
            52 : 'Watts using Resistor Amps and Resistance',
            53 : 'Watts using Resistor Volts and Resistance',
            54 : 'Watts using Resistor Volts and Resistor Amps',
            55 : "Watts using Volt Amps and Inductor VAR's",
            56 : 'Watts using Volt Amps and Power Factor',
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_Impedance),
                (self.function_strings[2], self.form_Impedance2),
                (self.function_strings[3], self.form_Impedance3),
                (self.function_strings[4], self.form_Impedance4),
                (self.function_strings[5], self.form_Impedance5),
                (self.function_strings[6], self.form_InductRe3),
                (self.function_strings[7], self.form_InductRe4),
                (self.function_strings[8], self.form_InductRe2),
                (self.function_strings[9], self.form_InductRe5),
                (self.function_strings[10], self.form_InductRe),
                (self.function_strings[11], self.form_InductA3),
                (self.function_strings[12], self.form_InductA4),
                (self.function_strings[13], self.form_InductA2),
                (self.function_strings[14], self.form_InductA), 
                (self.function_strings[15], self.form_InductorRating),
                (self.function_strings[16], self.form_InductorV),
                (self.function_strings[17], self.form_InductorV3),
                (self.function_strings[18], self.form_InductorV4),
                (self.function_strings[19], self.form_InductorV2),
                (self.function_strings[20], self.form_InductV),
                (self.function_strings[21], self.form_InductV2),
                (self.function_strings[22], self.form_InductV3),
                (self.function_strings[23], self.form_Power4),
                (self.function_strings[24], self.form_Power),
                (self.function_strings[25], self.form_Power3),
                (self.function_strings[26], self.form_Power2),
                (self.function_strings[27], self.form_Resistance3),
                (self.function_strings[28], self.form_Resistance4),
                (self.function_strings[29], self.form_Resistance),
                (self.function_strings[30], self.form_Resistance2),
                (self.function_strings[31], self.form_ResistA2),
                (self.function_strings[32], self.form_ResistA),
                (self.function_strings[33], self.form_ResistA5),
                (self.function_strings[34], self.form_ResistA3),
                (self.function_strings[35], self.form_ResistA4),
                (self.function_strings[36], self.form_ResistV),
                (self.function_strings[37], self.form_ResistV2),
                (self.function_strings[38], self.form_ResistV3),
                (self.function_strings[39], self.form_TAmps),
                (self.function_strings[40], self.form_TAmps5),
                (self.function_strings[41], self.form_TAmps2),
                (self.function_strings[42], self.form_TAmps3),
                (self.function_strings[43], self.form_TAmps4),
                (self.function_strings[44], self.form_TVolts3),
                (self.function_strings[45], self.form_TVolts2),
                (self.function_strings[46], self.form_TVolts),
                (self.function_strings[47], self.form_VoltA2),
                (self.function_strings[48], self.form_VoltA3),
                (self.function_strings[49], self.form_VoltA),
                (self.function_strings[50], self.form_VoltA4),
                (self.function_strings[51], self.form_VoltA5),
                (self.function_strings[52], self.form_Watts4),
                (self.function_strings[53], self.form_Watts2),
                (self.function_strings[54], self.form_Watts),
                (self.function_strings[55], self.form_Watts5),
                (self.function_strings[56], self.form_Watts3),
            ]
        )
#}}}_________________________________________________________________________________________
         
#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[1]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[2]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[3]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Volt Amps: ')
                    ]
            ),
            self.function_strings[4]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[5]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[6]:OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Inductor Rating: ')
                    ]
            ),
            self.function_strings[7]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[8]:OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[9]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[10]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            self.function_strings[11]:OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Volts: ')
                    ]
            ),
            self.function_strings[12]:OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[13]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[14]:OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[15]:OrderedDict(
                    [
                            ('number_input', 'Inducive Reactance: '),
                            ('number_input2', 'Frequency: ')
                    ]
            ),
            self.function_strings[16]:OrderedDict(
                    [
                            ('number_input', 'Inductor Amps: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[17]:OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amp: ')
                    ]
            ),
            self.function_strings[18]:OrderedDict(
                    [
                            ('number_Input', 'Inductor Volts: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            self.function_strings[19] : OrderedDict(
                [
                    ('number_input', 'Volt Amps: '),
                    ('number_input2', 'Watts: ')
                ]
            ),
            self.function_strings[20] : OrderedDict(
                [
                    ('number_input', "Inductor VAR's: "),
                    ('number_input2', 'Iductive Reactance: ')
                ]
            ),
            self.function_strings[21] : OrderedDict(
                [
                    ('number_input', 'Inductor Amps: '),
                    ('number_input2', 'Inductive Reactance: ')
                ]
            ),
            self.function_strings[22] : OrderedDict(
                [
                    ('number_input', "Inductor VAR's: "),
                    ('number_input2', 'Inductor Amps: ')
                ]
            ),
            self.function_strings[23] : OrderedDict(
                [
                    ('number_input', 'CoSine: '),
                    ('number_input2', 'Theta Angle: ')
                ]
            ),
            self.function_strings[24]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[25]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[26]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Volt Amps: ')
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
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[31]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[32]: OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[33]:OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Power Factor: ')
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
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            self.function_strings[36]: OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[37]: OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[38]: OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[39]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            self.function_strings[40]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[41] : OrderedDict(
                [
                    ('number_input', 'Total Volts: '),
                    ('number_input2', 'Impedance: ')
                ]
            ),
            self.function_strings[42]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Volts: ')
                    ]
            ),
            self.function_strings[43]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[44] : OrderedDict(
                [
                    ('number_input', 'Total Amps: '),
                    ('number_input2', 'Impedance: ')
                ]
            ),
            self.function_strings[45]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[46]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[47]:OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Impedance: ')
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
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[50]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            self.function_strings[51]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[52]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
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
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[55]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            self.function_strings[56]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{              #, self.form_Impedance),
                '' : '1 / ((1 / Resistance^2) + (1 / Inductive Reactance^2))'
            },
            self.function_strings[2]:{                      #, self.form_Impedance2),
                '' : 'Total Volts / Total Amps'
            },
            self.function_strings[3]:{                       #, self.form_Impedance3),
                '' : 'Total Volts / Volt Amps'
            },
            self.function_strings[4]:{                        #, self.form_Impedance4),
                '' : 'Volt Amps / Total Amps'
            },
            self.function_strings[5]:{                     #, self.form_Impedance5),
                '' : 'Resistance * Power Factor'
            },
            self.function_strings[6]:{         #, self.form_InductRe3),
                '' : '2 * 3.14 * Frequency * Inductor Rating'
            },
            self.function_strings[7]:{              #, self.form_InductRe4),
                '' : '1 / (1 / Impedance^2 - Resistacne^2)'
            },
            self.function_strings[8]:{      #, self.form_InductRe2),
                '' : "Inudctor VAR's / Inductor Amps^2"
            },
            self.function_strings[9]:{      #, self.form_InductRe5),
                '' : 'Inductor Volts / Inductor Amps'
            },
            self.function_strings[10]:{     #, self.form_InductRe),
                '' : "Inductor Volts^2 / Inductor VAR's"
            },
            self.function_strings[11]:{           #, self.form_InductA3),
                '' : "Inductor VAR's / Inductor Volts"
            },
            self.function_strings[12]:{      #, self.form_InductA4),
                '' : "sqrt(Inductor VAR's / Inductive Reactance)"
            },
            self.function_strings[13]:{      #, self.form_InductA2),
                '' : 'Inductor Volts / Inductive Reactance'
            },
            self.function_strings[14]:{                #, self.form_InductA), 
                '' : 'sqrt(Total Amps^2 - Resistor Amps^2)'
            },
            self.function_strings[15]:{         #, self.form_InductorRating),
                '' : 'Inductive Reactance / (2 * 3.14 * Frequency)'
            },
            self.function_strings[16]:{      #, self.form_InductorV),
                '' : 'Inductor Amps^2 * Inductive Reactance'
            },
            self.function_strings[17]:{           #, self.form_InductorV3),
                '' : 'Inductor Volts * Inductor Amps'
            },
            self.function_strings[18]:{     #, self.form_InductorV4),
                '' : 'Inductor Volts^2 / Inductive Reactance'
            },
            self.function_strings[19]:{                        #, self.form_InductorV2),
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
            self.function_strings[20]:{     #, self.form_InductV),
                '' : "Inductor VAR's * Inductive Reactance"
            },
            self.function_strings[21]:{      #, self.form_InductV2),
                '' : 'sqrt(Inductor Amps * Inductive Reactance)'
            },
            self.function_strings[22]:{           #, self.form_InductV3),
                '' : "Inductor VAR's / Inductor Amps"
            },
            self.function_strings[23]:{                       #, self.form_Power4),
                '' : 'CoSine * Theta Angle'
            },
            self.function_strings[24]:{                     #, self.form_Power),
                '' : 'Impedance / Resistance'
            },
            self.function_strings[25]:{                 #, self.form_Power3),
                '' : 'Resistor Amps / Total Amps'
            },
            self.function_strings[26]:{                          #, self.form_Power2),
                '' : 'Watts / Volt Amps'
            },
            self.function_strings[27]:{              #, self.form_Resistance3),
                '' : '1 / sqrt(Impedance^2 - Inductive Reactance^2)'
            },
            self.function_strings[28]:{                     #, self.form_Resistance4),
                '' : 'Impedance / Power Factor'
            },
            self.function_strings[29]:{               #, self.form_Resistance),
                '' : 'Resistor Volts / Resistor Amps'
            },
            self.function_strings[30]:{                        #, self.form_Resistance2),
                '' : 'Watts / Resistor Amps^2'
            },
            self.function_strings[31]:{               #, self.form_ResistA2),
                '' : 'Resistor Volts / Resistance'
            },
            self.function_strings[32]:{                #, self.form_ResistA),
                '' : 'sqrt(Total Amps^2 - Inductor Amps^2)'
            },
            self.function_strings[33]:{                 #, self.form_ResistA5),
                '' : 'Total Amps * Power Factor'
            },
            self.function_strings[34]:{                        #, self.form_ResistA3),
                '' : 'sqrt(Watts / Resistance)'
            },
            self.function_strings[35]:{                    #, self.form_ResistA4),
                '' : 'Watts / Resistor Volts'
            },
            self.function_strings[36]:{               #, self.form_ResistV),
                '' : 'Resistor Amps * Resistance'
            },
            self.function_strings[37]:{                       #, self.form_ResistV2),
                '' : 'sqrt(Watts * Resistance)'
            },
            self.function_strings[38]:{                    #, self.form_ResistV3),
                '' : 'Watts / Resistor Amps^2'
            },
            self.function_strings[39]:{                #, self.form_TAmps),
                '' : 'sqrt(Resistor Amps^2 + Inductor Amps^2)'
            },
            self.function_strings[40]:{                 #, self.form_TAmps5),
                '' : 'Resistor Amps / Power Factor'
            },
            self.function_strings[41]:{                      #, self.form_TAmps2),
                '' : 'Total Volts / Impedance'
            },
            self.function_strings[42]:{                      #, self.form_TAmps3),
                '' : 'Volt Amps / Total Volts'
            },
            self.function_strings[43]:{                        #, self.form_TAmps4),
                '' : 'sqrt(Volt Amps / Impedance)'
            },
            self.function_strings[44]:{                      #, self.form_TVolts3),
                '' : 'Total Amps * Impedance'
            },
            self.function_strings[45]:{                       #, self.form_TVolts2),
                '' : 'sqrt(Volt Amps * Impedance)'
            },
            self.function_strings[46]:{                      #, self.form_TVolts),
                '' : 'Volt Amps / Total Amps'
            },
            self.function_strings[47]:{                        #, self.form_VoltA2),
                '' : 'Total Amps^2 * Impedance'
            },
            self.function_strings[48]:{                       #, self.form_VoltA3),
                '' : 'Total Volts^2 / Impedance'
            },
            self.function_strings[49]:{                      #, self.form_VoltA),
                '' : 'Total Volts * Total Amps'
            },
            self.function_strings[50]:{                        #, self.form_VoltA4),
                '' : "sqrt(Watts^2 + Inductor VAR's^2)"
            },
            self.function_strings[51]:{                          #, self.form_VoltA5),
                '' : 'Watts / Power Factor'
            },
            self.function_strings[52]:{                        #, self.form_Watts4),
                '' : 'Resistor Amps^2 * Resistance'
            },
            self.function_strings[53]:{                       #, self.form_Watts2),
                '' : 'sqrt(Resistor Volts^2 / Resistance^2)'
            },
            self.function_strings[54]:{                    #, self.form_Watts),
                '' : 'Resistor Volts * Resistor Amps'
            },
            self.function_strings[55]:{                        #, self.form_Watts5),
                '' : "Volt Amps * Inductor VAR's"
            },
            self.function_strings[56]:{                          #, self.form_Watts3),
                '' : 'Volt Amps^2 / Power Factor'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def form_Impedance(self):
        title = self.function_strings[1]
        arg1 = 'Enter Resistance'
        arg2 = 'Enter Inductive Reactance'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = 1/((1/argsIn[0]**2) + (1/argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance2(self):
        title = self.function_strings[2]
        arg1 = 'Enter Total Volts'
        arg2 = 'Enter Total Amps'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance3(self):
        title = self.function_strings[3]
        arg1 = 'Enter Total Volts'
        arg2 = 'Enter Volt Amps'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance4(self):
        title = self.function_strings[4]
        arg1 = 'Enter Volt Amps'
        arg2 = 'Enter Total Amps'
        argsOut = [title, arg1, args2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance5(self):
        title = self.function_strings[5]
        arg1 = 'Enter Resistance'
        arg2 = 'Enter Power Factor'
        argsOut = [title, arg1, arg2]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_InductRe(self):
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe2(self):
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe3(self):
        result = 2*3.14*argsIn[0]*argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe4(self):
        result = 1/(1/(argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe5(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductive Reactance'))

    def form_InductA(self):
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))
        except(Exception):
            return (self.error_msg, '')

    def form_InductA2(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_InductA3(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_InductA4(self):
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Amp'))

    def form_InductorRating(self):
        result = argsIn[0] / (2*3.14*argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Rating'))

    def form_InductorV(self):
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Inductor VAR"))

    def form_InductorV2(self):
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))
        except(Exception):
            return (self.error_msg, '')

    def form_InductorV3(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_InductorV4(self):
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor VAR'))

    def form_InductV(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_InductV2(self):
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_InductV3(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Inductor Volt'))

    def form_Power(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Power2(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Power3(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Power4(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Resistance(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_Resistance2(self):
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_Resistance3(self):
        result = 1/sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))
    
    def form_Resistance4(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_ResistA(self):
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))
        except(Exception):
            return (self.error_msg, '')

    def form_ResistA2(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA3(self):
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA4(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA5(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_ResistV(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_ResistV2(self):
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_ResistV3(self):
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_ResistV4(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_TAmps(self):
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_TAmps2(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_TAmps3(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_TAmps4(self):
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_TAmps5(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_TVolts(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_TVolts2(self):
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_TVolts3(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))


    def form_VoltA6(self):
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VoltA(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VoltA2(self):
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VoltA3(self):
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VoltA4(self):
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VoltA5(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_Watts(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts2(self):
        result = sqrt((argsIn[0]**2) / (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts3(self):
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts4(self):
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts5(self):
        result = argsIn[0] * argsIn[1] 
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))
#}}}_________________________________________________________________________________________

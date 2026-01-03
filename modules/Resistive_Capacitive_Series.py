#!/usr/bin/env python3
#
# Resistive_Capacitive_Series.py
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


from .FormulaBase import * 

class Resistive_Capacitive_Series(FormulaBase):
    def __init__(self, name):
        super(Resistive_Capacitive_Series, self).__init__(name)
        self.name = name
        self.error_msg = "Can not be a negative square root"
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            # 55 Formula Strings
            1 : "Capacitive Reactance using Capacitor VAR's and Capacitor Amps",
            2 : 'Capacitive Reactance using Capacitor Volts and Capacitor Amps',
            3 : "Capacitive Reactance using Capacitor Volts and Capacitor VAR's",
            4 : 'Capacitive Reactance using Frequency and Capacitor Rating',
            5 : 'Capacitive Reactance using Impedance and Resistance',
            6 : "Capacitor Amps using Capacitor VAR's and Capacitor Volts",
            7 : "Capacitor Amps using Capacitor VAR's and Capacitive Reactance",
            8 : 'Capacitor Amps using Capacitor Volts and Capacitive Reactance',
            9 : 'Capacitor Rating using Frequency and Capacitive Reactance',
            10 : "Capacitor VAR's using Volt Amps and Watts",
            11 : "Capacitor VAR's using Capacitor Amps and Capacitive Reactance",
            12 : "Capacitor VAR's using Capacitor Volts and Capacitive Reactance",
            13 : "Capacitor VAR's using Capacitor Volts and Capacitor Amps",
            14 : 'Capacitor Volts using Capacitor Amps and Capacitive Reactance',
            15 : 'Capacitor Volts using Total Volts and Resistor Volts',
            16 : "Capacitor Volts using Capacitor VAR's and Capacitive Reactance",
            17 : "Capacitor Volts using Capacitor VAR's and Capacitor Amps",
            18 : 'Impedance using Resistance and Capacitive Reactance',
            19 : 'Impedance using Total Volts and Total Amps',
            20 : 'Impedance using Volt Amps and Total Amps',
            21 : 'Impedance using Resistance and Power Factor',
            22 : 'Impedance using Total Volts and Volt Amps',
            23 : 'Power Factor using Resistance and Impedance',
            24 : 'Power Factor using Watts and Volt Amps',
            25 : 'Power Factor using Resistor Volts and Total Volts',
            26 : 'Power Factor using CoSine and Theta Angle',
            27 : 'Resistance using Watts and Resistor Amps',
            28 : 'Resistance using Impedance and Capacitive Reactance',
            29 : 'Resistance using Resistor Volts and Watts',
            30 : 'Resistance using Impedance and Power Factor',
            31 : 'Resistance using Resistor Volts and Resistor Amps',
            32 : 'Resistor Amps using Resistor Volts and Resistance',
            33 : 'Resistor Amps using Watts and Resistor Volts',
            34 : 'Resistor Amps using Watts and Resistance',
            35 : 'Resistor Volts using Total Volts and Capacitor Volts',
            36 : 'Resistor Volts using Total Volts and Power Factor',
            37 : 'Resistor Volts using Resistor Amps and Resistance',
            38 : 'Resistor Volts using Watts and Resistance',
            39 : 'Resistor Volts using Watts and Resistor Amps',
            40 : 'Total Amps using Total Volts and Impedance',
            41 : 'Total Amps using Volt Amps and Total Volts',
            42 : 'Total Volts using Resistor Volts and Capacitor Volts',
            43 : 'Total Volts using Total Amps and Impedance',
            44 : 'Total Volts using Volt Amps and Total Amps',
            45 : 'Total Volts using Resistor Volts and Power Factor',
            46 : 'Volt Amps using Total Volts and Total Amps',
            47 : 'Volt Amps using Total Amps and Impedance',
            48 : 'Volt Amps using Total Volts and Impedance',
            49 : "Volt Amps using Watts and Capacitor VAR's",
            50 : 'Volt Amps using Watts and Power Factor',
            51 : 'Watts using Resistor Volts and Resistor Amps',
            52 : "Watts using Volt Amps and Capacitor VAR's",
            53 : 'Watts using Resistor Volts and Resistance',
            54 : 'Watts using Resistor Amps and Resistance',
            55 : 'Watts using Volt Amps and Power Factor',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_CReact2),
                (self.function_strings[2], self.form_CReact),
                (self.function_strings[3], self.form_CReact4),
                (self.function_strings[4], self.form_CReact5),
                (self.function_strings[5], self.form_CReact3),
                (self.function_strings[6], self.form_CAmps),
                (self.function_strings[7], self.form_CAmps2),
                (self.function_strings[8], self.form_CAmps3),
                (self.function_strings[9], self.form_CRate),
                (self.function_strings[10], self.form_CVAR), 
                (self.function_strings[11], self.form_CVAR3),
                (self.function_strings[12], self.form_CVAR4),
                (self.function_strings[13], self.form_CVAR2),
                (self.function_strings[14], self.form_CVolts),
                (self.function_strings[15], self.form_CVolts2),
                (self.function_strings[16], self.form_CVolts3),
                (self.function_strings[17], self.form_CVolts4),
                (self.function_strings[18], self.form_Impedance),
                (self.function_strings[19], self.form_Impedance2),
                (self.function_strings[20], self.form_Impedance3),
                (self.function_strings[21], self.form_Impedance4),
                (self.function_strings[22], self.form_Impedance5),
                (self.function_strings[23], self.form_Power),
                (self.function_strings[24], self.form_Power2),
                (self.function_strings[25], self.form_Power3),
                (self.function_strings[26], self.form_Power4),
                (self.function_strings[27], self.form_Resistance),
                (self.function_strings[28], self.form_Resistance2),
                (self.function_strings[29], self.form_Resistance3),
                (self.function_strings[30], self.form_Resistance4),
                (self.function_strings[31], self.form_Resistance5),
                (self.function_strings[32], self.form_RAmps),
                (self.function_strings[33], self.form_RAmps2),
                (self.function_strings[34], self.form_RAmps3),
                (self.function_strings[35], self.form_RVolts),
                (self.function_strings[36], self.form_RVolts2),
                (self.function_strings[37], self.form_RVolts3),
                (self.function_strings[38], self.form_RVolts4),
                (self.function_strings[39], self.form_RVolts5),
                (self.function_strings[40], self.form_TAmps),
                (self.function_strings[41], self.form_TAmps2),
                (self.function_strings[42], self.form_TVolts),
                (self.function_strings[43], self.form_TVolts2),
                (self.function_strings[44], self.form_TVolts3),
                (self.function_strings[45], self.form_TVolts4),
                (self.function_strings[46], self.form_VAmps),
                (self.function_strings[47], self.form_VAmps2),
                (self.function_strings[48], self.form_VAmps3),
                (self.function_strings[49], self.form_VAmps4),
                (self.function_strings[50], self.form_VAmps5),
                (self.function_strings[51], self.form_Watts),
                (self.function_strings[52], self.form_Watts2),
                (self.function_strings[53], self.form_Watts3),
                (self.function_strings[54], self.form_Watts4),
                (self.function_strings[55], self.form_Watts5),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[2]:OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', 'Capacitor Amps: ')
                    ]
            ),
            self.function_strings[1]:OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitor Amps: ')
                    ]
            ),
            self.function_strings[5]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[3]:OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', "Capacitor VAR's: ")
                    ]
            ),
            self.function_strings[4]:OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Capacitor Rating: ')
                    ]
            ),
            self.function_strings[6]:OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitor Volts: ')
                    ]
            ),
            self.function_strings[7]:OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[8]:OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[9]:OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[10]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            self.function_strings[11]:OrderedDict(
                    [
                            ('number_input', 'Capacitor Amps: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[12]:OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[13]:OrderedDict(
                    [
                            ('number_input' , 'Capacitor Volts: '),
                            ('number_input2' , 'Capacitor Amps: ')
                    ]
            ),
            self.function_strings[14]:OrderedDict(
                    [
                            ('number_input', 'Capacitor Amps: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[15]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            self.function_strings[16]:OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[17]:OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitor Amps: ')
                    ]
            ),
            self.function_strings[18]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[19]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[20]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[21]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[22]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Volt Amps: ')
                    ]
            ),
            self.function_strings[23]:OrderedDict(
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
                            ('number_input', 'CoSine: '),
                            ('number_input2', 'Theta Angle: ')
                    ]
            ),
            self.function_strings[27]:OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[28]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            self.function_strings[29]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            self.function_strings[30]:OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[31]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
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
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Capacitor Volts: ')
                    ]
            ),
            self.function_strings[36]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[37]:OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
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
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[42]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Capacitor Volts: ')
                    ]
            ),
            self.function_strings[43]:OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            self.function_strings[44]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[45]:OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Power Factor: ')
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
            self.function_strings[46]:OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            self.function_strings[47]:OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            "Volt Amps using Watts and Inductor VAR's":OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', "Inductor VAR's: ")
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
                            ('number_input2', "Capacitor VAR's: ")
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
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            self.function_strings[52]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', "Capacitor VAR's: ")
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
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            self.function_strings[55]:OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            self.function_strings[24]:OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Volt Amps (input): ")
                ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{                   #self.form_CReact2),
                '' : "Capacitor VAR's / Capacitor Amps^2"
            },
            self.function_strings[2]:{                   #self.form_CReact),
                '' : 'Capacitor Volts / Capacitor Amps'
            },
            self.function_strings[3]:{                  #self.form_CReact4),
                '' : "Capacitor Volts^2 / Capacitor VAR's"
            },
            self.function_strings[4]:{                       #self.form_CReact5),
                '' : '1 / (2 * 3.14 * Frequency * Capacitor Rating)'
            },
            self.function_strings[5]:{                             #self.form_CReact3),
                '' : 'sqrt(Impedance^2 - Resistance^2)'
            },
            self.function_strings[6]:{                        #self.form_CAmps),
                '' : "Capacitor VAR's / Capacitor Volts"
            },
            self.function_strings[7]:{                   #self.form_CAmps2),
                '' : "sqrt(Capacitor VAR's / Capacitive Reactance)"
            },
            self.function_strings[8]:{                   #self.form_CAmps3),
                '' : 'Capacitor Volts^2 * Capacitive Reactance'
            },
            self.function_strings[9]:{                       #self.form_CRate),
                '' : '1 / (2 * 3.14 Frequency * Capacitive Reactance)'
            },
            self.function_strings[10]:{                                       #self.form_CVAR), 
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
            self.function_strings[11]:{                   #self.form_CVAR3),
                '' : 'Capacitor Amps^2 * Capacitive Reactance'
            },
            self.function_strings[12]:{                  #self.form_CVAR4),
                '' : 'Capacitor Volts^2 / Capacitive Reactance'
            },
            self.function_strings[13]:{                        #self.form_CVAR2),
                '' : 'Capacitor Volts * Capacitor Amps'
            },
            self.function_strings[14]:{                   #self.form_CVolts),
                '' : 'Capacitor Amps * Capacitive Reactance'
            },
            self.function_strings[15]:{                            #self.form_CVolts2),
                '' : 'sqrt(Total Volts^2 - Resistor Volts^2)'
            },
            self.function_strings[16]:{                  #self.form_CVolts3),
                '' : "sqrt(Capacitor VAR's * Capacitive Reactance)"
            },
            self.function_strings[17]:{                        #self.form_CVolts4),
                '' : "Capacitor VAR's / Capacitor Amps"
            },
            self.function_strings[18]:{                             #self.form_Impedance),
                '' : 'sqrt(Impedance^2 + Capacitive Reactance^2)'
            },
            self.function_strings[19]:{                                      #self.form_Impedance2),
                '' : 'Total Volts / Total Amps'
            },
            self.function_strings[20]:{                                        #self.form_Impedance3),
                '' : 'Volt Amps / Total Amps^2'
            },
            self.function_strings[21]:{                                     #self.form_Impedance4),
                '' : 'Resistance / Power Factor'
            },
            self.function_strings[22]:{                                       #self.form_Impedance5),
                '' : 'Total Volts^2 / Volt Amps'
            },
            self.function_strings[23]:{                                     #self.form_Power),
                '' : 'Resistance / Impedance'
            },
            self.function_strings[24]:{                                          #self.form_Power2),
                '' : 'Watts / Volt Amps'
            },
            self.function_strings[25]:{                               #self.form_Power3),
                '' : 'Resistor Volts / Total Volts'
            },
            self.function_strings[26]:{                                       #self.form_Power4),
                '' : 'CoSine * Theta Angle'
            },
            self.function_strings[27]:{                                        #self.form_Resistance),
                '' : 'Watts / Resistor Amps^2'
            },
            self.function_strings[28]:{                             #self.form_Resistance2),
                '' : 'sqrt(Impedance^2 - Capacitive Reactance^2)'
            },
            self.function_strings[29]:{                                       #self.form_Resistance3),
                '' : 'Resistor Volts^2 / Watts'
            },
            self.function_strings[30]:{                                     #self.form_Resistance4),
                '' : 'Impedance * Power Factor'
            },
            self.function_strings[31]:{                               #self.form_Resistance5),
                '' : 'Resistor Volts / Resistor Amps'
            },
            self.function_strings[32]:{                               #self.form_RAmps),
                '' : 'Resistor Volts / Resistance'
            },
            self.function_strings[33]:{                                    #self.form_RAmps2),
                '' : 'Watts / Resistor Volts'
            },
            self.function_strings[34]:{                                        #self.form_RAmps3),
                '' : 'sqrt(Watts / Resistance)'
            },
            self.function_strings[35]:{                            #self.form_RVolts),
                '' : 'Total Volts * Capacitor Volts'
            },
            self.function_strings[36]:{                               #self.form_RVolts2),
                '' : 'sqrt(Total Volts * Power Factor)'
            },
            self.function_strings[37]:{                               #self.form_RVolts3),
                '' : 'Resistor Amps / Resistance'
            },
            self.function_strings[38]:{                                       #self.form_RVolts4),
                '' : 'sqrt(Watts^2 - Resistance^2)'
            },
            self.function_strings[39]:{                                    #self.form_RVolts5),
                '' : 'Watts * Resistor Amps'
            },
            self.function_strings[40]:{                                      #self.form_TAmps),
                '' : 'Total Volts / Impedance'
            },
            self.function_strings[41]:{                                      #self.form_TAmps2),
                '' : 'Volt Amps / Total Volts'
            },
            self.function_strings[42]:{                            #self.form_TVolts),
                '' : 'sqrt(Resistor Volts^2 + Capacitor Volts^2)'
            },
            self.function_strings[43]:{                                      #self.form_TVolts2),
                '' : 'Total Amps * Impedance'
            },
            self.function_strings[44]:{                                      #self.form_TVolts3),
                '' : 'Volt Amps / Total Amps'
            },
            self.function_strings[45]:{                               #self.form_TVolts4),
                '' : 'Resistor Volts / Power Factor'
            },
            self.function_strings[46]:{                                      #self.form_VAmps),
                '' : 'Total Volts * Total Amps'
            },
            self.function_strings[47]:{                                        #self.form_VAmps2),
                '' : 'Total Amps^2 * Impedance'
            },
            self.function_strings[48]:{                                       #self.form_VAmps3),
                '' : 'Total Volts^2 / Impedance'
            },
            self.function_strings[49]:{                                       #self.form_VAmps4),
                '' : "sqrt(Watts^2 + Capacitor VAR's^2)"
            },
            self.function_strings[50]:{                                          #self.form_VAmps5),
                '' : 'Watts / Power Factor'
            },
            self.function_strings[51]:{                                    #self.form_Watts),
                '' : 'Resistor Volts * Resistor Amps'
            },
            self.function_strings[52]:{                                       #self.form_Watts2),
                '' : "sqrt(Volt Amps^2 - Capacitor VAR's^2)"
            },
            self.function_strings[53]:{                                       #self.form_Watts3),
                '' : 'Resistor Volts^2 / Resistance'
            },
            self.function_strings[54]:{                                        #self.form_Watts4),
                '' : 'Resistor Amps^2 * Resistance'
            },
            self.function_strings[55]:{                                          #self.form_Watts5),
                '' : 'Volt Amps * Power Factor'
            },
        }

#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________
    def form_TVolts(self):
        title = self.function_strings[42]
        rv = "Enter Resistor Volts"
        cv = "Enter Capacitor Volts"
        argsOut = [title, rv, cv]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_TVolts2(self):
        title = self.function_strings[43]
        ta = "Enter Total Amps"
        i = "Enter Impedance"
        argsOut = [title, ta, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_TVolts3(self):
        title = self.function_strings[44]
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_TVolts4(self):
        title = self.function_strings[45]
        rv = "Enter Resistor Volts"
        pw = "Enter Power Factor"
        argsOut = [title, rv, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt'))

    def form_Power(self):
        title = self.function_strings[23]
        r = "Enter Resistance"
        i = "Enter Impedance"
        argsOut = [title, r, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Power2(self):
        title = self.function_strings[24]
        w = "Enter Watts"
        va = "Enter Volt Amps"
        argsOut = [title, w, va]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Power3(self):
        title = self.function_strings[25]
        rv = "Enter Resistor Volts"
        tv = "Enter Total Volts"
        argsOut = [title, rv, tv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_Power4(self):
        title = self.function_strings[26]
        coS = "Enter CoSine"
        theta = "Enter Theta Angle"
        argsOut = [title, coS, theta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor'))

    def form_TAmps(self):
        title = self.function_strings[40]
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_TAmps2(self):
        title = self.function_strings[41]
        va = "Enter Volt Amps"
        tv = "Enter Total Volts"
        argsOut = [title, va, tv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def form_VAmps(self):
        title = self.function_strings[46]
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VAmps2(self):
        title = self.function_strings[47]
        ta = "Enter Total Amps"
        i = "Enter Impedance"
        argsOut = [title, ta, i]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VAmps3(self):
        title = self.function_strings[48]
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VAmps4(self):
        title = self.function_strings[49]
        w = "Enter Watts"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, w, cvar]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_VAmps5(self):
        title = self.function_strings[50]
        w = "Enter Watts"
        pw = "Enter Power Factor"
        argsOut = [title, w, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))

    def form_Impedance(self):
        title = self.function_strings[18]
        r = "Enter Resistance"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, r, cr]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance2(self):
        title = self.function_strings[19]
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance3(self):
        title = self.function_strings[20]
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance4(self):
        title = self.function_strings[21]
        r = "Enter Resistance"
        pw = "Enter Power Factor"
        argsOut = [title, r, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_Impedance5(self):
        title = self.function_strings[22]
        tv = "Enter Total Volts"
        va = "Enter Volt Amps"
        argsOut = [title, tv, va]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def form_RAmps(self):
        title = self.function_strings[32]
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_RAmps2(self):
        title = self.function_strings[33]
        w = "Enter Watts"
        rv = "Enter Resistor Volts"
        argsOut = [title, w, rv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_RAmps3(self):
        title = self.function_strings[34]
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))

    def form_Watts(self):
        title = self.function_strings[51]
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts2(self):
        title = self.function_strings[52]
        va = "Enter Volt Amps"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, va, cvar]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Watt'))
        except(Exception):
            return (self.error_msg, '')

    def form_Watts3(self):
        title = self.function_strings[53]
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts4(self):
        title = self.function_strings[54]
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_Watts5(self):
        title = self.function_strings[55]
        va = "Enter Volt Amps"
        pw = "Enter Power Factor"
        argsOut = [title, va, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt'))

    def form_CAmps(self):
        title = self.function_strings[6]
        cvar = "Enter Capacitor VAR's"
        cv = "Enter Capacitor Volts"
        argsOut = [title, cvar, cv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))
        
    def form_CAmps2(self): 
        title = self.function_strings[7]
        cvar = "Enter Capacitor VAR's"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, cvar, creact]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_CAmps3(self): 
        title = self.function_strings[8]
        cv = "Enter Capacitor Volts"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, cv, creact]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Amp'))

    def form_CVAR (self): 
        title = self.function_strings[10]
        va = "Enter Volt Amps"
        w = "Enter Watts"
        argsOut = [title, va, w]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, "Capacitor VAR'"))
        except(Exception):
            return (self.error_msg, '')

    def form_CVAR2 (self):
        title = self.function_strings[13]
        cv = "Enter Capacitor Volts"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cv, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR3 (self):
        title = self.function_strings[11]
        ca = "Enter Capacitor Amps"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, ca, creact]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR4 (self):
        title = self.function_strings[12]
        cv = "Enter Capacitor Volts"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, cv, creact]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Capacitor VAR'"))

    def form_RVolts (self):
        title = self.function_strings[35]
        tv = "Enter Total Volts"
        cv = "Enter Capacitor Volts"
        argsOut = [title, tv, cv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts2 (self):
        title = self.function_strings[36]
        tv = "Enter Total Volts"
        pwf = "Enter Power Factor"
        argsOut = [title, tv, pwf]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts3 (self):
        title = self.function_strings[37]
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts4 (self):
        title = self.function_strings[38]
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))
        except(Exception):
            return (self.error_msg, '')

    def form_RVolts5 (self):
        title = self.function_strings[39]
        w = "Enter Watts"
        ra = "Enter Resistor Amps"
        argsOut = [title, w, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def form_Resistance (self):
        title = self.function_strings[27]
        w = "Enter Watts"
        ra = "Enter Resistor Amps"
        argsOut = [title, w, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_Resistance2 (self):
        title = self.function_strings[28]
        i = "Enter Impedance"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, i, creact]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Resistance'))
        except(Exception):
            return (self.error_msg, '')

    def form_Resistance3 (self):
        title = self.function_strings[29]
        rv = "Enter Resistor Volts"
        w = "Enter Watts"
        argsOut = [title, rv, w]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_Resistance4 (self):
        title = self.function_strings[30]
        imp = "Enter Impedance"
        pwf = "Enter Power Factor"
        argsOut = [title, imp, pwf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_Resistance5 (self):
        title = self.function_strings[31]
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def form_CReact(self):
        title = self.function_strings[2]
        cv = "Enter Capacitor Volts"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cv, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact2(self):
        title = self.function_strings[1]
        cvar = "Enter Capacitor VAR's"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cvar, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact3 (self):
        title = self.function_strings[5]
        imp = "Enter Impedance"
        r = "Enter Resistance"
        argsOut = [title, imp, r]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))
        except(Exception):
            return (self.error_msg, '')

    def form_CReact4 (self):
        title = self.function_strings[3]
        cv = "Enter Capacitor Volts"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, cv, cvar]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact5 (self):
        title = self.function_strings[4]
        freq = "Enter Frequency"
        crate = "Enter Capacitor Rating"
        argsOut = [title, freq, crate]
        argsIn = self.prompt(argsOut)
        result = 1 / (2 * 3.14 * argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def form_CRate (self):
        title = self.function_strings[9]
        freq = "Enter Frequency"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, freq, creact]
        argsIn = self.prompt(argsOut)
        result = 1 / (2 * 3.14 * argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Rating'))

    def form_CVolts (self):
        title = self.function_strings[14]
        ca = "Enter Capacitor Amps"
        creat = "Enter Capacitive Reactance"
        argsOut = [title, ca, creact]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts2 (self):
        title = self.function_strings[15]
        tv = "Enter Total Volts"
        rv = "Enter Resistor Volts"
        argsOut = [title, tv, rv]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))
        except(Exception):
            return (self.error_msg, '')

    def form_CVolts3 (self):
        title = self.function_strings[16]
        cvar = "Enter Capacitor VAR's"
        creact = "Enter Capacititve Reactance"
        argsOut = [title, cvar, creact]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts4 (self):
        title = self.function_strings[17]
        cvar = "Enter Capacitor VAR's"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cvar, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))
#}}}_________________________________________________________________________________________


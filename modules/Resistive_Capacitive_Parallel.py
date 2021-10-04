#!/usr/bin/python
#
# Resistive_Capacitive_Parallel.py
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

class Resistive_Capacitive_Parallel(FormulaBase):
    def __init__(self, name):
        super(Resistive_Capacitive_Parallel, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Total Amps using Resistor Amps and Capacitor Amps',
            2 : 'Total Amps using Total Volts and Impedance',
            3 : 'Total Amps using Volt Amps and Total Volts',
            4 : 'Total Amps using Resistor Amps and Power Factor',
            5 : 'Total Amps using Volt Amps and Impedance',
            6 : 'Power Factor using Impedance and Resistance',
            7 : 'Power Factor using Resistor Amps and Total Amps',
            8 : 'Power Factor using Watts and Volt Amps',
            9 : 'Power Factor using CoSine and Theta Angle',
            10 : 'Watts using Resistor Volts and Resistor Amps',
            11 : 'Watts using Volt Amps and Power Factor',
            12 : "Watts using Volt Amps and Capacitor VAR's",
            13 : 'Watts using Resistor Volts and Resistance',
            14 : 'Watts using Resistor Amps and Resistance',
            15 : 'Impedance using Resistance and Capacitive Reactance',
            16 : 'Impedance using Volt Amps and Total Amps',
            17 : 'Impedance using Total Volts and Total Amps',
            18 : 'Impedance using Total Volts and Volt Amps',
            19 : 'Impedance using Resistance and Power Factor',
            20 : 'Resistor Amps using Total Amps and Capacitor Amps',
            21 : 'Resistor Amps using Resistor Volts and Resistance',
            22 : 'Resistor Amps using Watts and Resistor Volts',
            23 : 'Resistor Amps using Watts and Resistance',
            24 : 'Resistor Amps using Power Factor and Total Amps',
            25 : 'Total Volts using Volt Amps and Total Amps',
            26 : 'Total Volts using Volt Amps and Impedance',
            27 : 'Total Volts using Total Amps and Impedance',
            28 : 'Volt Amps using Total Volts and Total Amps',
            29 : 'Volt Amps using Total Amps and Impedance',
            30 : 'Volt Amps using Total Volts and Impedance',
            31 : "Volt Amps using Watts and Capacitor VAR's",
            32 : 'Volt Amps using Watts and Power Factor',
            33 : 'Resistor Volts using Resistor Amps and Resistance',
            34 : 'Resistor Volts using Watts and Resistance',
            35 : 'Resistor Volts using Watts and Resistor Amps',
            36 : 'Capacitor Volts using Capacitor Amps and Capacitive Reactance',
            37 : "Capacitor Volts using Capacitor VAR's and Capacitive Reactance",
            38 : "Capacitor Volts using Capacitor VAR's and Capacitor Amps",
            39 : 'Resistance using Resistor Volts and Resistor Amps',
            40 : 'Resistance using Resistor Volts and Watts',
            41 : 'Resistance using Impedance and Capacitive Reactance',
            42 : 'Resistance using Watts and Resistor Amps',
            43 : 'Resistance using Impedance and Power Factor',
            44 : 'Capacitor Amps using Total Amps and Resistor Amps',
            45 : 'Capacitor Amps using Capacitor Volts and Capacitive Reactance',
            46 : "Capacitor Amps using Capacitor VAR's and Capacitor Volts",
            47 : "Capacitor Amps using Capacitor VAR's and Capacitive Reactance",
            48 : 'Capacitive Reactance using Impedance and Resistance',
            49 : 'Capacitive Reactance using Capacitor Volts and Capacitor Amps',
            50 : "Capacitive Reactance using Capacitor Volts and Capacitor VAR's",
            51 : "Capacitive Reactance using Capacitor VAR's and Capacitor Amps",
            52 : 'Capacitive Reactance using Frequency and Capacitor Rating',
            53 : 'Capacitor Rating using Frequency and Capacitive Reactance',
            54 : "Capacitor VAR's using Capacitor Amps and Capacitive Reactance",
            55 : "Capacitor VAR's using Capacitor Volts and Capacitive Reactance",
            56 : "Capacitor VAR's using Capacitor Volts and Capacitor Amps",
            57 : "Capacitor VAR's using Volt Amps and Watts",
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.TAmps),
                (self.function_strings[2], self.TAmps2),
                (self.function_strings[3], self.TAmps3),
                (self.function_strings[4], self.TAmps4),
                (self.function_strings[5], self.TAmps5),
                (self.function_strings[6], self.PFactor),
                (self.function_strings[7], self.PFactor2),
                (self.function_strings[8], self.PFactor3),
                (self.function_strings[9], self.PFactor4),
                (self.function_strings[10], self.watts),
                (self.function_strings[11], self.watts2),
                (self.function_strings[12], self.watts3),
                (self.function_strings[13], self.watts4),
                (self.function_strings[14], self.watts5),
                (self.function_strings[15], self.impedance),
                (self.function_strings[16], self.impedance2),
                (self.function_strings[17], self.impedance3),
                (self.function_strings[18], self.impedance4),
                (self.function_strings[19], self.impedance5),
                (self.function_strings[20], self.RAmps),
                (self.function_strings[21], self.RAmps2),
                (self.function_strings[22], self.RAmps3),
                (self.function_strings[23], self.RAmps4),
                (self.function_strings[24], self.RAmps5),
                (self.function_strings[25], self.TVolts),
                (self.function_strings[26], self.TVolts2),
                (self.function_strings[27], self.TVolts3),
                (self.function_strings[28], self.VAmps),
                (self.function_strings[29], self.VAmps2),
                (self.function_strings[30], self.VAmps3),
                (self.function_strings[31], self.VAmps4),
                (self.function_strings[32], self.VAmps5),
                (self.function_strings[33], self.RVolts),
                (self.function_strings[34], self.RVolts2),
                (self.function_strings[35], self.RVolts3),
                (self.function_strings[36], self.CVolts),
                (self.function_strings[37], self.CVolts2),
                (self.function_strings[38], self.CVolts3),
                (self.function_strings[39], self.Resist),
                (self.function_strings[40], self.Resist2),
                (self.function_strings[41], self.Resist3),
                (self.function_strings[42], self.Resist4),
                (self.function_strings[43], self.Resist5),
                (self.function_strings[44], self.CAmps),
                (self.function_strings[45], self.CAmps2),
                (self.function_strings[46], self.CAmps3),
                (self.function_strings[47], self.CAmps4),
                (self.function_strings[48], self.CReact),
                (self.function_strings[49], self.CReact2),
                (self.function_strings[50], self.CReact3),
                (self.function_strings[51], self.CReact4),
                (self.function_strings[52], self.CReact5),
                (self.function_strings[53], self.CRate),
                (self.function_strings[54], self.CVAR),
                (self.function_strings[55], self.CVAR2),
                (self.function_strings[56], self.CVAR3),
                (self.function_strings[57], self.CVAR4)
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1]:OrderedDict(
                [
                    ( 'number_input', 'Resistor Amps (input): '),
                    ( 'number_input2', 'Capacitor Amps (input): '),
                ]
            ),
            self.function_strings[2]:OrderedDict(
                [
                    ( 'number_input', 'Total Volts (input): '),
                    ( 'number_input2', 'Impedance (input): '),
                ]
            ),
            self.function_strings[3]:OrderedDict(
                [
                    ( 'number_input', 'Volt Amps (input): '),
                    ( 'number_input2', 'Total Volts (input): '),
                ]
            ),
            self.function_strings[4]:OrderedDict(
                [
                    ( 'number_input', 'Resistor Amps (input): '),
                    ( 'number_input2', 'Power Factor (input): '),
                ]
            ),
            self.function_strings[5]:OrderedDict(
                [
                    ( 'number_input', 'Volt Amps (input): '),
                    ( 'number_input2', 'Impedance (input): '),
                ]
            ),
            self.function_strings[6]:OrderedDict(
                [
                    ( 'number_input', 'Impedance (input): '),
                    ( 'number_input2', 'Resistance (input): '),
                ]
            ),
            self.function_strings[7]:OrderedDict(
                [
                    ('number_input' , 'Resistor Amps (input): '),
                    ('number_input2' , 'Total Amps (input): ')
                ]
            ),
            self.function_strings[8]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Volt Amps (input): ')
                ]
            ),
            self.function_strings[9]:OrderedDict(
                [
                    ('number_input' , 'CoSine (input): '),
                    ('number_input2' , 'Theta Angle (input): ')
                ]
            ),
            self.function_strings[10]:OrderedDict(
                [
                    ('number_input' , 'Resistor Volts (input): '),
                    ('number_input2' , 'Resistor Amps (input): ')
                ]
            ),
            self.function_strings[11]:OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , 'Power Factor (input): ')
                ]
            ),
            self.function_strings[12]:OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , "Capacitor VAR's (input): ")
                ]
            ),
            self.function_strings[13]:OrderedDict(
                [
                    ('number_input' , 'Resistor Volts (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[14]:OrderedDict(
                [
                    ('number_input' , 'Resistor Amps (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[15]:OrderedDict(
                [
                    ('number_input' , 'Resistance (input): '),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[16]:OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , 'Total Amps (input): ')
                ]
            ),
            self.function_strings[17]:OrderedDict(
                [
                    ('number_input' , 'Total Volts (input): '),
                    ('number_input2' , 'Total Amps (input): ')
                ]
            ),
            self.function_strings[18]:OrderedDict(
                [
                    ('number_input' , 'Total Volts (input): '),
                    ('number_input2' , 'Volt Amps (input): ')
                ]
            ),
            self.function_strings[19]:OrderedDict(
                [
                    ('number_input' , 'Resistance (input): '),
                    ('number_input2' , 'Power Factor (input): ')
                ]
            ),
            self.function_strings[20]:OrderedDict(
                [
                    ('number_input' , 'Total Amps (input): '),
                    ('number_input2' , 'Capacitor Amps (input): ')
                ]
            ),
            self.function_strings[21]:OrderedDict(
                [
                    ('number_input' , 'Resistor Volts (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[22]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Resistor Volts (input): ')
                ]
            ),
            self.function_strings[23]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[24]:OrderedDict(
                [
                    ('number_input' , 'Power Factor (input): '),
                    ('number_input2' , 'Total Amps (input): ')
                ]
            ),
            self.function_strings[25]:OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , 'Total Amps (input): ')
                ]
            ),
            self.function_strings[26]:OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , 'Impedance (input): ')
                ]
            ),
            self.function_strings[27]:OrderedDict(
                [
                    ('number_input' , 'Total Amps (input): '),
                    ('number_input2' , 'Impedance (input): ')
                ]
            ),
            self.function_strings[28]:OrderedDict(
                [
                    ('number_input' , 'Total Volts (input): '),
                    ('number_input2' , 'Total Amps (input): ')
                ]
            ),
            self.function_strings[29]:OrderedDict(
                [
                    ('number_input' , 'Total Amps (input): '),
                    ('number_input2' , 'Impedance (input): ')
                ]
            ),
            self.function_strings[30]:OrderedDict(
                [
                    ('number_input' , 'Total Volts (input): '),
                    ('number_input2' , 'Impedance (input): ')
                ]
            ),
            self.function_strings[31]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , "Capacitor VAR's (input): ")
                ]
            ),
            self.function_strings[32]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Power Factor (input): ')
                ]
            ),
            self.function_strings[33]:OrderedDict(
                [
                    ('number_input' , 'Resistor Amps (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[34]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[35]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Resistor Amps (input): ')
                ]
            ),
            self.function_strings[36]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Amps (input): '),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[37]:OrderedDict(
                [
                    ('number_input' , "Capacitor VAR's (input): "),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[38]:OrderedDict(
                [
                    ('number_input' , "Capacitor VAR's (input): "),
                    ('number_input2' , 'Capacitor Amps (input): ')
                ]
            ),
            self.function_strings[39]:OrderedDict(
                [
                    ('number_input' , 'Resistor Volts (input): '),
                    ('number_input2' , 'Resistor Amps (input): ')
                ]
            ),
            self.function_strings[40]:OrderedDict(
                [
                    ('number_input' , 'Resistor Volts (input): '),
                    ('number_input2' , 'Watts (input): ')
                ]
            ),
            self.function_strings[41]:OrderedDict(
                [
                    ('number_input' , 'Impedance (input): '),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[42]:OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Resistor Amps (input): ')
                ]
            ),
            self.function_strings[43]:OrderedDict(
                [
                    ('number_input' , 'Impedance (input): '),
                    ('number_input2' , 'Power Factor (input): ')
                ]
            ),
            self.function_strings[44]:OrderedDict(
                [
                    ('number_input' , 'Total Amps (input): '),
                    ('number_input2' , 'Resistor Amps (input): ')
                ]
            ),
            self.function_strings[45]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Volts (input): '),
                    ('number_input2' , 'Capacitor Reactance (input): ')
                ]
            ),
            self.function_strings[46]:OrderedDict(
                [
                    ('number_input' , "Capacitor VAR's (input): "),
                    ('number_input2' , 'Capacitor Volts (input): ')
                ]
            ),
            self.function_strings[47]:OrderedDict(
                [
                    ('number_input' , "Capacitor VAR's (input): "),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[48]:OrderedDict(
                [
                    ('number_input' , 'Impedance (input): '),
                    ('number_input2' , 'Resistance (input): ')
                ]
            ),
            self.function_strings[49]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Volts (input): '),
                    ('number_input2' , 'Capacitor Amps (input): ')
                ]
            ),
            self.function_strings[50]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Volts (input): '),
                    ('number_input2' , "Capacitor VAR's (input): ")
                ]
            ),
            self.function_strings[51]:OrderedDict(
                [
                    ('number_input' , "Capacitor VAR's (input): "),
                    ('number_input2' , 'Capacitor Amps (input): ')
                ]
            ),
            self.function_strings[52]:OrderedDict(
                [
                    ('number_input' , 'Frequency (input): '),
                    ('number_input2' , 'Capacitor Rating (input): ')
                ]
            ),
            self.function_strings[53]:OrderedDict(
                [
                    ('number_input' , 'Frequency (input): '),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[54]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Amps (input): '),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[55]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Volts (input): '),
                    ('number_input2' , 'Capacitive Reactance (input): ')
                ]
            ),
            self.function_strings[56]:OrderedDict(
                [
                    ('number_input' , 'Capacitor Volts (input): '),
                    ('number_input2' , 'Capacitor Amps (input): ')
                ]
            ),
            self.function_strings[57]:OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , 'Watts (input): ')
                ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{               #TAmps
                '' : 'sqrt((Resistor Amps^2) + (Capacitor Amps^2))'
            },
            self.function_strings[2]:{                      #TAmps2
                '' : 'Total Volts / Impedance'
            },
            self.function_strings[3]:{                      #TAmps3
                '' : 'Volt Amps / Total Volts'
            },
            self.function_strings[4]:{                 #TAmps4
                '' : 'Resistor Amps / Power Factor'
            },
            self.function_strings[5]:{                        #TAmps5
                '' : 'sqrt(Volt Amps / Impedance)'
            },
            self.function_strings[6]:{                     #PFactor
                '' : 'Impedance / Resistance'
            },
            self.function_strings[7]:{                 #PFactor2
                '' : 'Resistor Amps / Total Amps'
            },
            self.function_strings[8]:{                          #PFactor3
                '' : 'Watts / Volt Amps'
            },
            self.function_strings[9]:{                       #PFactor4
                '' : 'CoSine * Theta Angle'
            },
            self.function_strings[10]:{                    #watts
                '' : 'Resistor Volts * Resistor Amps'
            },
            self.function_strings[11]:{                          #watts2
                '' : 'sqrt(Volt Amps^2 - Power Factor^2)'
            },
            self.function_strings[12]:{                       #watts3
                '' : "Volt Amps * Capacitor VAR's"
            },
            self.function_strings[13]:{                       #watts4
                '' : 'Resistor Volts^2 / Resistance'
            },
            self.function_strings[14]:{                        #watts5
                '' : 'Resistor Amps^2 / Resistance'
            },
            self.function_strings[15]:{             #impedance
                '' : '1 / sqrt(Resistance^2 + Capacitive Reactance^2)'
            },
            self.function_strings[16]:{                        #impednace2
                '' : 'Volt Amps / Total Amps^2'
            },
            self.function_strings[17]:{                      #impedance3
                '' : 'Total Volts / Total Amps'
            },
            self.function_strings[18]:{                       #impedance4
                '' : 'Total Volts^2 / Volt Amps'
            },
            self.function_strings[19]:{                     #impedance5
                '' : 'Resistacne * Power Factor'
            },
            self.function_strings[20]:{               #RAmps
                '' : 'sqrt(Total Amps^2 - Capacitor Amps^2)'
            },
            self.function_strings[21]:{               #RAmps2
                '' : 'Resistor Volts / Resistance'
            },
            self.function_strings[22]:{                    #RAmps3
                '' : 'Watts / Resistor Volts'
            },
            self.function_strings[23]:{                        #RAmps4
                '' : 'sqrt(Watts / Resistance)'
            },
            self.function_strings[24]:{                 #RAmps5
                '' : 'Power Factor * Total Amps'
            },
            self.function_strings[25]:{                      #TVolts
                '' : 'Volt Amps * Total Amps'
            },
            self.function_strings[26]:{                       #TVolts2
                '' : 'Volt Amps * Impedance'
            },
            self.function_strings[27]:{                      #TVolts3
                '' : 'sqrt(Total Amps * Impedance)'
            },
            self.function_strings[28]:{                      #VAmps
                '' : 'Total Volts * Total Amps'
            },
            self.function_strings[29]:{                        #VAmps2
                '' : 'Total Amps^2 * Impedance'
            },
            self.function_strings[30]:{                       #VAmps3
                '' : 'Total Volts^2 / Impedance'
            },
            self.function_strings[31]:{                       #VAmps4
                '' : "sqrt(Watts^2 + Capacitor VAR's^2"
            },
            self.function_strings[32]:{                          #VAmps5
                '' : 'Watts / Power Factor'
            },
            self.function_strings[33]:{               #RVolts
                '' : 'Resistor Amps * Resistance'
            },
            self.function_strings[34]:{                       #RVolts2
                '' : 'sqrt(Watts * Resistance)'
            },
            self.function_strings[35]:{                    #RVolts3
                '' : 'Watts / Resistor Amps'
            },
            self.function_strings[36]:{   #CVolts
                '' : 'Capacitor Amps * Capacitive Reactance'
            },
            self.function_strings[37]:{  #CVolts2
                '' : "sqrt(Capacitor VAR's * Capacitive Reactance)"
            },
            self.function_strings[38]:{        #CVolts3
                '' : "Capacitor VAR's / Capacitor Amps"
            },
            self.function_strings[39]:{               #Resist
                '' : 'Resistor Volts / Resistor Amps'
            },
            self.function_strings[40]:{                       #Resist2
                '' : 'Resistor Volts^2 / Watts'
            },
            self.function_strings[41]:{             #Resist3
                '' : '1 / sqrt((1 / Impedance^2) - (1 / Capacitive Reactance)^2)'
            },
            self.function_strings[42]:{                        #Resist4
                '' : 'Watts / Resistor Amps^2'
            },
            self.function_strings[43]:{                     #Resist5
                '' : 'Impedance / Power Factor'
            },
            self.function_strings[44]:{               #CAmps
                '' : 'sqrt(Total Amps^2 - Resistor Amps^2)'
            },
            self.function_strings[45]:{   #CAmps2
                '' : 'Capacitor Volts / Capacitive Reactance'
            },
            self.function_strings[46]:{        #CAmps3
                '' : "Capacitor VAR's / Capacitor Volts"
            },
            self.function_strings[47]:{   #CAmps4
                '' : "sqrt(Capacitor VAR's / Capacitive Reactance)"
            },
            self.function_strings[48]:{             #CReat
                '' : '1 / sqrt((1 / Impedance)^2 - (1 / Resistance)^2)'
            },
            self.function_strings[49]:{   #CReat2
                '' : 'Capacitor Volts / Capacitor Amps'
            },
            self.function_strings[50]:{  #CReact3
                '' : "Capacitor Volts / Capacitor VAR's"
            },
            self.function_strings[51]:{   #CReact4
                '' : "Capacitor VAR's / Capacitor Amps"
            },
            self.function_strings[52]:{       #CReact5
                '' : '0.5 * 3.14 * Frequency * Capacitor Rating'
            },
            self.function_strings[53]:{       #CRate
                '' : '0.5 * 3.14 * Frequency * Capacitive Reactance'
            },
            self.function_strings[54]:{   #CVAR
                '' : 'Capacitor Amps^2 * Capacitive Reactance'
            },
            self.function_strings[55]:{  #CVAR2
                '' : 'Capacitor Volts^2 / Capacitive Reactance'
            },
            self.function_strings[56]:{        #CVAR3
                '' : 'Capacitor Volts * Capacitor Amps'
            },
            self.function_strings[57]:{                       #CVAR4
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def TAmps(self):
        title = self.function_strings[1]
        ra = "Enter Resistor Amps"
        ca = "Enter Capacitor Amps"
        argsOut = [title, ra, ca]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp'))

    def TAmps2 (self):
        title = self.function_strings[2]
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp')) 

    def TAmps3 (self): 
        title = self.function_strings[3]
        va = "Enter Volt Amps"
        tv = "Enter Total Volts"
        argsOut = [title, va, tv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp')) 

    def TAmps4 (self):
        title = self.function_strings[4]
        ra = "Enter Resistor Amps"
        pf = "Enter Power Factor"
        argsOut = [title, ra, pf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp')) 

    def TAmps5 (self):
        title = self.function_strings[5]
        va = "Enter Volt Amps"
        i = "Enter Impedance"
        argsOut = [title, va, i]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Total Amp')) 

    def PFactor (self):
        title = self.function_strings[6]
        i = "Enter Impedance"
        r = "Enter Resistance"
        argsOut = [title, i, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor')) 

    def PFactor2 (self):
        title = self.function_strings[7]
        ra = "Enter Resistor Amps"
        ta = "Enter Total Amps"
        argsOut = [title, ra, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor')) 

    def PFactor3 (self):
        title = self.function_strings[8]
        w = "Enter Watts"
        va = "Enter Volt Amps"
        argsOut = [title, w, va]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor')) 

    def PFactor4 (self):
        title = self.function_strings[9]
        coS = "Enter CoSine"
        theta = "Enter Theta Angle"
        argsOut = [title, coS, theta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Power Factor')) 

    def watts (self):
        title = self.function_strings[10]
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt')) 

    def watts2 (self):
        title = self.function_strings[11]
        va = "Enter Volt Amps"
        pf = "Enter Power Factor"
        argsOut = [title, va, pf]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Watt')) 
        except(Exception):
           return ("Can not be a negative square root", '')

    def watts3 (self):
        title = self.function_strings[12]
        va = "Enter Volt Amps"
        var = "Enter Capacitor VAR's"
        argsOut = [title, va, var]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt')) 

    def watts4 (self):
        title = self.function_strings[13]
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt')) 

    def watts5 (self):
        title = self.function_strings[14]
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Watt')) 

    def impedance (self):
        title = self.function_strings[15]
        r = "Enter Resistance"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, r, cr]
        argsIn = self.prompt(argsOut)
        result = 1 / sqrt((argsIn[0] ** 2) + (argsIn[1] ** 2))
        return (self.prec(result, 4), self.pluralize(result, 'Impedance')) 

    def impedance2 (self):
        title = self.function_strings[16]
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1] ** 2)
        return (self.prec(result, 4), self.pluralize(result, 'Impedance')) 

    def impedance3 (self): 
        title = self.function_strings[17]
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance')) 

    def impedance4 (self):
        title = self.function_strings[18]
        tv = "Enter Total Volts"
        va = "Enter Volt Amps"
        argsOut = [title, tv, va]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance'))

    def impedance5 (self): 
        title = self.function_strings[19]
        r = "Enter Resistance"
        pf = "Enter Power Factor"
        argsOut = [title, r, pf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Impedance')) 

    def RAmps (self):
        title = self.function_strings[20]
        ta = "Enter Total Amps"
        ca = "Enter Capacitor Amps"
        argsOut = [title, ta, ca]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp'))
        except(Exception):
           return ("Can not be a negative square root", '')

    def RAmps2 (self):
        title = self.function_strings[21]
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp')) 

    def RAmps3 (self):
        title = self.function_strings[22]
        w = "Enter Watts"
        rv = "Enter Resistor Volts"
        argsOut = [title, w, rv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp')) 

    def RAmps4 (self):
        title = self.function_strings[23]
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp')) 

    def RAmps5 (self):
        title = self.function_strings[24]
        pf = "Enter Power Factor"
        ta = "Enter Total Amps"
        argsOut = [title, pf, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Amp')) 

    def TVolts (self):
        title = self.function_strings[25]
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt')) 

    def TVolts2 (self):
        title = self.function_strings[26]
        va = "Enter Volt Amps"
        i = "Enter Impedance"
        argsOut = [title, var, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt')) 

    def TVolts3 (self):
        title = self.function_strings[27]
        ta = "Enter Total Amps"
        i = "Enter Impedance"
        argsOut = [title, ta, i]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Total Volt')) 

    def VAmps (self):
        title = self.function_strings[28]
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp')) 

    def VAmps2 (self):
        title = self.function_strings[29]
        ta = "Enter Total Amps"
        i = "Enter Impedance"
        argsOut = [title, ta, i]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp')) 

    def VAmps3 (self):
        title = self.function_strings[30]
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp')) 

    def VAmps4 (self):
        title = self.function_strings[31]
        w = "Enter Watts"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, w, cvar]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0] ** 2) + (argsIn[1] ** 2))
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp')) 

    def VAmps5 (self):
        title = self.function_strings[32]
        w = "Enter Watts"
        pw = "Enter Power Factor"
        argsOut = [title, w, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Volt Amp'))
    
    def RVolts (self):
        title = self.function_strings[33]
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt'))

    def RVolts2 (self):
        title = self.function_strings[34]
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt')) 

    def RVolts3 (self):
        title = self.function_strings[35]
        w = "Enter Watts"
        ra = "Enter Resistor Amps"
        argsOut = [title, w, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistor Volt')) 

    def CVolts (self):
        title = self.function_strings[36]
        ca = "Enter Capacitor Amps"
        cr = "Enter Capacitor Reactance"
        argsOut = [title, ca, cr]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def CVolts2 (self):
        title = self.function_strings[37]
        cvar = "Enter Capacitor VAR's"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, cvar, cr]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt'))

    def CVolts3 (self):
        title = self.function_strings[38]
        cvar = "Enter Capacitor VAR's"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cvar, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Volt')) 

    def Resist (self):
        title = self.function_strings[39]
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance'))

    def Resist2 (self):
        title = self.function_strings[40]
        rv = "Enter Resistor Volts"
        w = "Enter Watts"
        argsOut = [title, rv, w]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2 ) / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Resistance')) 

    def Resist3 (self):
        title = self.function_strings[41]
        i = "Enter Impedance"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, i, cr]
        argsIn = self.prompt(argsOut)
        result = 1 / sqrt((1/argsIn[0]) ** 2 - (1/argsIn[1])**2)
        return (self.prec(result, 4), self.pluralize(result, "Resistance"))

    def Resist4 (self):
        title = self.function_strings[42]
        w = "Enter Watts"
        ra = "Enter Resistor Amps"
        argsOut = [title, w, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] /  argsIn[1]**2
        return (self.prec(result, 4), self.pluralize(result, "Resistance"))

    def Resist5 (self):
        title = self.function_strings[43]
        i = "Enter Impedance"
        pw = "Enter Power Factor"
        argsOut = [title, i, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] /  argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Resistance"))

    def CAmps(self):
        title = self.function_strings[44]
        ta = "Enter Total Amps"
        ra = "Enter Resistor Amps"
        argsOut = [title, ta, ra]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0]**2 - argsIn[1]**2)
        try:
            return (self.prec(result, 4), self.pluralize(result, "Capacitor Amp"))
        except(Exception):
            return ('Can not be a negative square root', '')

    def CAmps2(self):
        title = self.function_strings[45]
        cv = "Enter Capacitor Volts"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, cv, cr]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Capacitor Amp"))

    def CAmps3(self):
        title = self.function_strings[46]
        cvar = "Enter Capacitor VAR's"
        cv = "Enter Capacitor Volts"
        argsOut = [title, cvar, cv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, "Capacitor Amp"))

    def CAmps4(self):
        title = self.function_strings[47]
        cvar = "Enter Capacitor VAR's"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, cvar, cr]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec(result, 4), self.pluralize(result, "Capacitor Amp"))

    def CReact(self):
        title = self.function_strings[48]
        i = "Enter Impedance"
        r = "Enter Resistance"
        argsOut = [title, i, r]
        argsIn = self.prompt(argsOut)
        result = 1 / sqrt((1/argsIn[0])**2 - (1/argsIn[1])**2)
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def CReact2(self):
        title = self.function_strings[49]
        cv = "Enter Capacitor Volts"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cv, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def CReact3(self):
        title = self.function_strings[50]
        cv = "Enter Capacitor Volts"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, cv, cvar]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def CReact4(self):
        title = self.function_strings[51]
        cvar = "Enter Capacitor VAR's"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cvar, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def CReact5(self):
        title = self.function_strings[52]
        f = "Enter Frequency"
        crate = "Enter Capacitor Rating"
        argsOut = [title, f, crate]
        argsIn = self.prompt(argsOut)
        result = 0.5*3.14*argsIn[0]*argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitive Reactance'))

    def CRate(self):
        title = self.function_strings[53]
        f = "Enter Frequency"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, f, cr]
        argsIn = self.prompt(argsOut)
        result = 0.5*3.14*argsIn[0]*argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor Rating'))

    def CVAR(self):
        title = self.function_strings[54]
        ca = "Enter Capacitor Amps"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, ca, cr]
        argsIn = self.prompt(argsOut)
        result = argsIn[0]**2 * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def CVAR2(self):
        title = self.function_strings[55]
        cv = "Enter Capacitor Volts"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, cv, cr]
        argsIn = self.prompt(argsOut)
        result = argsIn[0]**2 / argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def CVAR3(self):
        title = self.function_strings[56]
        cv = "Enter Capacitor Volts"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cv, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))

    def CVAR4(self):
        title = self.function_strings[57]
        va = "Enter Volt Amps"
        w = "Enter Watts"
        argsOut = [title, va, w]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0]**2 - argsIn[1]**2)
        try:
            return (self.prec(result, 4), self.pluralize(result, 'Capacitor VAR'))
        except(Exception):
            return ('Can not be a negative square root', '')
#}}}_________________________________________________________________________________________


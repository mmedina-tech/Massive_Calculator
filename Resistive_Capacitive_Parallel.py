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
from log import *

class Resistive_Capacitive_Parallel(FormulaBase):
    def __init__(self, name):
        super(Resistive_Capacitive_Parallel, self).__init__(name)
        self.name = name

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                ('Total Amps using Resistor Amps and Capacitor Amps', self.TAmps),
                ('Total Amps using Total Volts and Impedance', self.TAmps2),
                ('Total Amps using Volt Amps and Total Volts', self.TAmps3),
                ('Total Amps using Resistor Amps and Power Factor', self.TAmps4),
                ('Total Amps using Volt Amps and Impedance', self.TAmps5),
                ('Power Factor using Impedance and Resistance', self.PFactor),
                ('Power Factor using Resistor Amps and Total Amps', self.PFactor2),
                ('Power Factor using Watts and Volt Amps', self.PFactor3),
                ('Power Factor using CoSine and Theta Angle', self.PFactor4),
                ('Watts using Resistor Volts and Resistor Amps', self.watts),
                ('Watts using Volt Amps and Power Factor', self.watts2),
                ("Watts using Volt Amps and Capacitor VAR's", self.watts3),
                ('Watts using Resistor Volts and Resistance', self.watts4),
                ('Watts using Resistor Amps and Resistance', self.watts5),
                ('Impedance using Resistance and Capacitive Reactance', self.impedance),
                ('Impedance using Volt Amps and Total Amps', self.impedance2),
                ('Impedance using Total Volts and Total Amps', self.impedance3),
                ('Impedance using Total Volts and Volt Amps', self.impedance4),
                ('Impedance using Resistance and Power Factor', self.impedance5),
                ('Resistor Amps using Total Amps and Capacitor Amps', self.RAmps),
                ('Resistor Amps using Resistor Volts and Resistance', self.RAmps2),
                ('Resistor Amps using Watts and Resistor Volts', self.RAmps3),
                ('Resistor Amps using Watts and Resistance', self.RAmps4),
                ('Resistor Amps using Power Factor and Total Amps', self.RAmps5),
                ('Total Volts using Volt Amps and Total Amps', self.TVolts),
                ('Total Volts using Volt Amps and Impedance', self.TVolts2),
                ('Total Volts using Total Amps and Impedance', self.TVolts3),
                ('Volt Amps using Total Volts and Total Amps', self.VAmps),
                ('Volt Amps using Total Amps and Impedance', self.VAmps2),
                ('Volt Amps using Total Volts and Impedance', self.VAmps3),
                ("Volt Amps uisng Watts and Capacitor VAR's", self.VAmps4),
                ('Volt Amps using Watts and Power Factor', self.VAmps5),
                ('Resistor Volts using Resistor Amps and Resistance', self.RVolts),
                ('Resistor Volts using Watts and Resistance', self.RVolts2),
                ('Resistor Volts using Watts and Resistor Amps', self.RVolts3),
                ('Capacitor Volts using Capacitor Amps and Capacitive Reactance', self.CVolts),
                ("Capacitor Volts using Capacitor VAR's and Capacitive Reactance", self.CVolts2),
                ("Capacitor Volts using Capacitor VAR's and Capacittor Amps", self.CVolts3),
                ('Resistance using Resistor Volts and Resistor Amps', self.Resist),
                ('Resistance using Resistor Volts and Watts', self.Resist2),
                ('Resistance using Impedance and Capacitive Reactance', self.Resist3),
                ('Resistance using Watts and Resistor Amps', self.Resist4),
                ('Resistance using Impedance and Power Factor', self.Resist5),
                ('Capacitor Amps using Total Amps and Resistor Amps', self.CAmps),
                ('Capacitor Amps using Capacitor Volts and Capacitive Reactance', self.CAmps2),
                ("Capacitor Amps using Capacitor VAR's and Capacitor Volts", self.CAmps3),
                ("Capacitor Amps using Capacotor VAR's and Capacitivie Reactance", self.CAmps4),
                ('Capacitive Reactance using Impedance and Resistance', self.CReact),
                ('Capacitive Reactance using Capacitor Volts and Capacitor Amps', self.CReact2),
                ("Capacitive Reactance using Capacitor Volts and Capacitor VAR's", self.CReact3),
                ("Capacitive Reactance using Capacitor VAR's and Capacitor Amps", self.CReact4),
                ('Capacitive Reactance using Frequency and Capacitor Rating', self.CReact5),
                ('Capacitor Rating using Frequency and Capacitive Reactance', self.CRate),
                ("Capacitor VAR's using Capacitor Amps and Capacitive Reactance", self.CVAR),
                ("Capacitor VAR's using Capacitor Volts and Capacitive Reactance", self.CVAR2),
                ("Capactior VAR's using Capacitor Volts and Capacitor Amps", self.CVAR3),
                ("Capacitor VAR's using Volt Amps and Watts", self.CVAR4)
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            'Total Amps using Resistor Amps and Capacitor Amps':OrderedDict(
                [
                    ( 'number_input', 'Resistor Amps (input): '),
                    ( 'number_input2', 'Capacitor Amps (input): '),
                ]
            ),
            'Total Amps using Total Volts and Impedance':OrderedDict(
                [
                    ( 'number_input', 'Total Volts (input): '),
                    ( 'number_input2', 'Impedance (input): '),
                ]
            ),
            'Total Amps using Volt Amps and Total Volts':OrderedDict(
                [
                    ( 'number_input', 'Volt Amps (input): '),
                    ( 'number_input2', 'Total Volts (input): '),
                ]
            ),
            'Total Amps using Resistor Amps and Power Factor':OrderedDict(
                [
                    ( 'number_input', 'Resistor Amps (input): '),
                    ( 'number_input2', 'Power Factor (input): '),
                ]
            ),
            'Total Amps using Volt Amps and Impedance':OrderedDict(
                [
                    ( 'number_input', 'Volt Amps (input): '),
                    ( 'number_input2', 'Impedance (input): '),
                ]
            ),
            'Power Factor using Impedance and Resistance':OrderedDict(
                [
                    ( 'number_input', 'Impedance (input): '),
                    ( 'number_input2', 'Resistance (input): '),
                ]
            ),
            'Power Factor using Resistor Amps and Power Factor':OrderedDict(
                [
                    ('number_input' , 'Resistor Amps (input): '),
                    ('number_input2' , 'Power Factor (input): ')
                ]
            ),
            'Power Factor using Watts and Volt Amps':OrderedDict(
                [
                    ('number_input' , 'Watts (input): '),
                    ('number_input2' , 'Volt Amps (input): ')
                ]
            ),
            'Power Factor using CoSine and Theta Angle':OrderedDict(
                [
                    ('number_input' , 'CoSine (input): '),
                    ('number_input2' , 'Theta Angle (input): ')
                ]
            ),
            'Watts using Resistor Volts and Resistor Amps':OrderedDict(
                [
                    ('number_input' , 'Resistor Volts (input): '),
                    ('number_input2' , 'Resistor Amps (input): ')
                ]
            ),
            'Watts using Volt Amps and Power Factor':OrderedDict(
                [
                    ('number_input' , 'Volt Amps (input): '),
                    ('number_input2' , 'Power Factor (input): ')
                ]
            ),
            "Watts using Volt Amps and Capacitor VAR's":OrderedDict(
                [
                    ('number_input' , "Volt Amps (input): "),
                    ('number_input2' , "Capacitor VAR's (input): ")
                ]
            ),
            "Watts using Resistor Volts and Resistance":OrderedDict(
                [
                    ("number_input" , "Resistor Volts (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Watts using Resistor Amps and Resistance":OrderedDict(
                [
                    ("number_input" , "Resistor Amps (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Inpedance using Resistance and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Resistance (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Impedance using Volt Amps and Total Amps":OrderedDict(
                [
                    ("number_input" , "Volt Amps (input): "),
                    ("number_input2" , "Total Amps (input): ")
                ]
            ),
            "Impedance using Total Volts and Total Amps":OrderedDict(
                [
                    ("number_input" , "Total Volts (input): "),
                    ("number_input2" , "Total Amps (input): ")
                ]
            ),
            "Impedance using Total Volts and Volt Amps":OrderedDict(
                [
                    ("number_input" , "Total Volts (input): "),
                    ("number_input2" , "Volt Amps (input): ")
                ]
            ),
            "Impedance using Resistance and Power Factor":OrderedDict(
                [
                    ("number_input" , "Resistance (input): "),
                    ("number_input2" , "Power Factor (input): ")
                ]
            ),
            "Resistor Amps using Total Amps and Capacitor Amps":OrderedDict(
                [
                    ("number_input" , "Total Amps (input): "),
                    ("number_input2" , "Capacitor Amps (input): ")
                ]
            ),
            "Resistor Amps using Resistor Volts and Resistance":OrderedDict(
                [
                    ("number_input" , "Resistor Volts (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Resistor Amps using Watts and Resistor Volts":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Resistor Volts (input): ")
                ]
            ),
            "Resistor Amps using Watts and Resistance":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Resistor Amps using Power Factor and Total Amps":OrderedDict(
                [
                    ("number_input" , "Power Factor (input): "),
                    ("number_input2" , "Total Amps (input): ")
                ]
            ),
            "Total Volts using Volt Amps and Total Amps":OrderedDict(
                [
                    ("number_input" , "Volt Amps (input): "),
                    ("number_input2" , "Total Amps (input): ")
                ]
            ),
            "Total Volts using Volt Amps and Impedance":OrderedDict(
                [
                    ("number_input" , "Volt Amps (input): "),
                    ("number_input2" , "Impedance (input): ")
                ]
            ),
            "Total Volts using Total Amps and Impedance":OrderedDict(
                [
                    ("number_input" , "Total Amps (input): "),
                    ("number_input2" , "Impedance (input): ")
                ]
            ),
            "Volt Amps using Total Volts and Total Amps":OrderedDict(
                [
                    ("number_input" , "Total Volts (input): "),
                    ("number_input2" , "Total Amps (input): ")
                ]
            ),
            "Volt Amps using Total Amps and Impedance":OrderedDict(
                [
                    ("number_input" , "Total Amps (input): "),
                    ("number_input2" , "Impedance (input): ")
                ]
            ),
            "Volt Amps using Total Volts and Impedance":OrderedDict(
                [
                    ("number_input" , "Total Volts (input): "),
                    ("number_input2" , "Impedance (input): ")
                ]
            ),
            "Volt Amps using Watts and Capacitor VAR's":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Capacitor VAR's (input): ")
                ]
            ),
            "Volt Amps using Watts and Power Factor":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Power Factor (input): ")
                ]
            ),
            "Resistor Volts using Resistor Amps and Resistance":OrderedDict(
                [
                    ("number_input" , "Resistor Amps (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Resistor Volts using Watts and Resistance":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Resistor Volts using Watts and Resistor Amps":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Resistor Amps (input): ")
                ]
            ),
            "Capacitor Volts using Capacitor Amps and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Capacitor Amps (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Capacitor Volts using Capacitor VAR's and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Capacitor VAR's (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Capacitor Volts using Capacitor VAR's and Capacitor Amps":OrderedDict(
                [
                    ("number_input" , "Capacitor VAR's (input): "),
                    ("number_input2" , "Capacitor Amps (input): ")
                ]
            ),
            "Resistance using Resistor Volts and Resistor Amps":OrderedDict(
                [
                    ("number_input" , "Resistor Volts (input): "),
                    ("number_input2" , "Resistor Amps (input): ")
                ]
            ),
            "Resistance using Resistor Volts and Watts":OrderedDict(
                [
                    ("number_input" , "Resistor Volts (input): "),
                    ("number_input2" , "Watts (input): ")
                ]
            ),
            "Resistance using Impedance and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Impedance (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Resistance using Watts and Resistor Amps":OrderedDict(
                [
                    ("number_input" , "Watts (input): "),
                    ("number_input2" , "Resistor Amps (input): ")
                ]
            ),
            "Resistance using Impedance and Power Factor":OrderedDict(
                [
                    ("number_input" , "Impedance (input): "),
                    ("number_input2" , "Power Factor (input): ")
                ]
            ),
            "Capacitor Amps using Total Amps and Resistor Amps":OrderedDict(
                [
                    ("number_input" , "Total Amps (input): "),
                    ("number_input2" , "Resistor Amps (input): ")
                ]
            ),
            "Capacitor Amps using Capacitor Volts and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Capacitor Volts (input): "),
                    ("number_input2" , "Capacitor Reactance (input): ")
                ]
            ),
            "Capacitor Amps using Capacitor VAR's and Capacitor Volts":OrderedDict(
                [
                    ("number_input" , "Capacitor VAR's (input): "),
                    ("number_input2" , "Capacitor Volts (input): ")
                ]
            ),
            "Capacitor Amps using Capacitor VAR's and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Capacitor VAR's (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Capacitive Reactance using Impedance and Resistance":OrderedDict(
                [
                    ("number_input" , "Impedance (input): "),
                    ("number_input2" , "Resistance (input): ")
                ]
            ),
            "Capacitive Reactance using Capacitor Volts and Capacitor Amps":OrderedDict(
                [
                    ("number_input" , "Capacitor Volts (input): "),
                    ("number_input2" , "Capacitor Amps (input): ")
                ]
            ),
            "Capacitive Reactance using Capacitor Volts and Capacitor VAR's":OrderedDict(
                [
                    ("number_input" , "Capacitor Volts (input): "),
                    ("number_input2" , "Capacitor VAR's (input): ")
                ]
            ),
            "Capacitve Reactance using Capacitor VAR's and Capacitor Amps":OrderedDict(
                [
                    ("number_input" , "Capacitor VAR's (input): "),
                    ("number_input2" , "Capacitor Amps (input): ")
                ]
            ),
            "Capacitive Reactance using Frequency and Capacitor Rating":OrderedDict(
                [
                    ("number_input" , "Frequency (input): "),
                    ("number_input2" , "Capacitor Rating (input): ")
                ]
            ),
            "Capacitor Rating using Frequency and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Frequency (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Capacitor VAR's using Capacitor Amps and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Capacitor Amps (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Capacitor VAR's using Capacitor Volts and Capacitive Reactance":OrderedDict(
                [
                    ("number_input" , "Capacitor Volts (input): "),
                    ("number_input2" , "Capacitive Reactance (input): ")
                ]
            ),
            "Capacitor VAR's using Capacitor Volts and Capacitor Amps":OrderedDict(
                [
                    ("number_input" , "Capacitor Volts (input): "),
                    ("number_input2" , "Capacitor Amps (input): ")
                ]
            ),
            "Capacitor VAR's using Volt Amps and Watts":OrderedDict(
                [
                    ("number_input" , "Volt Amps (input): "),
                    ("number_input2" , "Watts (input): ")
                ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Total Amps using Resistor Amps and Capacitor Amps':{               #TAmps
                '' : 'sqrt((Resistor Amps^2) + (Capacitor Amps^2))'
            },
            'Total Amps using Total Volts and Impedance':{                      #TAmps2
                '' : 'Total Volts / Impedance'
            },
            'Total Amps using Volt Amps and Total Volts':{                      #TAmps3
                '' : 'Volt Amps / Total Volts'
            },
            'Total Amps using Resistor Amps and Power Factor':{                 #TAmps4
                '' : 'Resistor Amps / Power Factor'
            },
            'Total Amps using Volt Amps and Impedance':{                        #TAmps5
                '' : 'sqrt(Volt Amps / Impedance)'
            },
            'Power Factor using Impedance and Resistance':{                     #PFactor
                '' : 'Impedance / Resistance'
            },
            'Power Factor using Resistor Amps and Total Amps':{                 #PFactor2
                '' : 'Resistor Amps / Total Amps'
            },
            'Power Factor using Watts and Volt Amps':{                          #PFactor3
                '' : 'Watts / Volt Amps'
            },
            'Power Factor using CoSine and Theta Angle':{                       #PFactor4
                '' : 'CoSine * Theta Angle'
            },
            'Watts using Resistor Volts and Resistor Amps':{                    #watts
                '' : 'Resistor Volts * Resistor Amps'
            },
            'Watts using Volt Amps and Power Factor':{                          #watts2
                '' : 'sqrt(Volt Amps^2 - Power Factor^2)'
            },
            "Watts using Volt Amps and Capacitor VAR's":{                       #watts3
                '' : "Volt Amps * Capacitor VAR's"
            },
            'Watts using Resistor Volts and Resistance':{                       #watts4
                '' : 'Resistor Volts^2 / Resistance'
            },
            'Watts using Resistor Amps and Resistance':{                        #watts5
                '' : 'Resistor Amps^2 / Resistance'
            },
            'Impedance using Resistance and Capacitive Reactance':{             #impedance
                '' : '1 / sqrt(Resistance^2 + Capacitive Reactance^2)'
            },
            'Impedance using Volt Amps and Total Amps':{                        #impednace2
                '' : 'Volt Amps / Total Amps^2'
            },
            'Impedance using Total Volts and Total Amps':{                      #impedance3
                '' : 'Total Volts / Total Amps'
            },
            'Impedance using Total Volts and Volt Amps':{                       #impedance4
                '' : 'Total Volts^2 / Volt Amps'
            },
            'Impedance using Resistance and Power Factor':{                     #impedance5
                '' : 'Resistacne * Power Factor'
            },
            'Resistor Amps using Total Amps and Capacitor Amps':{               #RAmps
                '' : 'sqrt(Total Amps^2 - Capacitor Amps^2)'
            },
            'Resistor Amps using Resistor Volts and Resistance':{               #RAmps2
                '' : 'Resistor Volts / Resistance'
            },
            'Resistor Amps using Watts and Resistor Volts':{                    #RAmps3
                '' : 'Watts / Resistor Volts'
            },
            'Resistor Amps using Watts and Resistance':{                        #RAmps4
                '' : 'sqrt(Watts / Resistance)'
            },
            'Resistor Amps using Power Factor and Total Amps':{                 #RAmps5
                '' : 'Power Factor * Total Amps'
            },
            'Total Volts using Volt Amps and Total Amps':{                      #TVolts
                '' : 'Volt Amps * Total Amps'
            },
            'Total Volts using Volt Amps and Impedance':{                       #TVolts2
                '' : 'Volt Amps * Impedance'
            },
            'Total Volts using Total Amps and Impedance':{                      #TVolts3
                '' : 'sqrt(Total Amps * Impedance)'
            },
            'Volt Amps using Total Volts and Total Amps':{                      #VAmps
                '' : 'Total Volts * Total Amps'
            },
            'Volt Amps using Total Amps and Impedance':{                        #VAmps2
                '' : 'Total Amps^2 * Impedance'
            },
            'Volt Amps using Total Volts and Impedance':{                       #VAmps3
                '' : 'Total Volts^2 / Impedance'
            },
            "Volt Amps using Watts and Capacitor VAR's":{                       #VAmps4
                '' : "sqrt(Watts^2 + Capacitor VAR's^2"
            },
            'Volt Amps using Watts and Power Factor':{                          #VAmps5
                '' : 'Watts / Power Factor'
            },
            'Resistor Volts using Resistor Amps and Resistance':{               #RVolts
                '' : 'Resistor Amps * Resistance'
            },
            'Resistor Volts using Watts and Resistance':{                       #RVolts2
                '' : 'sqrt(Watts * Resistance)'
            },
            'Resistor Volts using Watts and Resistor Amps':{                    #RVolts3
                '' : 'Watts / Resistor Amps'
            },
            'Capacitor Volts using Capacitor Amps and Capacitive Reactance':{   #CVolts
                '' : 'Capacitor Amps * Capacitive Reactance'
            },
            "Capacitor Volts using Capacitor VAR's and Capacitive Reactance":{  #CVolts2
                '' : "sqrt(Capacitor VAR's * Capacitive Reactance)"
            },
            "Capacitor Volts using Capacitor VAR's and Capacitor Amps":{        #CVolts3
                '' : "Capacitor VAR's / Capacitor Amps"
            },
            'Resistance using Resistor Volts and Resistor Amps':{               #Resist
                '' : 'Resistor Volts / Resistor Amps'
            },
            'Resistance using Resistor Volts and Watts':{                       #Resist2
                '' : 'Resistor Volts^2 / Watts'
            },
            'Resistance using Impedance and Capacitive Reactance':{             #Resist3
                '' : '1 / sqrt((1 / Impedance^2) - (1 / Capacitive Reactance)^2)'
            },
            'Resistance using Watts and Resistor Amps':{                        #Resist4
                '' : 'Watts / Resistor Amps^2'
            },
            'Resistance using Impedance and Power Factor':{                     #Resist5
                '' : 'Impedance / Power Factor'
            },
            'Capacitor Amps using Total Amps and Resistor Amps':{               #CAmps
                '' : 'sqrt(Total Amps^2 - Resistor Amps^2)'
            },
            'Capacitor Amps using Capacitor Volts and Capacitive Reactance':{   #CAmps2
                '' : 'Capacitor Volts / Capacitive Reactance'
            },
            "Capacitor Amps using Capacitor VAR's and Capacitor Volts":{        #CAmps3
                '' : "Capacitor VAR's / Capacitor Volts"
            },
            "Capacitor Amps using Capacitor VAR's and Capacitive Reactance":{   #CAmps4
                '' : "sqrt(Capacitor VAR's / Capacitive Reactance)"
            },
            'Capacitive Reactance using Impedance and Resistance':{             #CReat
                '' : '1 / sqrt((1 / Impedance)^2 - (1 / Resistance)^2)'
            },
            'Capacitive Reactance using Capacitor Volts and Capacitor Amps':{   #CReat2
                '' : 'Capacitor Volts / Capacitor Amps'
            },
            "Capacitive Reactance using Capacitor Volts and Capacitor VAR's":{  #CReact3
                '' : "Capacitor Volts / Capacitor VAR's"
            },
            "Capacitive Reactance using Capacitor VAR's and Capacitor Amps":{   #CReact4
                '' : "Capacitor VAR's / Capacitor Amps"
            },
            'Capacitive Reactance using Frequency and Capacitor Rating':{       #CReact5
                '' : '0.5 * 3.14 * Frequency * Capacitor Rating'
            },
            'Capacitor Rating using Frequency and Capacitive Reactance':{       #CRate
                '' : '0.5 * 3.14 * Frequency * Capacitive Reactance'
            },
            "Capacitor VAR's using Capacitor Amps and Capacitive Reactance":{   #CVAR
                '' : 'Capacitor Amps^2 * Capacitive Reactance'
            },
            "Capacitor VAR's using Capacitor Volts and Capacitive Reactance":{  #CVAR2
                '' : 'Capacitor Volts^2 / Capacitive Reactance'
            },
            "Capacitor VAR's using Capacitor Volts and Capacitor Amps":{        #CVAR3
                '' : 'Capacitor Volts * Capacitor Amps'
            },
            "Capacitor VAR's using Volt Amps and Watts":{                       #CVAR4
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def TAmps(self):
        title = "Total Amps using Resistor Amps and Capacitor Amps"
        ra = "Enter Resistor Amps"
        ca = "Enter Capacitor Amps"
        argsOut = [title, ra, ca]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def TAmps2 (self):
        title = "Total Amps using Total Volts and Impedance"
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Amp')) 

    def TAmps3 (self): 
        title = "Total Amps using Volt Amps and Total Volts"
        va = "Enter Volt Amps"
        tv = "Enter Total Volts"
        argsOut = [title, va, tv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Amp')) 

    def TAmps4 (self):
        title = "Total Amps using Resistor Amps and Power Factor"
        ra = "Enter Resistor Amps"
        pf = "Enter Power Factor"
        argsOut = [title, ra, pf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Amp')) 

    def TAmps5 (self):
        title = "Total Amps using Volt Amps and Impedance"
        va = "Enter Volt Amps"
        i = "Enter Impedance"
        argsOut = [title, va, i]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Total Amp')) 

    def PFactor (self):
        title = "Power Factor using Impedance and Resistance"
        i = "Enter Impedance"
        r = "Enter Resistance"
        argsOut = [title, i, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor')) 

    def PFactor2 (self):
        title = "Power Factor using Resistor Amps and Total Amps"
        ra = "Enter Resistor Amps"
        ta = "Enter Total Amps"
        argsOut = [title, ra, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor')) 

    def PFactor3 (self):
        title = "Power Factor using Watts and Volt Amps"
        w = "Enter Watts"
        va = "Enter Volt Amps"
        argsOut = [title, w, va]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor')) 

    def PFactor4 (self):
        title = "Power Factor using CoSine and Theta Angle"
        coS = "Enter CoSine"
        theta = "Enter Theta Angle"
        argsOut = [title, coS, theta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor')) 

    def watts (self):
        title = "Watts using Resistor Volts and Resistor Amps"
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt')) 

    def watts2 (self):
        title = "Watts using Volt Amps and Power Factor"
        va = "Enter Volt Amps"
        pf = "Enter Power Factor"
        argsOut = [title, va, pf]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
        return (self.prec4(result), self.pluralize(result, 'Watt')) 

    def watts3 (self):
        title = "Watts using Volt Amps and Capacitor VAR's"
        va = "Enter Volt Amps"
        var = "Enter Capacitor VAR's"
        argsOut = [title, va, var]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt')) 

    def watts4 (self):
        title = "Watts using Resistor Volts and Resistance"
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt')) 

    def watts5 (self):
        title = "Watts using Resistor Amps and Resistance"
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt')) 

    def impedance (self):
        title = "Impedance using Resiatance and Capacitive Reactance"
        r = "Enter Resistance"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, r, cr]
        argsIn = self.prompt(argsOut)
        result = 1 / sqrt((argsIn[0] ** 2) + (argsIn[1] ** 2))
        return (self.prec4(result), self.pluralize(result, 'Impedance')) 

    def impedance2 (self):
        title = "Impedance using Volt Amps and Total Amps"
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1] ** 2)
        return (self.prec4(result), self.pluralize(result, 'Impedance')) 

    def impedance3 (self): 
        title = "Impedance using Total Volts and Total Amps"
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Impedance')) 

    def impedance4 (self):
        title = "Impedance using Total Volts and Volt Amps"
        tv = "Enter Total Volts"
        va = "Enter Volt Amps"
        argsOut = [title, tv, va]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def impedance5 (self): 
        title = "Impedance using Resistance and Power Factor"
        r = "Enter Resistance"
        pf = "Enter Power Factor"
        argsOut = [title, r, pf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Impedance')) 

    def RAmps (self):
        title = "Resistor Amps using Total Amps and Capacitor Amps"
        ta = "Enter Total Amps"
        ca = "Enter Capacitor Amps"
        argsOut = [title, ta, ca]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def RAmps2 (self):
        title = "Resistor Amps using Resistor Volts and Resistance"
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp')) 

    def RAmps3 (self):
        title = "Resistor Amps using Watts and Resistor Volts"
        w = "Enter Watts"
        rv = "Enter Resistor Volts"
        argsOut = [title, w, rv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp')) 

    def RAmps4 (self):
        title = "Resistor Amps using Watts and Resistance"
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp')) 

    def RAmps5 (self):
        title = "Resistor Amps using Power Factor and Total Amps"
        pf = "Enter Power Factor"
        ta = "Enter Total Amps"
        argsOut = [title, pf, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp')) 

    def TVolts (self):
        title = "Total Volts using Volt Amps and Total Amps"
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Volt')) 

    def TVolts2 (self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Volt')) 

    def TVolts3 (self):
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Total Volt')) 

    def VAmps (self):
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp')) 

    def VAmps2 (self):
        result = (argsIn[0] ** 2) * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp')) 

    def VAmps3 (self):
        result = (argsIn[0] ** 2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp')) 

    def VAmps4 (self):
        result = sqrt((argsIn[0] ** 2) + (argsIn[1] ** 2))
        return (self.prec4(result), self.pluralize(result, 'Volt Amp')) 

    def VAmps5 (self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp'))
    
    def RVolts (self):
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def RVolts2 (self):
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt')) 

    def RVolts3 (self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt')) 

    def CVolts (self):
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def CVolts2 (self):
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def CVolts3 (self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt')) 

    def Resist (self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def Resist2 (self):
        result = (argsIn[0] ** 2 ) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistance')) 

    def Resist3 (self):
        result = 1 / sqrt((1/argsIn[0]) ** 2 - (1/argsIn[1])**2)
        return (self.prec4(result), self.pluralize(result, "Resistance"))

    def Resist4 (self):
        result = argsIn[0] /  argsIn[1]**2
        return (self.prec4(result), self.pluralize(result, "Resistance"))

    def Resist5 (self):
        result = argsIn[0] /  argsIn[1]
        return (self.prec4(result), self.pluralize(result, "Resistance"))

    def CAmps(self):
        result = sqrt(argsIn[0]**2 - argsIn[1]**2)
        return (self.prec4(result), self.pluralize(result, "Capacitor Amp"))

    def CAmps2(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, "Capacitor Amp"))

    def CAmps3(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, "Capacitor Amp"))

    def CAmps4(self):
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec4(result), self.pluralize(result, "Capacitor Amp"))

    def CReact(self):
        result = 1 / sqrt((1/argsIn[0])**2 - (1/argsIn[1])**2)
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def CReact2(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def CReact3(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def CReact4(self):
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def CReact5(self):
        result = 0.5*3.14*argsIn[0]*argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def CRate(self):
        result = 0.5*3.14*argsIn[0]*argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Rating'))

    def CVAR(self):
        result = argsIn[0]**2 * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor VAR'))

    def CVAR2(self):
        result = argsIn[0]**2 / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor VAR'))

    def CVAR3(self):
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor VAR'))

    def CVAR4(self):
        result = sqrt(argsIn[0]**2 - argsIn[1]**2)
        return (self.prec4(result), self.pluralize(result, 'Capacitor VAR'))
#}}}_________________________________________________________________________________________


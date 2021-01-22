#!/usr/bin/python
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


from FormulaBase import * 

class Resistive_Capacitive_Series(FormulaBase):
    def __init__(self):
        super(Resistive_Capacitive_Series, self).__init__()

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                ("Capacitive Reactance using Capacitor VAR's and Capacitor Amps", self.form_CReact2),
                ('Capacitive Reactance using Capacitor Volts and Capacitor Amps', self.form_CReact),
                ("Capacitive Reactance using Capacitor Volts and Capacitor VAR's", self.form_CReact4),
                ('Capacitive Reactance using Frequency and Capacitor Rating', self.form_CReact5),
                ('Capacitive Reactance using Impedance and Resistance', self.form_CReact3),
                ("Capacitor Amps using Capacitor VAR's and Capacitor Volts", self.form_CAmps),
                ("Capacitor Amps using Capacitor VAR's and Capacitive Reactance", self.form_CAmps2),
                ('Capacitor Amps using Capacitor Volts and Capacitive Reactance', self.form_CAmps3),
                ('Capacitor Rating using Frequency and Capacitive Reactance', self.form_CRate),
                ("Capacitor VAR's using Volt Amps and Watts", self.form_CVAR), 
                ("Capacitor VAR's using Capacitor Amps and Capacitive Reactance", self.form_CVAR3),
                ("Capacitor VAR's using Capacitor Volts and Capacitive Reactance", self.form_CVAR4),
                ("Capacitor VAR's using Capacitor Volts and Capacitor Amps", self.form_CVAR2),
                ('Capacitor Volts using Capacitor Amps and Capacitive Reactance', self.form_CVolts),
                ('Capacitor Volts using Total Volts and Resistor Volts', self.form_CVolts2),
                ("Capacitor Volts using Capacitor VAR's and Capacitive Reactance", self.form_CVolts3),
                ("Capacitor Volts using Capacitor VAR's and Capacitor Amps", self.form_CVolts4),
                ('Impedance using Resistance and Capacitive Reactance', self.form_Impedance),
                ('Impedance using Total Volts and Total Amps', self.form_Impedance2),
                ('Impedance using Volt Amps and Total Amps', self.form_Impedance3),
                ('Impedance using Resistance and Power Factor', self.form_Impedance4),
                ('Impedance using Total Volts and Volt Amps', self.form_Impedance5),
                ('Power Factor using Resistance and Impedance', self.form_Power),
                ('Power Factor using Watts and Volt Amps', self.form_Power2),
                ('Power Factor using Resistor Volts and Total Volts', self.form_Power3),
                ('Power Factor using CoSine and Theta Angle', self.form_Power4),
                ('Resistance using Watts and Resistor Amps', self.form_Resistance),
                ('Resistance using Impedance and Capacitive Reactance', self.form_Resistance2),
                ('Resistance using Resistor Volts and Watts', self.form_Resistance3),
                ('Resistance using Impedance and Power Factor', self.form_Resistance4),
                ('Resistance using Resistor Volts and Resistor Amps', self.form_Resistance5),
                ('Resistor Amps using Resistor Volts and Resistance', self.form_RAmps),
                ('Resistor Amps using Watts and Resistor Volts', self.form_RAmps2),
                ('Resistor Amps using Watts and Resistance', self.form_RAmps3),
                ('Resistor Volts using Total Volts and Capacitor Volts', self.form_RVolts),
                ('Resistor Volts using Total Volts and Power Factor', self.form_RVolts2),
                ('Resistor Volts using Resistor Amps and Resistance', self.form_RVolts3),
                ('Resistor Volts using Watts and Resistance', self.form_RVolts4),
                ('Resistor Volts using Watts and Resistor Amps', self.form_RVolts5),
                ('Total Amps using Total Volts and Impedance', self.form_TAmps),
                ('Total Amps using Volt Amps and Total Volts', self.form_TAmps2),
                ('Total Volts using Resistor Volts and Capacitor Volts', self.form_TVolts),
                ('Total Volts using Total Amps and Impedance', self.form_TVolts2),
                ('Total Volts using Volt Amps and Total Amps', self.form_TVolts3),
                ('Total Volts using Resistor Volts and Power Factor', self.form_TVolts4),
                ('Volt Amps using Total Volts and Total Amps', self.form_VAmps),
                ('Volt Amps using Total Amps and Impedance', self.form_VAmps2),
                ('Volt Amps using Total Volts and Impedance', self.form_VAmps3),
                ("Volt Amps using Watts and Capacitor VAR's", self.form_VAmps4),
                ('Volt Amps using Watts and Power Factor', self.form_VAmps5),
                ('Watts using Resistor Volts and Resistor Amps', self.form_Watts),
                ("Watts using Volt Amps and Capacitor VAR's", self.form_Watts2),
                ('Watts using Resistor Volts and Resistance', self.form_Watts3),
                ('Watts using Resistor Amps and Resistance', self.form_Watts4),
                ('Watts using Volt Amps and Power Factor', self.form_Watts5),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            'Capacitive Reactance using Capacitor Volts and Capacitor Amps':OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', 'Capacitor Amps: ')
                    ]
            ),
            "Capacitive Reactance using Capacitor VAR's and Capacitor Amps":OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitor Amps: ')
                    ]
            ),
            'Capacitive Reactance using Impedance and Resistance':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            "Capacitive Reactance using Capacitor Volts and Capacitor VAR's":OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', "Capacitor VAR's: ")
                    ]
            ),
            'Capacitive Reactance using Frequency and Capacitor Rating':OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Capacitor Rating: ')
                    ]
            ),
            "Capacitor Amps using Capacitor VAR's and Capacitor Volts":OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitor Volts: ')
                    ]
            ),
            "Capacitor Amps using Capacitor VAR's and Capacitive Reactance":OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            'Capacitor Amps using Capacitor Volts and Capacitive Reactance':OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            'Capacitor Rating using Frequency and Capacitive Reactance':OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            "Capacitor VAR's using Volt Amps and Watts":OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            "Capacitor VAR's using Capacitor Amps and Capacitive Reactance":OrderedDict(
                    [
                            ('number_input', 'Capacitor Amps: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            "Capacitor VAR's using Capacitor Volts and Capacitive Reactance":OrderedDict(
                    [
                            ('number_input', 'Capacitor Volts: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            "Capacitor VAR's using Capacitor Volts and Capacitor Amps":OrderedDict(
                    [
                            ('number_input' , 'Capacitor Volts: '),
                            ('number_input2' , 'Capacitor Amps: ')
                    ]
            ),
            'Capacitor Volts using Capacitor Amps and Capacitive Reactance':OrderedDict(
                    [
                            ('number_input', 'Capacitor Amps: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            'Capacitor Volts using Total Volts and Resistor Volts':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            "Capacitor Volts using Capacitor VAR's and Capacitive Reactance":OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            "Capacitor Volts using Capacitor VAR's and Capacitor Amps":OrderedDict(
                    [
                            ('number_input', "Capacitor VAR's: "),
                            ('number_input2', 'Capacitor Amps: ')
                    ]
            ),
            'Impedance using Resistance and Capacitive Reactance':OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Capacitive Reactance: ')
                    ]
            ),
            'Impedance using Total Volts and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Impedance using Volt Amps and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Impedance using Resistance and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Impedance using Total Volts and Volt Amps':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Volt Amps: ')
                    ]
            ),
            'Power Factor using Resistance and Impedance':OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            'Power Factor using Resistor Volts and Total Volts':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Total Volts: ')
                    ]
            ),
            'Power Factor using CoSine and Theta Angle':OrderedDict(
                    [
                            ('number_input', 'CoSine: '),
                            ('number_input2', 'Theta Angle: ')
                    ]
            ),
            'Resistance using Watts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistance using Impedance and Capacitive Reactance':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input', 'Capacitive Reactance: ')
                    ]
            ),
            'Resistance using Resistor Volts and Watts':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            'Resistance using Impedance and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Resistance using Resistor Volts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistor Amps using Resistor Volts and Resistance':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Resistor Amps using Watts and Resistor Volts':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            'Resistor Amps using Watts and Resistance':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Resistor Volts using Total Volts and Capacitor Volts':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Capacitor Volts: ')
                    ]
            ),
            'Resistor Volts using Total Volts and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Resistor Volts using Resistor Amps and Resistance':OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Resistor Volts using Watts and Resistance':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Resistor Volts using Watts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Total Volts using Resistor Volts and Capacitor Volts':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Capacitor Volts: ')
                    ]
            ),
            'Total Volts using Total Amps and Impedance':OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            'Total Volts using Volt Amps and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Total Volts using Resistor Volts and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Total Amps using Total Volts and Impedance':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            'Total Amps using Volt Amps and Total Volts':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Volts: ')
                    ]
            ),
            'Volt Amps using Total Volts and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Volt Amps using Total Amps and Impedance':OrderedDict(
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
            'Volt Amps using Total Volts and Impedance':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            "Volt Amps using Watts and Capacitor VAR's":OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', "Capacitor VAR's: ")
                    ]
            ),
            'Volt Amps using Watts and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Watts using Resistor Volts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            "Watts using Volt Amps and Capacitor VAR's":OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', "Capacitor VAR's: ")
                    ]
            ),
            'Watts using Resistor Volts and Resistance':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Watts using Resistor Amps and Resistance':OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Watts using Volt Amps and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            "Capacitive Reactance using Capacitor VAR's and Capacitor Amps":{                   #self.form_CReact2),
                '' : "Capacitor VAR's / Capacitor Amps^2"
            },
            'Capacitive Reactance using Capacitor Volts and Capacitor Amps':{                   #self.form_CReact),
                '' : 'Capacitor Volts / Capacitor Amps'
            },
            "Capacitive Reactance using Capacitor Volts and Capacitor VAR's":{                  #self.form_CReact4),
                '' : "Capacitor Volts^2 / Capacitor VAR's"
            },
            'Capacitive Reactance using Frequency and Capacitor Rating':{                       #self.form_CReact5),
                '' : '1 / (2 * 3.14 * Frequency * Capacitor Rating)'
            },
            'Capacitive Reactance using Impedance and Resistance':{                             #self.form_CReact3),
                '' : 'sqrt(Impedance^2 - Resistance^2)'
            },
            "Capacitor Amps using Capacitor VAR's and Capacitor Volts":{                        #self.form_CAmps),
                '' : "Capacitor VAR's / Capacitor Volts"
            },
            "Capacitor Amps using Capacitor VAR's and Capacitive Reactance":{                   #self.form_CAmps2),
                '' : "sqrt(Capacitor VAR's / Capacitive Reactance)"
            },
            'Capacitor Amps using Capacitor Volts and Capacitive Reactance':{                   #self.form_CAmps3),
                '' : 'Capacitor Volts^2 * Capacitive Reactance'
            },
            'Capacitor Rating using Frequency and Capacitive Reactance':{                       #self.form_CRate),
                '' : '1 / (2 * 3.14 Frequency * Capacitive Reactance)'
            },
            "Capacitor VAR's using Volt Amps and Watts":{                                       #self.form_CVAR), 
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
            "Capacitor VAR's using Capacitor Amps and Capacitive Reactance":{                   #self.form_CVAR3),
                '' : 'Capacitor Amps^2 * Capacitive Reactance'
            },
            "Capacitor VAR's using Capacitor Volts and Capacitive Reactance":{                  #self.form_CVAR4),
                '' : 'Capacitor Volts^2 / Capacitive Reactance'
            },
            "Capacitor VAR's using Capacitor Volts and Capacitor Amps":{                        #self.form_CVAR2),
                '' : 'Capacitor Volts * Capacitor Amps'
            },
            'Capacitor Volts using Capacitor Amps and Capacitive Reactance':{                   #self.form_CVolts),
                '' : 'Capacitor Amps * Capacitive Reactance'
            },
            'Capacitor Volts using Total Volts and Resistor Volts':{                            #self.form_CVolts2),
                '' : 'sqrt(Total Volts^2 - Resistor Volts^2)'
            },
            "Capacitor Volts using Capacitor VAR's and Capacitive Reactance":{                  #self.form_CVolts3),
                '' : "sqrt(Capacitor VAR's * Capacitive Reactance)"
            },
            "Capacitor Volts using Capacitor VAR's and Capacitor Amps":{                        #self.form_CVolts4),
                '' : "Capacitor VAR's / Capacitor Amps"
            },
            'Impedance using Resistance and Capacitive Reactance':{                             #self.form_Impedance),
                '' : 'sqrt(Impedance^2 + Capacitive Reactance^2)'
            },
            'Impedance using Total Volts and Total Amps':{                                      #self.form_Impedance2),
                '' : 'Total Volts / Total Amps'
            },
            'Impedance using Volt Amps and Total Amps':{                                        #self.form_Impedance3),
                '' : 'Volt Amps / Total Amps^2'
            },
            'Impedance using Resistance and Power Factor':{                                     #self.form_Impedance4),
                '' : 'Resistance / Power Factor'
            },
            'Impedance using Total Volts and Volt Amps':{                                       #self.form_Impedance5),
                '' : 'Total Volts^2 / Volt Amps'
            },
            'Power Factor using Resistance and Impedance':{                                     #self.form_Power),
                '' : 'Resistance / Impedance'
            },
            'Power Factor using Watts and Volt Amps':{                                          #self.form_Power2),
                '' : 'Watts / Volt Amps'
            },
            'Power Factor using Resistor Volts and Total Volts':{                               #self.form_Power3),
                '' : 'Resistor Volts / Total Volts'
            },
            'Power Factor using CoSine and Theta Angle':{                                       #self.form_Power4),
                '' : 'CoSine * Theta Angle'
            },
            'Resistance using Watts and Resistor Amps':{                                        #self.form_Resistance),
                '' : 'Watts / Resistor Amps^2'
            },
            'Resistance using Impedance and Capacitive Reactance':{                             #self.form_Resistance2),
                '' : 'sqrt(Impedance^2 - Capacitive Reactance^2)'
            },
            'Resistance using Resistor Volts and Watts':{                                       #self.form_Resistance3),
                '' : 'Resistor Volts^2 / Watts'
            },
            'Resistance using Impedance and Power Factor':{                                     #self.form_Resistance4),
                '' : 'Impedance * Power Factor'
            },
            'Resistance using Resistor Volts and Resistor Amps':{                               #self.form_Resistance5),
                '' : 'Resistor Volts / Resistor Amps'
            },
            'Resistor Amps using Resistor Volts and Resistance':{                               #self.form_RAmps),
                '' : 'Resistor Volts / Resistance'
            },
            'Resistor Amps using Watts and Resistor Volts':{                                    #self.form_RAmps2),
                '' : 'Watts / Resistor Volts'
            },
            'Resistor Amps using Watts and Resistance':{                                        #self.form_RAmps3),
                '' : 'sqrt(Watts / Resistance)'
            },
            'Resistor Volts using Total Volts and Capacitor Volts':{                            #self.form_RVolts),
                '' : 'Total Volts * Capacitor Volts'
            },
            'Resistor Volts using Total Volts and Power Factor':{                               #self.form_RVolts2),
                '' : 'sqrt(Total Volts * Power Factor)'
            },
            'Resistor Volts using Resistor Amps and Resistance':{                               #self.form_RVolts3),
                '' : 'Resistor Amps / Resistance'
            },
            'Resistor Volts using Watts and Resistance':{                                       #self.form_RVolts4),
                '' : 'sqrt(Watts^2 - Resistance^2)'
            },
            'Resistor Volts using Watts and Resistor Amps':{                                    #self.form_RVolts5),
                '' : 'Watts * Resistor Amps'
            },
            'Total Amps using Total Volts and Impedance':{                                      #self.form_TAmps),
                '' : 'Total Volts / Impedance'
            },
            'Total Amps using Volt Amps and Total Volts':{                                      #self.form_TAmps2),
                '' : 'Volt Amps / Total Volts'
            },
            'Total Volts using Resistor Volts and Capacitor Volts':{                            #self.form_TVolts),
                '' : 'sqrt(Resistor Volts^2 + Capacitor Volts^2)'
            },
            'Total Volts using Total Amps and Impedance':{                                      #self.form_TVolts2),
                '' : 'Total Amps * Impedance'
            },
            'Total Volts using Volt Amps and Total Amps':{                                      #self.form_TVolts3),
                '' : 'Volt Amps / Total Amps'
            },
            'Total Volts using Resistor Volts and Power Factor':{                               #self.form_TVolts4),
                '' : 'Resistor Volts / Power Factor'
            },
            'Volt Amps using Total Volts and Total Amps':{                                      #self.form_VAmps),
                '' : 'Total Volts * Total Amps'
            },
            'Volt Amps using Total Amps and Impedance':{                                        #self.form_VAmps2),
                '' : 'Total Amps^2 * Impedance'
            },
            'Volt Amps using Total Volts and Impedance':{                                       #self.form_VAmps3),
                '' : 'Total Volts^2 / Impedance'
            },
            "Volt Amps using Watts and Capacitor VAR's":{                                       #self.form_VAmps4),
                '' : "sqrt(Watts^2 + Capacitor VAR's^2)"
            },
            'Volt Amps using Watts and Power Factor':{                                          #self.form_VAmps5),
                '' : 'Watts / Power Factor'
            },
            'Watts using Resistor Volts and Resistor Amps':{                                    #self.form_Watts),
                '' : 'Resistor Volts * Resistor Amps'
            },
            "Watts using Volt Amps and Capacitor VAR's":{                                       #self.form_Watts2),
                '' : "sqrt(Volt Amps^2 - Capacitor VAR's^2)"
            },
            'Watts using Resistor Volts and Resistance':{                                       #self.form_Watts3),
                '' : 'Resistor Volts^2 / Resistance'
            },
            'Watts using Resistor Amps and Resistance':{                                        #self.form_Watts4),
                '' : 'Resistor Amps^2 * Resistance'
            },
            'Watts using Volt Amps and Power Factor':{                                          #self.form_Watts5),
                '' : 'Volt Amps * Power Factor'
            },
        }

#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________
    def form_TVolts(self, num, num2):
            result = sqrt((float(num)**2) + (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts2(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts3(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts4(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_Power(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_Power2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_Power3(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_Power4(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_TAmps(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_TAmps2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_VAmps(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps2(self, num, num2):
            result = (float(num)**2) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps3(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps4(self, num, num2):
            result = sqrt((float(num)**2) + (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps5(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_Impedance(self, num, num2):
            result = sqrt((float(num)**2) + (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance3(self, num, num2):
            result = float(num) / (float(num2)**2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance4(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance5(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_RAmps(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_RAmps2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_RAmps3(self, num, num2):
            result = sqrt(float(num) / float(num2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_Watts(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts2(self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts3(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts4(self, num, num2):
            result = (float(num)**2) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts5(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_CAmps(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Capacitor Amp'))
            
    def form_CAmps2(self, num, num2): 
            result = sqrt(float(num) / float(num2))
            return (self.prec4(result), self.pluralize(result, 'Capacitor Amp'))

    def form_CAmps3(self, num, num2): 
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Capacitor Amp'))

    def form_CVAR (self, num, num2): 
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR2 (self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR3 (self, num, num2):
            result = (float(num)**2) * float(num2)
            return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR4 (self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_RVolts (self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts2 (self, num, num2):
            result = sqrt(float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts3 (self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts4 (self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts5 (self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_Resistance (self, num, num2):
            result = float(num) / (float(num2)**2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance2 (self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance3 (self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance4 (self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance5 (self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_CReact(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact2(self, num, num2):
            result = float(num) / (float(num2)**2)
            return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact3 (self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact4 (self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact5 (self, num, num2):
            result = 1 / (2 * 3.14 * float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CRate (self, num, num2):
            result = 1 / (2 * 3.14 * float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Capacitor Rating'))

    def form_CVolts (self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts2 (self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts3 (self, num, num2):
            result = sqrt(float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts4 (self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))
#}}}_________________________________________________________________________________________


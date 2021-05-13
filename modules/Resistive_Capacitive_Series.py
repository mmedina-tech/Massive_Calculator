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
    def __init__(self, name):
        super(Resistive_Capacitive_Series, self).__init__(name)
        self.name = name

#{{{___ Function List _____________________________________________________________________________
        self.function_list = {
            'Watts using Volt Amps and Power Factor': self.form_Watts5,
            "Capacitive Reactance using Capacitor VAR's and Capacitor Amps": self.form_CReact2,
            'Capacitive Reactance using Capacitor Volts and Capacitor Amps': self.form_CReact,
            "Capacitive Reactance using Capacitor Volts and Capacitor VAR's": self.form_CReact4,
            'Capacitive Reactance using Frequency and Capacitor Rating': self.form_CReact5,
            'Capacitive Reactance using Impedance and Resistance': self.form_CReact3,
            "Capacitor Amps using Capacitor VAR's and Capacitor Volts": self.form_CAmps,
            "Capacitor Amps using Capacitor VAR's and Capacitive Reactance": self.form_CAmps2,
            'Capacitor Amps using Capacitor Volts and Capacitive Reactance': self.form_CAmps3,
            'Capacitor Rating using Frequency and Capacitive Reactance': self.form_CRate,
            "Capacitor VAR's using Volt Amps and Watts": self.form_CVAR, 
            "Capacitor VAR's using Capacitor Amps and Capacitive Reactance": self.form_CVAR3,
            "Capacitor VAR's using Capacitor Volts and Capacitive Reactance": self.form_CVAR4,
            "Capacitor VAR's using Capacitor Volts and Capacitor Amps": self.form_CVAR2,
            'Capacitor Volts using Capacitor Amps and Capacitive Reactance': self.form_CVolts,
            'Capacitor Volts using Total Volts and Resistor Volts': self.form_CVolts2,
            "Capacitor Volts using Capacitor VAR's and Capacitive Reactance": self.form_CVolts3,
            "Capacitor Volts using Capacitor VAR's and Capacitor Amps": self.form_CVolts4,
            'Impedance using Resistance and Capacitive Reactance': self.form_Impedance,
            'Impedance using Total Volts and Total Amps': self.form_Impedance2,
            'Impedance using Volt Amps and Total Amps': self.form_Impedance3,
            'Impedance using Resistance and Power Factor': self.form_Impedance4,
            'Impedance using Total Volts and Volt Amps': self.form_Impedance5,
            'Power Factor using Resistance and Impedance': self.form_Power,
            'Power Factor using Watts and Volt Amps': self.form_Power2,
            'Power Factor using Resistor Volts and Total Volts': self.form_Power3,
            'Power Factor using CoSine and Theta Angle': self.form_Power4,
            'Resistance using Watts and Resistor Amps': self.form_Resistance,
            'Resistance using Impedance and Capacitive Reactance': self.form_Resistance2,
            'Resistance using Resistor Volts and Watts': self.form_Resistance3,
            'Resistance using Impedance and Power Factor': self.form_Resistance4,
            'Resistance using Resistor Volts and Resistor Amps': self.form_Resistance5,
            'Resistor Amps using Resistor Volts and Resistance': self.form_RAmps,
            'Resistor Amps using Watts and Resistor Volts': self.form_RAmps2,
            'Resistor Amps using Watts and Resistance': self.form_RAmps3,
            'Resistor Volts using Total Volts and Capacitor Volts': self.form_RVolts,
            'Resistor Volts using Total Volts and Power Factor': self.form_RVolts2,
            'Resistor Volts using Resistor Amps and Resistance': self.form_RVolts3,
            'Resistor Volts using Watts and Resistance': self.form_RVolts4,
            'Resistor Volts using Watts and Resistor Amps': self.form_RVolts5,
            'Total Amps using Total Volts and Impedance': self.form_TAmps,
            'Total Amps using Volt Amps and Total Volts': self.form_TAmps2,
            'Total Volts using Resistor Volts and Capacitor Volts': self.form_TVolts,
            'Total Volts using Total Amps and Impedance': self.form_TVolts2,
            'Total Volts using Volt Amps and Total Amps': self.form_TVolts3,
            'Total Volts using Resistor Volts and Power Factor': self.form_TVolts4,
            'Volt Amps using Total Volts and Total Amps': self.form_VAmps,
            'Volt Amps using Total Amps and Impedance': self.form_VAmps2,
            'Volt Amps using Total Volts and Impedance': self.form_VAmps3,
            "Volt Amps using Watts and Capacitor VAR's": self.form_VAmps4,
            'Volt Amps using Watts and Power Factor': self.form_VAmps5,
            'Watts using Resistor Volts and Resistor Amps': self.form_Watts,
            "Watts using Volt Amps and Capacitor VAR's": self.form_Watts2,
            'Watts using Resistor Volts and Resistance': self.form_Watts3,
            'Watts using Resistor Amps and Resistance': self.form_Watts4,
        }
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
    def form_TVolts(self):
        title = "Total Volts using Resistor Volts and Capacitor Volts"
        rv = "Enter Resistor Volts"
        cv = "Enter Capacitor Volts"
        argsOut = [title, rv, cv]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts2(self):
        title = "Total Volts using Total Amps and Impedance"
        ta = "Enter Total Amps"
        i = "Enter Impedance"
        argsOut = [title, ta, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts3(self):
        title = "Total Volts using Volt Amps and Total Amps"
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts4(self):
        title = "Total Volts using Resistor Volts and Power Factor"
        rv = "Enter Resistor Volts"
        pw = "Enter Power Factor"
        argsOut = [title, rv, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_Power(self):
        title = "Power Factor using Resistance and Impedance"
        r = "Enter Resistance"
        i = "Enter Impedance"
        argsOut = [title, r, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_Power2(self):
        title = "Power Factor using Watts and Volt Amps"
        w = "Enter Watts"
        va = "Enter Volt Amps"
        argsOut = [title, w, va]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_Power3(self):
        title = "Power Factor using Resistor Volts and Total Volts"
        rv = "Enter Resistor Volts"
        tv = "Enter Total Volts"
        argsOut = [title, rv, tv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_Power4(self):
        title = "Power Factor using CoSine and Theta Angle"
        coS = "Enter CoSine"
        theta = "Enter Theta Angle"
        argsOut = [title, coS, theta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_TAmps(self):
        title = "Total Amps using Total Volts and Impedance"
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_TAmps2(self):
        title = "Total Amps using Volt Amps and Total Volts"
        va = "Enter Volt Amps"
        tv = "Enter Total Volts"
        argsOut = [title, va, tv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_VAmps(self):
        title = "Volt Amps using Total Volts and Total Amps"
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps2(self):
        title = "Volt Amps using Total Amps and Impedance"
        ta = "Enter Total Amps"
        i = "Enter Impedance"
        argsOut = [title, ta, i]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps3(self):
        title = "Volt Amps using Total Volts and Impedance"
        tv = "Enter Total Volts"
        i = "Enter Impedance"
        argsOut = [title, tv, i]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps4(self):
        title = "Volt Amps using Watts and Capacitor VAR's"
        w = "Enter Watts"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, w, cvar]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VAmps5(self):
        title = "Volt Amps using Watts and Power Factor"
        w = "Enter Watts"
        pw = "Enter Power Factor"
        argsOut = [title, w, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_Impedance(self):
        title = "Impedance using Resistance and Capacitive Reactance"
        r = "Enter Resistance"
        cr = "Enter Capacitive Reactance"
        argsOut = [title, r, cr]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance2(self):
        title = "Impedance using Total Volts and Total Amps"
        tv = "Enter Total Volts"
        ta = "Enter Total Amps"
        argsOut = [title, tv, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance3(self):
        title = "Impedance using Volt Amps and Total Amps"
        va = "Enter Volt Amps"
        ta = "Enter Total Amps"
        argsOut = [title, va, ta]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance4(self):
        title = "Impedance using Resistance and Power Factor"
        r = "Enter Resistance"
        pw = "Enter Power Factor"
        argsOut = [title, r, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance5(self):
        title = "Impedance using Total Volts and Volt Amps"
        tv = "Enter Total Volts"
        va = "Enter Volt Amps"
        argsOut = [title, tv, va]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_RAmps(self):
        title = "Resistor Amps using Resistor Volts and Resistance"
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_RAmps2(self):
        title = "Resistor Amps using Watts and Resistor Volts"
        w = "Enter Watts"
        rv = "Enter Resistor Volts"
        argsOut = [title, w, rv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_RAmps3(self):
        title = "Resistor Amps using Watts and Resistance"
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_Watts(self):
        title = "Watts using Resistor Volts and Resistor Amps"
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts2(self):
        title = "Watts using Volt Amps and Capacitor VAR's"
        va = "Enter Volt Amps"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, va, cvar]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts3(self):
        title = "Watts using Resistor Volts and Resistance"
        rv = "Enter Resistor Volts"
        r = "Enter Resistance"
        argsOut = [title, rv, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts4(self):
        title = "Watts using Resistor Amps and Resistance"
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts5(self):
        title = "Watts using Volt Amps and Power Factor"
        va = "Enter Volt Amps"
        pw = "Enter Power Factor"
        argsOut = [title, va, pw]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_CAmps(self):
        title = "Capacitor Amps using Capacitor VAR's and Capacitor Volts"
        cvar = "Enter Capacitor VAR's"
        cv = "Enter Capacitor Volts"
        argsOut = [title, cvar, cv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Amp'))
        
    def form_CAmps2(self): 
        title = "Capacitor Amps using Capacitor VAR's and Capacitive Reactance"
        cvar = "Enter Capacitor VAR's"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, cvar, creact]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Capacitor Amp'))

    def form_CAmps3(self): 
        title = "Capacitor Amps using Capacitor Volts and Capacitive Reactance"
        cv = "Enter Capacitor Volts"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, cv, creact]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Amp'))

    def form_CVAR (self): 
        title = "Capacitor VAR's using Volt Amps and Watts"
        va = "Enter Volt Amps"
        w = "Enter Watts"
        argsOut = [title, va, w]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR2 (self):
        title = "Capacitor VAR's using Capacitor Volts and Capacitor Amps"
        cv = "Enter Capacitor Volts"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cv, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR3 (self):
        title = "Capacitor VAR's using Capacitor Amps and Capacitive Reactance"
        ca = "Enter Capacitor Amps"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, ca, creact]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) * argsIn[1]
        return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_CVAR4 (self):
        title = "Capacitor VAR's using Capcacitor Volts and Capacitive Reactance"
        cv = "Enter Capacitor Volts"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, cv, creact]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, "Capacitor VAR'"))

    def form_RVolts (self):
        title = "Resistor Volts using Total Volts and Capacitor Volts"
        tv = "Enter Total Volts"
        cv = "Enter Capacitor Volts"
        argsOut = [title, tv, cv]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts2 (self):
        title = "Resistor Volts using Total Volts and Power Factor"
        tv = "Enter Total Volts"
        pwf = "Enter Power Factor"
        argsOut = [title, tv, pwf]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts3 (self):
        title = "Resistor Volts using Resistor Amps and Resistance"
        ra = "Enter Resistor Amps"
        r = "Enter Resistance"
        argsOut = [title, ra, r]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts4 (self):
        title = "Resistor Volts using Watts and Resistance"
        w = "Enter Watts"
        r = "Enter Resistance"
        argsOut = [title, w, r]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_RVolts5 (self):
        title = "Resistor Volts using Watts and Resistor Amps"
        w = "Enter Watts"
        ra = "Enter Resistor Amps"
        argsOut = [title, w, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_Resistance (self):
        title = "Resistance using Watts and Resistor Amps"
        w = "Enter Watts"
        ra = "Enter Resistor Amps"
        argsOut = [title, w, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance2 (self):
        title = "Resistance using Impedance and Capacitive Reactance"
        i = "Enter Impedance"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, i, creact]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance3 (self):
        title = "Resistance usin Resistor Volts and Watts"
        rv = "Enter Resistor Volts"
        w = "Enter Watts"
        argsOut = [title, rv, w]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance4 (self):
        title = "Resistance using Impedance and Power Factor"
        imp = "Enter Impedance"
        pwf = "Enter Power Factor"
        argsOut = [title, imp, pwf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance5 (self):
        title = "Resistance using Resistor Volts and Resistor Amps"
        rv = "Enter Resistor Volts"
        ra = "Enter Resistor Amps"
        argsOut = [title, rv, ra]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_CReact(self):
        title = "Capacitive Reactance using Capacitor Volts and Capacitor Amps"
        cv = "Enter Capacitor Volts"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cv, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact2(self):
        title = "Capacitive Reactance using Capacitor VAR's and Capacitor Amps"
        cvar = "Enter Capacitor VAR's"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cvar, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1]**2)
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact3 (self):
        title = "Capacitive Reactance using Impedance and Resistance"
        imp = "Enter Impedance"
        r = "Enter Resistance"
        argsOut = [title, imp, r]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact4 (self):
        title = "Capacitive Reactance using Capacitor Volts and Capacitor VAR's"
        cv = "Enter Capacitor Volts"
        cvar = "Enter Capacitor VAR's"
        argsOut = [title, cv, cvar]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0]**2) / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CReact5 (self):
        title = "Capacitive Reactance using Frequency and Capacitor Rating"
        freq = "Enter Frequency"
        crate = "Enter Capacitor Rating"
        argsOut = [title, freq, crate]
        argsIn = self.prompt(argsOut)
        result = 1 / (2 * 3.14 * argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Capacitive Reactance'))

    def form_CRate (self):
        title = "Capacitor Rating using Frequency and Capacitive Reactance"
        freq = "Enter Frequency"
        creact = "Enter Capacitive Reactance"
        argsOut = [title, freq, creact]
        argsIn = self.prompt(argsOut)
        result = 1 / (2 * 3.14 * argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Capacitor Rating'))

    def form_CVolts (self):
        title = "Capacitor Volts using Capacitor Amps and Capacitive Reactance"
        ca = "Enter Capacitor Amps"
        creat = "Enter Capacitive Reactance"
        argsOut = [title, ca, creact]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts2 (self):
        title = "Capacitor Volts using Total Volts and Resistor Volts"
        tv = "Enter Total Volts"
        rv = "Enter Resistor Volts"
        argsOut = [title, tv, rv]
        argsIn = self.prompt(argsOut)
        result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts3 (self):
        title = "Capacitor Volts using Capacitor VAR's and Capacitive Reactance"
        cvar = "Enter Capacitor VAR's"
        creact = "Enter Capacititve Reactance"
        argsOut = [title, cvar, creact]
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))

    def form_CVolts4 (self):
        title = "Capacitor Volts using Capacitor VAR's and Capacitor Amps"
        cvar = "Enter Capacitor VAR's"
        ca = "Enter Capacitor Amps"
        argsOut = [title, cvar, ca]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec4(result), self.pluralize(result, 'Capacitor Volt'))
#}}}_________________________________________________________________________________________


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

class ResistiveInductive_series(FormulaBase):
    def __init__(self, name):
        super(ResistiveInductive_series, self).__init__(name)
        self.name = name

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                ('Impedance using Resistance and Inductive Reactance', self.form_impedance),
                ('Impedance using Resistance and Power Factor', self.form_impedance4),
                ('Impedance using Total Volts and Total Amps', self.form_impedance2),
                ('Impedance using Total Volts and Volt Amps', self.form_impedance5),
                ('Impedance using Volt Amps and Total Volts', self.form_impedance3),
                ("Inductor Amps using Inductor VAR's and Inductive Reactance", self.form_iAmps3),
                ("Inductor Amps using Inductor VAR's and Inductor Volts", self.form_iAmps2),
                ('Inductor Amps using Inductor Volts and Inductive Reactance', self.form_iAmps),
                ('Inductor Rating using Inductive Reactance and Frequency', self.form_inductor),
                ('Inductive Reactance using Frequency and Inductor Rating', self.form_iReactance5),
                ("Inductive Reactance using Inductor VAR's and Inductor Amps", self.form_iReactance4),
                ('Inductive Reactance using Impedance and Resistance', self.form_iReactance),
                ('Inductive Reactance using Inductor Volts and Inductor Amps', self.form_iReactance2),
                ("Inductive Reactance using Inductor Volts and Inductor VAR's", self.form_iReactance3),
                ("Inductor VAR's using Inductor Amps and Inductive Reactance", self.form_VAR4),
                ("Inductor VAR's using Inductor Volts and Inductor Amps", self.form_VAR2),
                ("Inductor VAR's using Inductor Volts and Inductive Reactance", self.form_VAR3),
                ("Inductor VAR's using Volt Amps and Watts", self.form_VAR),
                ('Inductor Volts using Inductor Amps and Inductive Reactance', self.form_inductance),
                ("Inductor Volts using Inductor VAR's and Inductive Reactance", self.form_inductance3),
                ("Inductor Volts using Inductor VAR's and Inductor Amps", self.form_inductance4),
                ('Inductor Volts using Total Volts and Resistor Volts', self.form_inductance2),
                ('Power Factor using CoSine and Theta Angle', self.form_powerFactor4),
                ('Power Factor using Resistance and Impedance', self.form_powerFactor),
                ('Power Factor using Resistor Volts and Total Volts', self.form_powerFactor3),
                ('Power Factor using Watts and Volt Amps', self.form_powerFactor2),
                ('Resistance using Impedance and Inductive Reactance', self.form_resistance),
                ('Resistance using Impedance and Power Factor', self.form_resistance4),
                ('Resistance using Resistor Volts and Resistor Amps', self.form_resistance2),
                ('Resistance using Resistor Volts and Watts', self.form_resistance5),
                ('Resistance using Watts and Resistor Amps', self.form_resistance3),
                ('Resistor Amps using Resistor Volts and Resistance', self.form_rAmps),
                ('Resistor Amps using Watts and Resistor Volts', self.form_rAmps2),
                ('Resistor Amps using Watts and Resistance', self.form_rAmps3),
                ('Resistor Volts using Resistor Amps and Resistance', self.form_rVolts),
                ('Resistor Volts using Total Volts and Inductor Volts', self.form_rVolts4),
                ('Resistor Volts using Total Volts and Power Factor', self.form_rVolts5),
                ('Resistor Volts using Watts and Resistance', self.form_rVolts2),
                ('Resistor Volts using Watts and Resistor Amps', self.form_rVolts3),
                ('Total Amps using Total Volts and Impedance', self.form_tAmps),
                ('Total Amps using Volt Amps and Total Volts', self.form_tAmps2),
                ('Total Volts using Resistor Volts and Inductor Volts', self.form_tVolts),
                ('Total Volts using Resistor Volts and Power Factor', self.form_tVolts4),
                ('Total Volts using Total Amps and Impedance', self.form_tVolts2),
                ('Total Volts using Volt Amps and Total Amps', self.form_tVolts3),
                ('Volt Amps using Total Amps and Impedance', self.form_va2),
                ('Volt Amps using Total Volts and Total Amps', self.form_va),
                ('Volt Amps using Total Volts and Impedance', self.form_va3),
                ("Volt Amps using Watts and Inductor VAR's", self.form_va4),
                ('Volt Amps using Watts and Power Factor', self.form_va5),
                ('Watts using Resistor Amps and Resistance', self.form_watts4),
                ('Watts using Resistor Volts and Resistor Amps', self.form_watts),
                ('Watts using Resistor Volts and Resistance', self.form_watts3),
                ("Watts using Volt Amps and Inductor VAR's", self.form_watts2),
                ('Watts using Volt Amps and Power Factor', self.form_watts5),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            'Total Volts using Resistor Volts and Inductor Volts' : OrderedDict(
                [
                    ('number_input', 'Resistor Volts: '),
                    ('number_input2', 'Inductor Volts: ')
                ]
            ),
            'Total Volts using Total Amps and Impedance' : OrderedDict(
                [
                    ('number_input', 'Total Amps: '),
                    ('number_input2', 'Impedance: ')
                ]
            ),
            'Total Volts using Volt Amps and Total Amps' : OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Total Volts using Resistor Volts and Power Factor' : OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Power Factor: ')
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
            'Resistance using Impedance and Inductive Reactance':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            'Resistance using Resistor Volts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistance using Watts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps')
                    ]
            ),
            'Resistance using Impedance and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Resistance using Resistor Volts and Watts':OrderedDict(
                    [
                            ('number_input',  'Resistor Volts: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            'Impedance using Total Volts and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Impedance using Volt Amps and Total Volts':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Volts: ')
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
            'Watts using Resistor Volts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            "Watts using Volt Amps and Inductor VAR's":OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', "Inductor VAR's: ")
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
            'Inductor Volts using Inductor Amps and Inductive Reactance':OrderedDict(
                    [
                            ('number_input', 'Inductor Amps: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            'Inductor Volts using Total Volts and Resistor Volts':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Resistor Volts: ')
                    ]
            ),
            "Inductor Volts using Inductor VAR's and Inductive Reactance":OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            "Inductor Volts using Inductor VAR's and Inductor Amps":OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Amps: ')
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
            'Volt Amps using Total Volts and Impedance':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            "Volt Amps using Watts and Inductor VAR's":OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            'Volt Amps using Watts and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
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
                            ('numebr_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistor Volts using Total Volts and Inductor Volts':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Inductor Volts: ')
                    ]
            ),
            'Resistor Volts using Total Volts and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Inductor Rating using Inductive Reactance and Frequency':OrderedDict(
                    [
                            ('number_input', 'Inductive Reactance: '),
                            ('number_input2', 'Frequency: ')
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
            'Inductive Reactance using Impedance and Resistacne':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Inductive Reactance using Inductor Volts and Inductor Amps':OrderedDict(
                    [
                            ('numebr_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            "Inductive Reactance using Inductor Volts and Inductor VAR's":OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            "Inductive Reactance using Inductor VAR's and Inductor Amps":OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            'Inductive Reactance using Frequency and Inductor Rating':OrderedDict(
                    [
                            ('number_input', 'Frequency: '),
                            ('number_input2', 'Inductor Rating: ')
                    ]
            ),
            "Inductor VAR's using Volt Amps and Watts":OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            "Inductor VAR's using Inductor Volts and Inductor Amps":OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            "Inductor VAR's using Inductor Volts and Inductive Reactance":OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            "Inductor VAR's using Inductor Amps and Inductive Reactance":OrderedDict(
                    [
                            ('number_input', 'Inductor Amps: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            'Impedance using Resistance and Inductive Reactance':{              #self.form_impedance),
                '' : 'sqrt(Resistance^2 + Inductive Reactance^2)'
            },
            'Impedance using Resistance and Power Factor':{                     #self.form_impedance4),
                '' : 'Resistance / Power Factor'
            },
            'Impedance using Total Volts and Total Amps':{                      #self.form_impedance2),
                '' : 'Total Volts / Total Amps'
            },
            'Impedance using Total Volts and Volt Amps':{                       #self.form_impedance5),
                '' : 'Total Volts / Volt Amps'
            },
            'Impedance using Volt Amps and Total Volts':{                       #self.form_impedance3),
                '' : 'Volt Amps / Total Volts'
            },
            "Inductor Amps using Inductor VAR's and Inductive Reactance":{      #self.form_iAmps3),
                '' : "sqrt(Inductor VAR's / Inductive Reactance)"
            },
            "Inductor Amps using Inductor VAR's and Inductor Volts":{           #self.form_iAmps2),
                '' : "Inductor VAR's / Inductor Volts"
            },
            'Inductor Amps using Inductor Volts and Inductive Reactance':{      #self.form_iAmps),
                '' : "Inductor Volts / Inductive Reactance"
            },
            'Inductor Rating using Inductive Reactance and Frequency':{         #self.form_inductor),
                '' : 'Inductive Reactance / (2 * 3.14 * Frequency)'
            },
            'Inductive Reactance using Frequency and Inductor Rating':{         #self.form_iReactance5),
                '' : '2 * 3.14 * Frequency * Inductor Rating'
            },
            "Inductive Reactance using Inductor VAR's and Inductor Amps":{      #self.form_iReactance4),
                '' : "Inductor VAR's / Inductor Amps^2"
            },
            'Inductive Reactance using Impedance and Resistance':{              #self.form_iReactance),
                '' : 'sqrt(Impedance^2 - Resistance^2)'
            },
            'Inductive Reactance using Inductor Volts and Inductor Amps':{      #self.form_iReactance2),
                '' : 'Inductor Volts / Inductor Amps'
            },
            "Inductive Reactance using Inductor Volts and Inductor VAR's":{     #self.form_iReactance3),
                '' : "Inductor Volts^2 / Inductor VAR's"
            },
            "Inductor VAR's using Inductor Amps and Inductive Reactance":{      #self.form_VAR4),
                '' : 'Inductor Amps^2 * Inductive Reactance'
            },
            "Inductor VAR's using Inductor Volts and Inductor Amps":{           #self.form_VAR2),
                '' : 'Inductor Volts * Inductor Amps'
            },
            "Inductor VAR's using Inductor Volts and Inductive Reactance":{     #self.form_VAR3),
                '' : 'Inductor Volts^2 / Inductive Reactance'
            },
            "Inductor VAR's using Volt Amps and Watts":{                        #self.form_VAR),
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
            'Inductor Volts using Inductor Amps and Inductive Reactance':{      #self.form_inductance),
                '' : 'Inductor Amps * Inductive Reactance'
            },
            "Inductor Volts using Inductor VAR's and Inductive Reactance":{     #self.form_inductance3),
                '' : "sqrt(Inductor VAR's * Inductive Reactance)"
            },
            "Inductor Volts using Inductor VAR's and Inductor Amps":{           #self.form_inductance4),
                '' : "Inductor VAR's / Inductor Amps"
            },
            'Inductor Volts using Total Volts and Resistor Volts':{             #self.form_inductance2),
                '' : "sqrt(Total Volts^2 - Resistor Volts^2)"
            },
            'Power Factor using CoSine and Theta Angle':{                       #self.form_powerFactor4),
                '' : 'CoSine * Theta Angle'
            },
            'Power Factor using Resistance and Impedance':{                     #self.form_powerFactor),
                '' : 'Resistance / Impedance'
            },
            'Power Factor using Resistor Volts and Total Volts':{               #self.form_powerFactor3),
                '' : 'Resistor Volts / Total Volts'
            },
            'Power Factor using Watts and Volt Amps':{                          #self.form_powerFactor2),
                '' : "Watts / Volt Amps"
            },
            'Resistance using Impedance and Inductive Reactance':{              #self.form_resistance),
                '' : 'sqrt(Impedance^2 - Inductive Reactance^2)'
            },
            'Resistance using Impedance and Power Factor':{                     #self.form_resistance4),
                '' : 'Impedance / Power Factor^2'
            },
            'Resistance using Resistor Volts and Resistor Amps':{               #self.form_resistance2),
                '' : 'Resistor Volts / Resistor Amps'
            },
            'Resistance using Resistor Volts and Watts':{                       #self.form_resistance5),
                '' : 'Resistor Volts * Watts'
            },
            'Resistance using Watts and Resistor Amps':{                        #self.form_resistance3),
                '' : "Watts^2 / Resistor Amps"
            },
            'Resistor Amps using Resistor Volts and Resistance':{               #self.form_rAmps),
                '' : 'Resistor Volts / Resistance'
            },
            'Resistor Amps using Watts and Resistor Volts':{                    #self.form_rAmps2),
                '' : "Watts / Resistor Volts"
            },
            'Resistor Amps using Watts and Resistance':{                        #self.form_rAmps3),
                '' : 'sqrt(Watts / Resistance)'
            },
            'Resistor Volts using Resistor Amps and Resistance':{               #self.form_rVolts),
                '' : 'Resistor Amps * Resistance'
            },
            'Resistor Volts using Total Volts and Inductor Volts':{             #self.form_rVolts4),
                '' : 'sqrt(Total Volts^2 - Inductor Volts^2)'
            },
            'Resistor Volts using Total Volts and Power Factor':{               #self.form_rVolts5),
                '' : "Total Volts * Power Factor"
            },
            'Resistor Volts using Watts and Resistance':{                       #self.form_rVolts2),
                '' : 'sqrt(Watts * Resistance)'
            },
            'Resistor Volts using Watts and Resistor Amps':{                    #self.form_rVolts3),
                '' : 'Watts / Resistor Amps'
            },
            'Total Amps using Total Volts and Impedance':{                      #self.form_tAmps),
                '' : 'Total Volts / Impedance'
            },
            'Total Amps using Volt Amps and Total Volts':{                      #self.form_tAmps2),
                '' : 'Volt Amps / Total Volts'
            },
            'Total Volts using Resistor Volts and Inductor Volts':{             #self.form_tVolts),
                '' : 'sqrt(Resistor Volts^2 + Inductor Volts^2)'
            },
            'Total Volts using Resistor Volts and Power Factor':{               #self.form_tVolts4),
                '' : 'Resistor Volts / Power Factor'
            },
            'Total Volts using Total Amps and Impedance':{                      #self.form_tVolts2),
                '' : 'Total Amps * Impedance'
            },
            'Total Volts using Volt Amps and Total Amps':{                      #self.form_tVolts3),
                '' : 'Volt Amps / Total Amps'
            },
            'Volt Amps using Total Amps and Impedance':{                        #self.form_va2),
                '' : 'Total Amps^2 * Impedance'
            },
            'Volt Amps using Total Volts and Total Amps':{                      #self.form_va),
                '' : 'Total Volts * Total Amps'
            },
            'Volt Amps using Total Volts and Impedance':{                       #self.form_va3),
                '' : 'Total Volts^2 / Impedance'
            },
            "Volt Amps using Watts and Inductor VAR's":{                        #self.form_va4),
                '' : "sqrt(Watts^2 + Inductor VAR's^2)"
            },
            'Volt Amps using Watts and Power Factor':{                          #self.form_va5),
                '' : 'Watts / Power Factor'
            },
            'Watts using Resistor Amps and Resistance':{                        #self.form_watts4),
                '' : 'Resistor Amps^2 * Resistance'
            },
            'Watts using Resistor Volts and Resistor Amps':{                    #self.form_watts),
                '' : 'Resistor Volts * Resistor Amps'
            },
            'Watts using Resistor Volts and Resistance':{                       #self.form_watts3),
                '' : 'Resistor Volts^2 / Resistance'
            },
            "Watts using Volt Amps and Inductor VAR's":{                        #self.form_watts2),
                '' : "sqrt(Volt Amps^2 - Inductor VAR'^2)"
            },
            'Watts using Volt Amps and Power Factor':{                          #self.form_watts5),
                '' : 'Volt Amps * Power Factor'
            },
        }

#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def form_tVolts(self):
           title = 'Total Volts using Resistor Volts and Inductor Volts'
           arg1 = 'Enter Resistor Volts'
           arg2 = 'Enter Inductor Volts'
           argsOut = [title, arg1, arg2]
           argsIn = self.prompt(argsOut)
           result = sqrt((argsIn[0] ** 2) + ((argsIn[1] ** 2)))
           return (self.prec4(result), self.pluralize(result, 'Total Volt'))
            
    def form_tVolts2(self):
            title = 'Total Volts using Total Amps and Impedance'
            arg1 = 'Enter Total Amps'
            arg2 = 'Enter Impedance'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))
            
    def form_tVolts3(self):
            title = 'Total Volts using Volt Amps and Total Amps'
            arg1 = 'Enter Volt Amps'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))
            
    def form_tVolts4(self):
            title = 'Total Volts using Resistor Volts and Power Factor'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Power Factor'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))
            
    def form_powerFactor(self):
            title = 'Power Factor using Resistance and Impedance'
            arg1 = 'Enter Resistance'
            arg2 = 'Enter Impedance'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[0]
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))
    
    def form_powerFactor2(self):
            title = 'Power Factor using Watts and Volt Amps'
            arg1 = 'Enter Watts'
            arg2 = 'Enter Volt Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))
            
    def form_powerFactor3(self):
            title = 'Power Factor using Resistor Volts and Total Volts'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Total Volts'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))
    
    def form_powerFactor4(self):
            title = 'Power Factor using CoSine and Theta Angle'
            arg1 = 'Enter Cosine'
            arg2 = 'Enter Theta Angle'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Power Factor'))

    def form_resistance(self):
            title = 'Resistance using Impedance and Inductive Reactance'
            arg1 = 'Enter Impedance'
            arg2 = 'Enter Inductive Reactance'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_resistance2(self):
            title = 'Resistance using Resistor Volts and Resistor Amps'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Resistor Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1] 
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_resistance3(self):
            title = 'Resistance using Watts and Resistor Amps'
            arg1 = 'Enter Watts'
            arg2 = 'Enter Resistor Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0] ** 2) / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistance'))
    
    def form_resistance4(self):
            title = 'Resistance using Impedance and Power Factor'
            arg1 = 'Enter Impedance'
            arg2 = 'Enter Power Factor'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / (argsIn[1] ** 2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_resistance5(self):
            title = 'Resistance using Resistor Volts and Watts'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Watts'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_impedance(self):
            title = 'Impedance using Resistance and Inductive Reactance'
            arg1 = 'Enter Resistance'
            arg2 = 'Enter Inductive Reactance'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) + (argsIn[1] ** 2))
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_impedance2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_impedance3(self):
            title = 'Impedance using Volt Amps and Total Volts'
            arg1 = 'Enter Volt Amps'
            arg2 = 'Enter Total Volts'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_impedance4(self):
            title = 'Impedance using Resistance and Power Factor'
            arg1 = 'Enter Resistance'
            arg2 = 'Enter Power Factor'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_impedance5(self):
            title = 'Impedance using Total Volts and Volt Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Volt Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_watts(self):
            title = 'Watts using Resistor Volts and Resistor Amps'
            arg1 = 'Enter Resistor Votls'
            arg2 = 'Enter Resistor Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_watts2(self):
            title = "Watts using Volt Amps and Inductor VAR's"
            arg1 = 'Enter Volt Amps'
            arg2 = "Enter Inductor VAR's"
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] ** 2) - (argsIn[1] ** 2))
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_watts3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0] **2) / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_watts4(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0]**2) * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_watts5(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_inductance(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_inductance2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] **2) - (argsIn[1] **2))
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_inductance3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] * argsIn[1])
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_inductance4(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_iAmps(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_iAmps2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_iAmps3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] / argsIn[1])
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_va(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_va2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0]**2) * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_va3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0]**2) / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_va4(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) + (argsIn[1]**2))
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_va5(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_rVolts(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts2(self):	
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] * argsIn[1])
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts4(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_rVolts5(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_inductor(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / (2*3.14*argsIn[1])
            return (self.prec4(result), self.pluralize(result, 'Inductor Size'))

    def form_tAmps(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_tAmps2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_rAmps(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_rAmps2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_rAmps3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] / argsIn[1])
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_iReactance(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0]**2) / argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance4(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / (argsIn[1]**2)
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_iReactance5(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = 2*3.14*argsIn[0]*argsIn[1]
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance Rating'))

    def form_VAR(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0]**2) - (argsIn[1]**2))
            return (self.prec4(result), self.pluralize(result, "Inductor VAR'"))

    def form_VAR2(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (self.prec4(result), self.pluralize(result, "Inductor VAR'"))

    def form_VAR3(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0]**2) / argsIn[1]
            return (self.prec4(result), self.pluralize(result, "Inductor VAR'"))

    def form_VAR4(self):
            title = 'Impedance using Total Volts and Total Amps'
            arg1 = 'Enter Total Volts'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = (argsIn[0]**2) * argsIn[1]
            return (self.prec4(result), self.pluralize(result, "Inductor VAR'"))

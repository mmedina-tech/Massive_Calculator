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
        
#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                ('Impedance using Resistance and Inductive Reactance', self.form_Impedance),
                ('Impedance using Total Volts and Total Amps', self.form_Impedance2),
                ('Impedance using Total Volts and Volt Amps', self.form_Impedance3),
                ('Impedance using Volt Amps and Total Amps', self.form_Impedance4),
                ('Impedance using Resistance and Power Factor', self.form_Impedance5),
                ('Inductive Reactance using Frequency and Inductor Rating', self.form_InductRe3),
                ('Inductive Reactance using Impedance and Resistance', self.form_InductRe4),
                ("Inductive Reactance using Inductor VAR's and Inductor Amps", self.form_InductRe2),
                ('Inductive Reactance using Inductor Volts and Inductor Amps', self.form_InductRe5),
                ("Inductive Reactance using Inductor Volts and Inductor VAR's", self.form_InductRe),
                ("Inductor Amps using Inductor VAR's and Inductor Volts", self.form_InductA3),
                ("Inductor Amps using Inductor VAR's and Inductive Reactance", self.form_InductA4),
                ('Inductor Amps using Inductor Volts and Inductive Reactance', self.form_InductA2),
                ('Inductor Amps using Total Amps and Resistor Amps', self.form_InductA), 
                ('Inductor Rating using Inductive Reactance and Frequency', self.form_InductorRating),
                ("Inductor VAR's using Inductor Amps and Inductive Reactance", self.form_InductorV),
                ("Inductor VAR's using Inductor Volts and Inductor Amps", self.form_InductorV3),
                ("Inductor VAR's using Inductor Volts and Inductive Reactance", self.form_InductorV4),
                ("Inductor VAR's using Volt Amps and Watts", self.form_InductorV2),
                ("Inductor Volts using Inductor VAR's and Inductive Reactance", self.form_InductV),
                ('Inductor Volts using Inductor Amps and Inductive Reactance', self.form_InductV2),
                ("Inductor Volts using Inductor VAR's and Inductor Amps", self.form_InductV3),
                ('Power Factor using CoSine and Theta Angle', self.form_Power4),
                ('Power Factor using Impedance and Resistance', self.form_Power),
                ('Power Factor using Resistor Amps and Total Amps', self.form_Power3),
                ('Power Factor using Watts and Volt Amps', self.form_Power2),
                ('Resistance using Impedance and Inductive Reactance', self.form_Resistance3),
                ('Resistance using Impedance and Power Factor', self.form_Resistance4),
                ('Resistance using Resistor Volts and Resistor Amps', self.form_Resistance),
                ('Resistance using Watts and Resistor Amps', self.form_Resistance2),
                ('Resistor Amps using Resistor Volts and Resistance', self.form_ResistA2),
                ('Resistor Amps using Total Amps and Inductor Amps', self.form_ResistA),
                ('Resistor Amps using Total Amps and Power Factor', self.form_ResistA5),
                ('Resistor Amps using Watts and Resistance', self.form_ResistA3),
                ('Resistor Amps using Watts and Resistor Volts', self.form_ResistA4),
                ('Resistor Volts using Resistor Amps and Resistance', self.form_ResistV),
                ('Resistor Volts using Watts and Resistance', self.form_ResistV2),
                ('Resistor Volts using Watts and Resistor Amps', self.form_ResistV3),
                ('Total Amps using Resistor Amps and Inductor Amps', self.form_TAmps),
                ('Total Amps using Resistor Amps and Power Factor', self.form_TAmps5),
                ('Total Amps using Total Volts and Impedance', self.form_TAmps2),
                ('Total Amps using Volt Amps and Total Volts', self.form_TAmps3),
                ('Total Amps using Volt Amps and Impedance', self.form_TAmps4),
                ('Total Volts using Total Amps and Impedance', self.form_TVolts3),
                ('Total Volts using Volt Amps and Impedance', self.form_TVolts2),
                ('Total Volts using Volt Amps and Total Amps', self.form_TVolts),
                ('Volt Amps using Total Amps and Impedance', self.form_VoltA2),
                ('Volt Amps using Total Volts and Impedance', self.form_VoltA3),
                ('Volt Amps using Total Volts and Total Amps', self.form_VoltA),
                ("Volt Amps using Watts and Inductor VAR's", self.form_VoltA4),
                ('Volt Amps using Watts and Power Factor', self.form_VoltA5),
                ('Watts using Resistor Amps and Resistance', self.form_Watts4),
                ('Watts using Resistor Volts and Resistance', self.form_Watts2),
                ('Watts using Resistor Volts and Resistor Amps', self.form_Watts),
                ("Watts using Volt Amps and Inductor VAR's", self.form_Watts5),
                ('Watts using Volt Amps and Power Factor', self.form_Watts3),
            ]
        )
#}}}_________________________________________________________________________________________
         
#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            'Impedance using Resistance and Inductive Reactance':OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            'Impedance using Total Volts and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Impedance using Total Volts and Volt Amps':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Volt Amps: ')
                    ]
            ),
            'Impedance using Volt Amps and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Power Factor using Impedance and Resistance':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Power Factor using Watts and Volt Amps':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Volt Amps: ')
                    ]
            ),
            'Power Factor using Resistor Amps and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Total Amps: ')
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
            'Impedance using Resistance and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Volt Amps using Watts and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Inductive Reactance using Inductor Volts and Inductor Amps':OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            "Inductor VAR's using Inductor Amps and Inductive Reactance":OrderedDict(
                    [
                            ('number_input', 'Inductor Amps: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            "Inductor VAR's using Inductor Volts and Inductor Amps":OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductor Amp: ')
                    ]
            ),
            "Inductor VAR's using Inductor Volts and Inductive Reactance":OrderedDict(
                    [
                            ('number_Input', 'Inductor Volts: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            'Resistance using Resistor Volts and Watts':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            'Total Volts using Volt Amps and Total Amps':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Total Amps: ')
                    ]
            ),
            'Total Volts using Volt Amps and Impedance':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Impedance: ')
                    ]
            ),
            'Total Amps using Resistor Amps and Inductor Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            'Total Amps using Total Volt and Impedance':OrderedDict(
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
            'Total Amps using Volt Amps and Impedance':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Impedance: ')
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
            'Inductive Reactance using Impedance and Resistance':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Inductor Amps using Total Amps and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Inductor Amps using Inductor Volts and Inductive Reactance':OrderedDict(
                    [
                            ('number_input', 'Inductor Volts: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            "Inductor Amps using Inductor VAR's and Inductor Volts":OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductor Volts: ')
                    ]
            ),
            "Inductor Amps using Inductor VAR's and Inductive Reactance":OrderedDict(
                    [
                            ('number_input', "Inductor VAR's: "),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            'Inductor Rating using Inductive Reactance and Frequency':OrderedDict(
                    [
                            ('number_input', 'Inducive Reactance: '),
                            ('number_input2', 'Frequency: ')
                    ]
            ),
            'Volt Amps using Total Volts and Impedance':OrderedDict(
                    [
                            ('number_input', 'Total Volts: '),
                            ('number_input2', 'Impedance: ')
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
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistance using Impedance and Inductive Reactance':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Inductive Reactance: ')
                    ]
            ),
            'Resistance using Impedance and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Impedance: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Resistor Volts using Resistor Amps and Resistance': OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Resistor Volts using Watts and Resistance': OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Resistor Volts using Watts and Resistor Amps': OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistor Amps using Total Amps and Inductor Amps': OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Inductor Amps: ')
                    ]
            ),
            'Resistor Amps using Resistor Volts and Resistance':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Total Amps using Resistor Amps and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Watts using Resistor Volts and Resistor Amps':OrderedDict(
                    [
                            ('number_input', 'Resistor Volts: '),
                            ('number_input2', 'Resistor Amps: ')
                    ]
            ),
            'Resistor Amps using Watts and Resistance':OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            'Watts using Resistor Volts and Resistance':OrderedDict(
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
            'Watts using Volt Amps and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
            'Watts using Resistor Amps and Resistance':OrderedDict(
                    [
                            ('number_input', 'Resistor Amps: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
            "Watts using Volt Amps and Inductor VAR's":OrderedDict(
                    [
                            ('number_input', 'Volt Amps: '),
                            ('number_input2', "Inductor VAR's: ")
                    ]
            ),
            'Resistor Amps using Total Amps and Power Factor':OrderedDict(
                    [
                            ('number_input', 'Total Amps: '),
                            ('number_input2', 'Power Factor: ')
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Impedance using Resistance and Inductive Reactance':{              #, self.form_Impedance),
                '' : '1 / ((1 / Resistance^2) + (1 / Inductive Reactance^2))'
            },
            'Impedance using Total Volts and Total Amps':{                      #, self.form_Impedance2),
                '' : 'Total Volts / Total Amps'
            },
            'Impedance using Total Volts and Volt Amps':{                       #, self.form_Impedance3),
                '' : 'Total Volts / Volt Amps'
            },
            'Impedance using Volt Amps and Total Amps':{                        #, self.form_Impedance4),
                '' : 'Volt Amps / Total Amps'
            },
            'Impedance using Resistance and Power Factor':{                     #, self.form_Impedance5),
                '' : 'Resistance * Power Factor'
            },
            'Inductive Reactance using Frequency and Inductor Rating':{         #, self.form_InductRe3),
                '' : '2 * 3.14 * Frequency * Inductor Rating'
            },
            'Inductive Reactance using Impedance and Resistance':{              #, self.form_InductRe4),
                '' : '1 / (1 / Impedance^2 - Resistacne^2)'
            },
            "Inductive Reactance using Inductor VAR's and Inductor Amps":{      #, self.form_InductRe2),
                '' : "Inudctor VAR's / Inductor Amps^2"
            },
            'Inductive Reactance using Inductor Volts and Inductor Amps':{      #, self.form_InductRe5),
                '' : 'Inductor Volts / Inductor Amps'
            },
            "Inductive Reactance using Inductor Volts and Inductor VAR's":{     #, self.form_InductRe),
                '' : "Inductor Volts^2 / Inductor VAR's"
            },
            "Inductor Amps using Inductor VAR's and Inductor Volts":{           #, self.form_InductA3),
                '' : "Inductor VAR's / Inductor Volts"
            },
            "Inductor Amps using Inductor VAR's and Inductive Reactance":{      #, self.form_InductA4),
                '' : "sqrt(Inductor VAR's / Inductive Reactance)"
            },
            'Inductor Amps using Inductor Volts and Inductive Reactance':{      #, self.form_InductA2),
                '' : 'Inductor Volts / Inductive Reactance'
            },
            'Inductor Amps using Total Amps and Resistor Amps':{                #, self.form_InductA), 
                '' : 'sqrt(Total Amps^2 - Resistor Amps^2)'
            },
            'Inductor Rating using Inductive Reactance and Frequency':{         #, self.form_InductorRating),
                '' : 'Inductive Reactance / (2 * 3.14 * Frequency)'
            },
            "Inductor VAR's using Inductor Amps and Inductive Reactance":{      #, self.form_InductorV),
                '' : 'Inductor Amps^2 * Inductive Reactance'
            },
            "Inductor VAR's using Inductor Volts and Inductor Amps":{           #, self.form_InductorV3),
                '' : 'Inductor Volts * Inductor Amps'
            },
            "Inductor VAR's using Inductor Volts and Inductive Reactance":{     #, self.form_InductorV4),
                '' : 'Inductor Volts^2 / Inductive Reactance'
            },
            "Inductor VAR's using Volt Amps and Watts":{                        #, self.form_InductorV2),
                '' : 'sqrt(Volt Amps^2 - Watts^2)'
            },
            "Inductor Volts using Inductor VAR's and Inductive Reactance":{     #, self.form_InductV),
                '' : "Inductor VAR's * Inductive Reactance"
            },
            'Inductor Volts using Inductor Amps and Inductive Reactance':{      #, self.form_InductV2),
                '' : 'sqrt(Inductor Amps * Inductive Reactance)'
            },
            "Inductor Volts using Inductor VAR's and Inductor Amps":{           #, self.form_InductV3),
                '' : "Inductor VAR's / Inductor Amps"
            },
            'Power Factor using CoSine and Theta Angle':{                       #, self.form_Power4),
                '' : 'CoSine * Theta Angle'
            },
            'Power Factor using Impedance and Resistance':{                     #, self.form_Power),
                '' : 'Impedance / Resistance'
            },
            'Power Factor using Resistor Amps and Total Amps':{                 #, self.form_Power3),
                '' : 'Resistor Amps / Total Amps'
            },
            'Power Factor using Watts and Volt Amps':{                          #, self.form_Power2),
                '' : 'Watts / Volt Amps'
            },
            'Resistance using Impedance and Inductive Reactance':{              #, self.form_Resistance3),
                '' : '1 / sqrt(Impedance^2 - Inductive Reactance^2)'
            },
            'Resistance using Impedance and Power Factor':{                     #, self.form_Resistance4),
                '' : 'Impedance / Power Factor'
            },
            'Resistance using Resistor Volts and Resistor Amps':{               #, self.form_Resistance),
                '' : 'Resistor Volts / Resistor Amps'
            },
            'Resistance using Watts and Resistor Amps':{                        #, self.form_Resistance2),
                '' : 'Watts / Resistor Amps^2'
            },
            'Resistor Amps using Resistor Volts and Resistance':{               #, self.form_ResistA2),
                '' : 'Resistor Volts / Resistance'
            },
            'Resistor Amps using Total Amps and Inductor Amps':{                #, self.form_ResistA),
                '' : 'sqrt(Total Amps^2 - Inductor Amps^2)'
            },
            'Resistor Amps using Total Amps and Power Factor':{                 #, self.form_ResistA5),
                '' : 'Total Amps * Power Factor'
            },
            'Resistor Amps using Watts and Resistance':{                        #, self.form_ResistA3),
                '' : 'sqrt(Watts / Resistance)'
            },
            'Resistor Amps using Watts and Resistor Volts':{                    #, self.form_ResistA4),
                '' : 'Watts / Resistor Volts'
            },
            'Resistor Volts using Resistor Amps and Resistance':{               #, self.form_ResistV),
                '' : 'Resistor Amps * Resistance'
            },
            'Resistor Volts using Watts and Resistance':{                       #, self.form_ResistV2),
                '' : 'sqrt(Watts * Resistance)'
            },
            'Resistor Volts using Watts and Resistor Amps':{                    #, self.form_ResistV3),
                '' : 'Watts / Resistor Amps^2'
            },
            'Total Amps using Resistor Amps and Inductor Amps':{                #, self.form_TAmps),
                '' : 'sqrt(Resistor Amps^2 + Inductor Amps^2)'
            },
            'Total Amps using Resistor Amps and Power Factor':{                 #, self.form_TAmps5),
                '' : 'Resistor Amps / Power Factor'
            },
            'Total Amps using Total Volts and Impedance':{                      #, self.form_TAmps2),
                '' : 'Total Volts / Impedance'
            },
            'Total Amps using Volt Amps and Total Volts':{                      #, self.form_TAmps3),
                '' : 'Volt Amps / Total Volts'
            },
            'Total Amps using Volt Amps and Impedance':{                        #, self.form_TAmps4),
                '' : 'sqrt(Volt Amps / Impedance)'
            },
            'Total Volts using Total Amps and Impedance':{                      #, self.form_TVolts3),
                '' : 'Total Amps * Impedance'
            },
            'Total Volts using Volt Amps and Impedance':{                       #, self.form_TVolts2),
                '' : 'sqrt(Volt Amps * Impedance)'
            },
            'Total Volts using Volt Amps and Total Amps':{                      #, self.form_TVolts),
                '' : 'Volt Amps / Total Amps'
            },
            'Volt Amps using Total Amps and Impedance':{                        #, self.form_VoltA2),
                '' : 'Total Amps^2 * Impedance'
            },
            'Volt Amps using Total Volts and Impedance':{                       #, self.form_VoltA3),
                '' : 'Total Volts^2 / Impedance'
            },
            'Volt Amps using Total Volts and Total Amps':{                      #, self.form_VoltA),
                '' : 'Total Volts * Total Amps'
            },
            "Volt Amps using Watts and Inductor VAR's":{                        #, self.form_VoltA4),
                '' : "sqrt(Watts^2 + Inductor VAR's^2)"
            },
            'Volt Amps using Watts and Power Factor':{                          #, self.form_VoltA5),
                '' : 'Watts / Power Factor'
            },
            'Watts using Resistor Amps and Resistance':{                        #, self.form_Watts4),
                '' : 'Resistor Amps^2 * Resistance'
            },
            'Watts using Resistor Volts and Resistance':{                       #, self.form_Watts2),
                '' : 'sqrt(Resistor Volts^2 / Resistance^2)'
            },
            'Watts using Resistor Volts and Resistor Amps':{                    #, self.form_Watts),
                '' : 'Resistor Volts * Resistor Amps'
            },
            "Watts using Volt Amps and Inductor VAR's":{                        #, self.form_Watts5),
                '' : "Volt Amps * Inductor VAR's"
            },
            'Watts using Volt Amps and Power Factor':{                          #, self.form_Watts3),
                '' : 'Volt Amps^2 / Power Factor'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def form_Impedance(self, num, num2):
            result = 1/((1/float(num)**2) + (1/float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance3(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance4(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

    def form_Impedance5(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Impedance'))

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

    def form_VoltA(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VoltA2(self, num, num2):
            result = (float(num)**2) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VoltA3(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VoltA4(self, num, num2):
            result = sqrt((float(num)**2) + (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_VoltA5(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_InductorV(self, num, num2):
            result = (float(num)**2) * float(num2)
            return (self.prec4(result), self.pluralize(result, "Inductor VAR"))

    def form_InductorV2(self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Inductor VAR'))

    def form_InductorV3(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductor VAR'))

    def form_InductorV4(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductor VAR'))

    def form_TVolts(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts2(self, num, num2):
            result = sqrt(float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TVolts3(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Volt'))

    def form_TAmps(self, num, num2):
            result = sqrt((float(num)**2) + (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_TAmps2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_TAmps3(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_TAmps4(self, num, num2):
            result = sqrt(float(num) / float(num2))
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_InductRe(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe2(self, num, num2):
            result = float(num) / (float(num2)**2)
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe3(self, num, num2):
            result = 2*3.14*float(num)*float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe4(self, num, num2):
            result = 1/(1/(float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance'))

    def form_InductRe5(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductive Reactance'))

    def form_InductV(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_InductV2(self, num, num2):
            result = sqrt(float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_InductV3(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductor Volt'))

    def form_InductA(self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_InductA2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_InductA3(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_InductA4(self, num, num2):
            result = sqrt(float(num) / float(num2))
            return (self.prec4(result), self.pluralize(result, 'Inductor Amp'))

    def form_VoltA6(self, num, num2):
            result = (float(num)**2) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Volt Amp'))

    def form_InductorRating(self, num, num2):
            result = float(num) / (2*3.14*float(num2))
            return (self.prec4(result), self.pluralize(result, 'Inductor Rating'))

    def form_Resistance(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance2(self, num, num2):
            result = float(num) / (float(num2)**2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_Resistance3(self, num, num2):
            result = 1/sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Resistance'))
    
    def form_Resistance4(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistance'))

    def form_ResistV(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_ResistV2(self, num, num2):
            result = sqrt(float(num) * float(num2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_ResistV3(self, num, num2):
            result = float(num) / (float(num2)**2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_ResistV4(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Volt'))

    def form_ResistA(self, num, num2):
            result = sqrt((float(num)**2) - (float(num2)**2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA2(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA3(self, num, num2):
            result = sqrt(float(num) / float(num2))
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA4(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_ResistA5(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Resistor Amp'))

    def form_TAmps5(self, num, num2):
            result = float(num) / float(num2)
            return (self.prec4(result), self.pluralize(result, 'Total Amp'))

    def form_Watts(self, num, num2):
            result = float(num) * float(num2)
            return (self.prec4(result), self.pluralize(result, 'Watt'))

    def form_Watts2(self, num, num2):
            result = sqrt((float(num)**2) / (float(num2)**2))
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
#}}}_________________________________________________________________________________________

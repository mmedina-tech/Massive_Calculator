#!/usr/bin/python
#
# OhmsLaw.py
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

class OhmsLaw(FormulaBase):
    def __init__(self, name):
        super(OhmsLaw, self).__init__(name)
        self.name = name 
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Volts using Amps and Resistance',
            2 : 'Volts using Watts and Amps',
            3 : 'Volts using Watts and Resistance',
            4 : 'Amps using Volts and Resistance',
            5 : 'Amps using Watts and Volts',
            6 : 'Amps using Watts and Resistance',
            7 : 'Resistance using Volts and Amps',
            8 : 'Resistance using Watts and Amps',
            9 : 'Resistance using Volts and Watts',
            10 : 'Watts using Volts and Amps',
            11 : 'Watts using Resistance and Amps',
            12 : 'Watts using Volts and Resistance',
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_voltsar),
                (self.function_strings[2], self.form_voltswa),
                (self.function_strings[3], self.form_voltswr),
                (self.function_strings[4], self.form_ampsvr),
                (self.function_strings[5], self.form_ampswv),
                (self.function_strings[6], self.form_ampswr),
                (self.function_strings[7], self.form_resisva),
                (self.function_strings[8], self.form_resiswa),
                (self.function_strings[9], self.form_resisvw),
                (self.function_strings[10], self.form_wattsva),
                (self.function_strings[11], self.form_wattsra),
                (self.function_strings[12], self.form_wattsvr),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1] : OrderedDict(
                [
                    ('number_input' , 'Amps: '),
                    ('number_input2' , 'Resistance: ')
                ]
            ),
            self.function_strings[3] :OrderedDict(
                [
                    ('number_input', 'Watts: '),
                    ('number_input2', 'Resistance: ')
                ]
            ),
            self.function_strings[2] : OrderedDict(
                [    
                    ('number_input', 'Watts: '),
                    ('number_input2', 'Amps: ')
                ]
            ),
            self.function_strings[4] : OrderedDict(
                [
                    ('number_input', 'Volts: '),
                    ('number_input2', 'Resistance: ')
                ]
            ),
            self.function_strings[5] : OrderedDict(
                [
                    ('number_input', 'Watts: '),
                    ('number_input2', 'Volts: ')
                ]
            ),
            self.function_strings[6] : OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Resistacne: ')
                    ]
            ),
            self.function_strings[7] : OrderedDict(
                    [
                            ('number_input', 'Volts: '),
                            ('number_input2', 'Amps: ')
                    ]
            ),
            self.function_strings[8] : OrderedDict(
                    [
                            ('number_input', 'Watts: '),
                            ('number_input2', 'Amps: ')
                    ]
            ),
            self.function_strings[9] :OrderedDict(
                    [
                            ('number_input', 'Volts: '),
                            ('number_input2', 'Watts: ')
                    ]
            ),
            self.function_strings[10]: OrderedDict(
                    [
                            ('number_input', 'Volts: '),
                            ('number_input2', 'Amps: ')
                    ]
            ),
            self.function_strings[11]:OrderedDict(
                    [
                            ('number_input', 'Resistance: '),
                            ('number_input2', 'Amps: ')
                    ]
            ),
            self.function_strings[12]:OrderedDict(
                    [
                            ('number_input', 'Volts: '),
                            ('number_input2', 'Resistance: ')
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{
                '' : 'Amps * Resistance'
            },
            self.function_strings[2]:{
                '' : 'Watts / Amps'
            },
            self.function_strings[3]:{
                '' : 'sqrt(Watts * Resistance)'
            },
            self.function_strings[4]:{
                '' : 'Volts / Resistance'
            },
            self.function_strings[5]:{
                '' : 'Watts / Volts'
            },
            self.function_strings[6]:{
                '' : 'sqrt(Watts / Resistance)'
            },
            self.function_strings[7]:{
                '' : 'Volts / Amps'
            },
            self.function_strings[8]:{
                '' : 'sqrt(Watts / Amps<sup>2</sup>)'
            },
            self.function_strings[9]:{
                '' : 'Volts<sup>2</sup> / Watts'
            },
            self.function_strings[10]:{
                '' : 'Volts * Amps'
            },
            self.function_strings[11]:{
                '' : 'Resistance * Amps<sup>2</sup>'
            },
            self.function_strings[12]:{
                '' : 'Volts<sup>2</sup> / Resistance'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Functions _____________________________________________________________________________

    def form_voltsar(self):
        argsOut = [self.function_strings[1], 'Enter Amps', 'Enter Resistance']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (result, self.pluralize(result, 'Volt'))
            
    def form_voltswa(self):
        argsOut = [self.function_strings[2], 'Enter Watts', 'Enter Amps']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Volt'))
            
    def form_voltswr(self):
        argsOut = [self.function_strings[3], 'Enter Watts', 'Enter Resistance']
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] * argsIn[1]) 
        return (result, self.pluralize(result, 'Volt'))
            
    def form_ampsvr(self):
        argsOut = [self.function_strings[4], 'Enter Volts', 'Enter Resistance']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Amp'))
            
    def form_ampswv(self):
        argsOut = [self.function_strings[5], 'Enter Watts', 'Enter Volts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Amp'))
            
    def form_ampswr(self):
        argsOut = [self.function_strings[6], 'Enter Watts', 'Enter Resistance']
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / argsIn[1])
        return (result, self.pluralize(result, 'Amp'))
            
    def form_resisva(self):
        argsOut = [self.function_strings[7], 'Enter Volts', 'Enter Amps']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Resistance'))
            
    def form_resiswa(self):
        argsOut = [self.function_strings[8], 'Enter Watts', 'Enter Amps']
        argsIn = self.prompt(argsOut)
        result = sqrt(argsIn[0] / (argsIn[1] ** 2))
        return (result, self.pluralize(result, 'Resistance'))
            
    def form_resisvw(self):
        argsOut = [self.function_strings[9], 'Enter Volts', 'Enter Watts']
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (result, self.pluralize(result, 'Resistance'))
            
    def form_wattsva(self):
        argsOut = [self.function_strings[10], 'Enter Volts', 'Enter Amps']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (result, self.pluralize(result, 'Watt'))
            
    def form_wattsra(self):
        argsOut = [self.function_strings[11], 'Enter Resistance', 'Enter Amps']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * (argsIn[1] ** 2)
        return (result, self.pluralize(result, 'Watt'))
            
    def form_wattsvr(self):
        argsOut = [self.function_strings[12], 'Enter Volts', 'Enter Resistacne']
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] ** 2) / argsIn[1]
        return (result, self.pluralize(result, 'Watt'))
            
#}}}_________________________________________________________________________________________


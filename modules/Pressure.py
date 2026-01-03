#!/usr/bin/env python3
#
# Pressure.py
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

class Pressure(FormulaBase):
    def __init__(self, name): 
        super(Pressure, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Bars to KiloPascals',
            2 : 'Bars to PSI',
            3 : 'Inches of Mercury to KiloPascals',
            4 : 'Inches of Water to KiloPascals',
            5 : 'KiloPascals to Bars',
            6 : 'KiloPascals to Inches of Mercury',
            7 : 'KiloPascals to PSI',
            8 : 'Pascals to Pounds per Square Foot',
            9 : 'Pounds per Square Foot to Pascals',
            10 : 'PSI to KiloPascals',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.bars),
                (self.function_strings[2], self.bars2),
                (self.function_strings[3], self.InHg),
                (self.function_strings[4], self.InH2O),
                (self.function_strings[5], self.kbars),
                (self.function_strings[6], self.KpHg),
                (self.function_strings[7], self.KpPSI),
                (self.function_strings[8], self.pascal),
                (self.function_strings[9], self.psf),
                (self.function_strings[10], self.PSI),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1]:{
                    'number_input' : 'Bars: '
            },
            self.function_strings[2]:{
                    'number_input' : 'Bars: '
            },
            self.function_strings[3]:{
                    'number_input' : 'Inches ot Mercury: '
            },
            self.function_strings[4]:{
                    'number_input' : 'Inches of Water: '
            },
            self.function_strings[5]:{
                    'number_input' : 'KiloPascals: '
            },
            self.function_strings[6]:{
                    'number_input' : 'KiloPascals: '
            },
            'KiloPascals to Inches of Water':{
                    'number_input' : 'KiloPascals: '
            },
            self.function_strings[8]:{
                    'number_input' : 'Pascals: '
            },
            self.function_strings[9]:{
                    'number_input' : 'Pounds: '
            },
            self.function_strings[10]:{
                    'number_input' : 'PSI: '
            },
            self.function_strings[7]:{
                "number_input" : "KiloPascals (input): "
            },
        }    
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[3]:{
                '' : 'Inches of Mercury * 3.377'
            },
            self.function_strings[6]:{
                '' : 'KiloPascals * 0.2961'
            },
            self.function_strings[10]:{
                '' : 'PSI * 6.895'
            },
            self.function_strings[7]:{
                '' : 'KiloPascals * 0.145'
            },
            self.function_strings[4]:{
                '' : 'Inches of Water * 0.2488'
            },
            self.function_strings[1]:{
                '' : 'Bars * 100'
            },
            self.function_strings[5]:{
                '' : 'KiloPascals * 0.01'
            },
            self.function_strings[8]:{
                '' : 'Pascals * 0.02088'
            },
            self.function_strings[9]:{
                '' : 'Pounds per Square Foot * 47.88'
            },
            self.function_strings[2]:{
                '' : '(Bars * 100) * .145'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def InHg (self):
        title = self.function_strings[3]
        InHg = "Enter Inches of Mercury"
        argsOut = [title, InHg]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.377
        return (result, self.pluralize(result, 'KiloPascal'))

    def KpHg (self):
        title = self.function_strings[6]
        Kp = "Enter KiloPascals"
        argsOut = [title, Kp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2961
        return (result, self.pluralize(result, 'Inches of Mercury'))

    def PSI (self):
        title = self.function_strings[10]
        psi = "Enter PSI"
        argsOut = [title, psi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 6.895
        return (result, self.pluralize(result, 'KiloPascal'))

    def KpPSI (self):
        title = self.function_strings[7]
        Kp = "Enter KiloPascals"
        argsOut = [title, Kp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .145
        return (result, self.pluralize(result, 'PSI'))
    
    def InH2O (self):
        title = self.function_strings[4]
        InH2O = "Enter Inches of Water"
        argsOut = [title, InH2O]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2488
        return (result, self.pluralize(result, 'KiloPascal'))

    def bars (self):
        title = self.function_strings[1]
        bar = "Enter Bars"
        argsOut = [title, bar]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 100
        return (result, self.pluralize(result, 'KiloPascal'))

    def kbars (self):
        title = self.function_strings[5]
        Kp = "Enter KiloPascals"
        argsOut = [title, Kp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .01
        return (result, self.pluralize(result, 'Bar'))

    def psf (self):
        title = self.function_strings[9]
        psf = "Enter Pounds per Square Foot"
        argsOut = [title, psf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 47.88
        return (result, self.pluralize(result, 'Pascal'))

    def pascal (self):
        title = self.function_strings[8]
        pas = "Enter Pascal"
        argsOut = [title, pas]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .02088
        return (result, self.pluralize(result, 'Pounds per Square Foot'))

    def bars2 (self):
        title = self.function_strings[2]
        bar = "Enter Bars"
        argsOut = [title, bar]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] * 100) * .145
        return (result, self.pluralize(result, 'PSI'))
#}}}_________________________________________________________________________________________


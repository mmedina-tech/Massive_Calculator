#!/usr/bin/env python3
#
# Mass.py
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

class Mass(FormulaBase):
    def __init__(self, name):
        super (Mass, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Tons to Kilograms',
            2 : 'Kilograms to Tons',
            3 : 'Tons to Metric Tons',
            4 : 'Metric Tons to Tons',
            5 : 'Grains to Drams',
            6 : 'Grains to Ounces',
            7 : 'Grains to Grams',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.tons),
                (self.function_strings[2], self.kilo),
                (self.function_strings[3], self.tons2),
                (self.function_strings[4], self.tons3),
                (self.function_strings[5], self.grains),
                (self.function_strings[6], self.grains2),
                (self.function_strings[7], self.grains3),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[1]:{
                'number_input' : 'Tons (input): '
            },
            self.function_strings[2]:{
                'number_input' : 'Kilograms (input): '
            },
            self.function_strings[3]:{
                'number_input' : 'Tons (input): '
            },
            self.function_strings[4]:{
                'number_input' : 'Metric Tons (input): '
            },
            self.function_strings[5]:{
                'number_input' : 'Grains (input): '
            },
            self.function_strings[6]:{
                'number_input' : 'Grains (input): '
            },
            self.function_strings[7]:{
                'number_input' : 'Grains (input): '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{
                '' : 'Tons * 907.18'
            },
            self.function_strings[2]:{
                '' : 'Kilograms * 0.001102'
            },
            self.function_strings[3]:{
                '' : 'Tons * 0.90718'
            },
            self.function_strings[4]:{
                '' : 'Metric Tons * 1.1023'
            },
            self.function_strings[5]:{
                '' : 'Grains * 0.0365764447696'
            },
            self.function_strings[6]:{
                '' : 'Grains * 0.00228571'
            },
            self.function_strings[7]:{
                '' : 'Grains * 15.43236'
            },
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Formula Functions _____________________________________________________________________________

    def tons(self):
        title = self.function_strings[1]
        ton = "Enter Tons"
        argsOut = [title, ton]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 907.18
        return (result, self.pluralize(result, 'Kilogram'))

    def kilo(self):
        title = self.function_strings[2]
        kilo = "Enter Kilograms"
        argsOut = [title, kilo]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .001102
        return (result, self.pluralize(result, 'Ton'))

    def tons2(self):
        title = self.function_strings[3]
        ton = "Enter Tons"
        argsOut = [title, ton]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .90718
        return (result, self.pluralize(result, 'Metric Ton'))

    def tons3(self):
        title = self.function_strings[4]
        mt = "Enter Metric Tons"
        argsOut = [title, mt]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.1023
        return (result, self.pluralize(result, 'Ton'))

    def grains(self):
        title = self.function_strings[5]
        grain = "Enter Grains"
        argsOut = [title, grain]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0365764447696
        return (result, self.pluralize(result, 'Dram'))

    def grains2(self):
        title = self.function_strings[6]
        grain = "Enter Grains"
        argsOut = [title, grain]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .00228571
        return (result, self.pluralize(result, 'Ounce'))

    def grains3(self):
        title = self.function_strings[7]
        grain = "Enter Grains"
        argsOut = [title, grain]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 15.43236
        return (result, self.pluralize(result, 'Gram'))
#}}}_________________________________________________________________________________________


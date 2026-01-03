#!/usr/bin/env python3
#
# Energy_or_Work.py
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


class Energy_or_Work(FormulaBase):
    def __init__(self, name):
        super(Energy_or_Work, self).__init__(name)
        self.name = name
            
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'BTU to Foot-Pounds',
            2 : 'Mega Joules to KiloWatt Hours',
            3 : 'BTU to Gram-Calories',
            4 : 'BTU to Joules',
            5 : 'Joules to Watt Hours',
            6 : 'Calories to Joules',
            7 : 'Foot-Pounds to Joules',
            8 : 'Joules to BTU',
            9 : 'WattHours to Joules',
            10 : 'Joules to Calories',
            11 : 'Joules to Foot-Pounds',
            12 : 'KiloWatt Hours to Mega Joules',
        }

#}}}_________________________________________________________________________________________
        
#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_btu),
                (self.function_strings[2], self.megaJ),
                (self.function_strings[3], self.form_btu2),
                (self.function_strings[4], self.btu3),
                (self.function_strings[5], self.joules4),
                (self.function_strings[6], self.calories),
                (self.function_strings[7], self.foot),
                (self.function_strings[8], self.joules3),
                (self.function_strings[9], self.watt),
                (self.function_strings[10], self.joules2),
                (self.function_strings[11], self.joules),
                (self.function_strings[12], self.kiloWatt),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {

            self.function_strings[1] : {
                    'number_input' : 'BTU (input): '
            },
            self.function_strings[3] : {
                    'number_input' : 'BTU (input): '
            },
            self.function_strings[7] : {
                    'number_input' : 'Foot-Pounds (input): '
            },
            self.function_strings[11]:{
                    'number_input' : 'Joules (input): '
            },
            self.function_strings[4]:{
                    'number_input' : "BTU's (input): "
            },
            self.function_strings[8]:{
                    'number_input' : 'Joules (input): '
            },
            self.function_strings[9]:{
                    'number_input' : 'Watt Hours (input): '
            },
            self.function_strings[5]:{
                    'number_input' : 'Joules (input): '
            },
            self.function_strings[12]:{
                    'number_input' : 'KiloWatt Hours (input): '
            },
            self.function_strings[2]:{
                    'number_input' : 'Mega Joules (input): '
            },
            self.function_strings[6]:{
                'number_input' : 'Calories (input): '
            },
            self.function_strings[10]:{
                'number_input' : 'Joules (input): '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {

            self.function_strings[1]:{
                '' : 'BTU * 778.2'
            },
            self.function_strings[3]:{
                '' : 'BTU * 252.0'
            },
            self.function_strings[7]:{
                '' : 'Foot-Pounds * 1.3558'
            },
            self.function_strings[11]:{
                '' : 'Joules * 0.7376'
            },
            self.function_strings[6]:{
                '' : 'Calories * 4.187'
            },
            self.function_strings[10]:{
                '' : 'Joules * 0.2388'
            },
            self.function_strings[4]:{
                '' : 'BTU * 1055'
            },
            self.function_strings[8]:{
                '' : 'Joules * 0.000948'
            },
            self.function_strings[9]:{
                '' : 'Watt Hours * 3600'
            },
            self.function_strings[5]:{
                '' : 'Joules * 0.0002778'
            },
            self.function_strings[12]:{
                '' : 'KiloWatt Hours * 3.6'
            },
            self.function_strings[2]:{
                '' : 'Mega Joules * 0.2778'
            },
        }
#}}}_________________________________________________________________________________________
    
#{{{___ Functions _____________________________________________________________________________

    def form_btu(self):
        argsOut = [self.function_strings[1], 'Enter BTUs']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 778.2
        return (result, self.pluralize(result, 'Foot-Pound'))
        
    def form_btu2(self):
        argsOut = [self.function_strings[3], 'Enter BTUs']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 252.0
        return (result, self.pluralize(result, 'Gram-Calorie'))

    def megaJ (self):
        title = self.function_strings[2]
        argsOut = [title, 'Enter Mega Joules']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2778
        return (result, self.pluralize(result, 'Kilo Watt Hour'))

    def kiloWatt (self):
        title = self.function_strings[12]
        argsOut = [title, 'Enter KiloWatts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.6
        return (result, self.pluralize(result, 'Mega Joule'))

    def joules4 (self):
        title = self.function_strings[5]
        argsOut = [title, 'Enter Joules']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0002778
        return (result, self.pluralize(result, 'Watt Hour'))

    def watt (self):
        title = self.function_strings[9]
        argsOut = [title, 'Enter Watts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3600
        return (result, self.pluralize(result, 'Joule'))

    def joules3 (self):
        title = self.function_strings[8]
        argsOut = [title, 'Enter Joules']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .000948
        return (result, self.pluralize(result, "BTU'"))

    def btu3 (self):
        title = self.function_strings[4]
        argsOut = [title, 'Enter BTU']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1055
        return (result, self.pluralize(result, "Joule"))

    def calories (self):
        title = self.function_strings[6]
        argsOut = [title, 'Enter Calories']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4.187
        return (result, self.pluralize(result, 'Joule'))

    def joules2 (self):
        title = self.function_strings[10]
        argsOut = [title, 'Enter Joules']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2388
        return (result, self.pluralize(result, 'Calorie'))

    def foot (self):
        title = self.function_strings[7]
        argsOut = [title, 'Enter Foot/Pounds']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.3558
        return (result, self.pluralize(result, 'Joule'))

    def joules (self):
        title = self.function_strings[11]
        argsOut = [title, 'Enter Joules']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .7376
        return (result, self.pluralize(result, 'Foot/Pound'))

#}}}_________________________________________________________________________________________

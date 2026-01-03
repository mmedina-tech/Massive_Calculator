#!/usr/bin/env python3
#
# Imperial_to_Imperial.py
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


class Imperial_to_Imperial(FormulaBase):
    def __init__(self, name):
        super(Imperial_to_Imperial, self).__init__(name)
        self.name = name
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Feet to Miles',
            2 : 'Miles to Feet',
            3 : 'Ounces to Pounds',
            4 : 'Pounds to Ounces',
            5 : 'Tons to Pounds',
            6 : 'Yards to Miles',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_feet),
                (self.function_strings[2], self.form_miles),
                (self.function_strings[3], self.form_ounces),
                (self.function_strings[4], self.form_pounds),
                (self.function_strings[5], self.form_tons),
                (self.function_strings[6], self.form_yards)
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[1] : {
                'number_input' : 'Feet: '
            },
            self.function_strings[2] : {
                'number_input' : 'Miles: '
            },
            self.function_strings[3] : {
                'number_inputs' : 'Ounces: '
            },
            self.function_strings[4] : {
                'number_input' : 'Pounds: '
            },
            self.function_strings[5] : {
                'number_input' : 'Tons: '
            },
            self.function_strings[6] : {
                'number_input' : 'Yards: '
            },
            'Pounds to Tons' : {
                'number_input' : 'Pounds: '
            },
            'Feet to Inches' : {
                'number_input' : 'Feet: '
            },
            'Feet to Yards' : {
                'number_input' : 'Feet: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{
                '' : 'Feet * 0.0001894'
            },
            self.function_strings[2]:{
                '' : 'Miles * 5280'
            },
            self.function_strings[3]:{
                '' : 'Ounces * 0.0625'
            },
            self.function_strings[4]:{
                '' : 'Pounds * 16'
            },
            self.function_strings[5]:{
                '' : 'Tons * 2000'
            },
            self.function_strings[6]:{
                '' : 'Yards * 0.0005682'
            },
        }
#}}}_________________________________________________________________________________________
    
#{{{___ Functions _____________________________________________________________________________

    def form_feet(self):
        argsOut = [self.function_strings[1], 'Enter Feet']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0001894
        return (result, self.pluralize(result, 'Mile'))
            
    def form_miles(self):
        argsOut = [self.function_strings[2], 'Enter Miles']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 5280
        return (result, self.pluralize(result, 'Foot'))
            
    def form_ounces(self):
        argsOut = [self.function_strings[3], 'Enter Ounces']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0625
        return (result, self.pluralize(result, 'Pound'))
            
    def form_pounds(self):
        argsOut = [self.function_strings[4], 'Enter Pounds']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 16
        return (result, self.pluralize(result, 'Ounce'))
            
    def form_tons(self):
        argsOut = [self.function_strings[5], 'Enter Tons']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2000
        return (result, self.pluralize(result, 'Pound'))
            
    def form_yards(self):
        argsOut = [self.function_strings[6], 'Enter Yards']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0005682
        return (result, self.pluralize(result, 'Mile'))

#}}}_________________________________________________________________________________________


#!/usr/bin/env python3
#
# PlaneAngle.py
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

class PlaneAngle(FormulaBase):
    def __init__(self, name):
        super(PlaneAngle, self).__init__(name)
        self.name = name
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Degrees to Radians',
            2 : 'Minutes to Degrees',
            3 : 'Quadrants to Degrees',
            4 : 'Quadrants to Radians',
            5 : 'Radians to Degrees',
            6 : 'Minutes to Radians',
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_degrees),
                (self.function_strings[2], self.form_minutes),
                (self.function_strings[3], self.form_quadrants),
                (self.function_strings[4], self.form_quadrants2),
                (self.function_strings[5], self.form_radians),
                (self.function_strings[6], self.form_minutes2),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1] : {
                    'number_input' : 'Degrees: '
            },
            self.function_strings[2] : {
                    'number_input' : 'Minutes: '
            },
            self.function_strings[6] : {
                    'number_input' : 'Minutes: '
            },
            self.function_strings[3] : {
                    'number_input' : 'Quadrants: '
            },
            self.function_strings[4] : {
                    'number_input' : 'Quadrants: '
            },
            self.function_strings[5] : {
                    'number_input' : 'Radians: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{
                '' : 'Degrees * 0.0175'
            },
            self.function_strings[2]:{
                '' : 'Minutes * 0.1667'
            },
            self.function_strings[6]:{
                '' : 'Minutes * (2.9 * 10<sup>-4</sup>)'
            },
            self.function_strings[3]:{
                '' : 'Quadrants * 90'
            },
            self.function_strings[4]:{
                '' : 'Quadrants * 1.5708'
            },
            self.function_strings[5]:{
                '' : 'Radians * 57.3'
            },
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Functions _____________________________________________________________________________

    def form_degrees(self):
        argsOut = [self.function_strings[1], 'Enter Degrees']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0175
        return (result, self.pluralize(result, 'Radian'))
            
    def form_minutes(self):
        argsOut = [self.function_strings[2], 'Enter Minutes']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .1667
        return (result, self.pluralize(result, 'Degree'))
            
    def form_minutes2(self):
        argsOut = [self.function_strings[6], 'Enter Minutes']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * (2.9 * 10 ** (-4))
        return (result, self.pluralize(result, 'Radian'))
            
    def form_quadrants(self):
        argsOut = [self.function_strings[3], 'Enter Quadrant']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 90.0
        return (result, self.pluralize(result, 'Degree'))
            
    def form_quadrants2(self):
        argsOut = [self.function_strings[4], 'Enter Quadrant']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.5708
        return (result, self.pluralize(result, 'Radian'))
            
    def form_radians(self):
        argsOut = [self.function_strings[5], 'Enter Radians']
        argsIn =self.prompt(argsOut)
        result = argsIn[0] * 57.3
        return (result, self.pluralize(result, 'Degree'))
#}}}_________________________________________________________________________________________


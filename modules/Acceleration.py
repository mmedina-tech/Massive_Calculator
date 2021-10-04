#!/usr/bin/python
#SYNOPSIS: Acceleration Formula Set

#
# Acceleration.py
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
# This Module is for Acceleration Formulas 


from FormulaBase import * 

class Acceleration(FormulaBase):
    def __init__(self, name): 
        super(Acceleration, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________

        self.function_strings = {
            1 : 'Feet/Sec Squared to Meters/Sec Squared',
            2 : 'Inches/Sec Squared to Meters/Sec Squared',
            3 : 'Meters/Sec Squared to Feet/Sec Squared',
            4 : 'Meters/Sec Squared to Inches/Sec Squared',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = {
            self.function_strings[1] : self.feet,
            self.function_strings[2] : self.inch,
            self.function_strings[3] : self.meters,
            self.function_strings[4] : self.meters2,
        }
#}}}_________________________________________________________________________________________

#{{{ Inputs
        self.functionInputs = {
            self.function_strings[1]:{
                    'number_input' : 'Feet/Sec<sup>2</sup> (input): '
            },
            self.function_strings[3]:{
                    'number_input' : 'Meters/Sec<sup>2</sup> (input): '
            },
            self.function_strings[2]:{
                    'number_input' : 'Inches/Sec<sup>2</sup> (input): '
            },
            self.function_strings[4]:{
                    'number_input' : 'Meters/Sec<sup>2</sup> (input): '
            },
        }
#}}}

#{{{___ Show Formula _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{
                "Formula:<br> " : 'Feet/Sec<sup>2</sup> * 0.3048'
            },
            self.function_strings[3]:{
                'Formula:<br> ' : 'Meters/Sec<sup>2</sup> * 3.281'
            },
            self.function_strings[2]:{
                'Formula:<br>' : 'Inches/Sec<sup>2</sup> * 0.0254'
            },
            self.function_strings[4]:{
                'Formula:<br>' : 'Meters/Sec<sup>2</sup> * 39.37'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Functions _____________________________________________________________________________

    def feet (self):
        # Feet/Sec Squared to Meters/Sec Squared 
        title = self.function_strings[1]
        feet = 'Enter Feet/Sec Squared'
        argsOut = [title, feet]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .3048
        return (result, self.pluralize(result, 'Meters/Sec^2'))

    def meters (self):
        # Meters/Sec Squared to Feet/Sec Squared 
        title = self.function_strings[3]
        meter = 'Enter Meters/Sec Squared'
        argsOut = [title, meter]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.281
        return (result, self.pluralize(result, 'Feet/Sec^2'))

    def inch (self):
        # Inches/Sec Squared to Meters/Sec Squared 
        title = self.function_strings[2]
        inch = 'Enter Inches/Sec Squared'
        argsOut = [title, inch]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0254
        return (result, self.pluralize(result, 'Meters/Sec^2'))

    def meters2 (self):
        # Meters/Sec Squared to Inches/Sec Squared 
        title = self.function_strings[4]
        meter = 'Enter Meters/Sec Squared'
        argsOut = [title, meter]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 39.37
        return (result, self.pluralize(result, 'Inches/Sec^2'))
#}}}_________________________________________________________________________________________


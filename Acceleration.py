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


from FormulaBase import * 
from collections import OrderedDict

class Acceleration(FormulaBase):
    def __init__(self, name): 
        super(Acceleration, self).__init__(name)
        self.name = name

        self.function_list = OrderedDict(
            [
                ('Feet/Sec Squared to Meters/Sec Squared', self.feet),
                ('Inches/Sec Squared to Meters/Sec Squared', self.inch),
                ('Meters/Sec Squared to Feet/Sec Squared', self.meters),
                ('Meters/Sec Squared to Inches/Sec Squared', self.meters2),
            ]
        )
#{{{
        self.functionInputs = {
            'Feet/Sec Squared to Meters/Sec Squared':{
                    'number_input' : 'Feet/Sec<sup>2</sup> (input): '
            },
            'Meters/Sec Squared to Feet/Sec Squared':{
                    'number_input' : 'Meters/Sec<sup>2</sup> (input): '
            },
            'Inches/Sec Squared to Meters/Sec Squared':{
                    'number_input' : 'Inches/Sec<sup>2</sup> (input): '
            },
            'Meters/Sec Squared to Inches/Sec Squared':{
                    'number_input' : 'Meters/Sec<sup>2</sup> (input): '
            },
        }
#}}}

        self.formula_list = {
            'Feet/Sec Squared to Meters/Sec Squared':{
                "Formula:<br> " : 'Feet/Sec<sup>2</sup> * 0.3048'
            },
            'Meters/Sec Squared to Feet/Sec Squared':{
                'Formula:<br> ' : 'Meters/Sec<sup>2</sup> * 3.281'
            },
            'Inches/Sec Squared to Meters/Sec Squared':{
                'Formula:<br>' : 'Inches/Sec<sup>2</sup> * 0.0254'
            },
            'Meters/Sec Squared to Inches/Sec Squared':{
                'Formula:<br>' : 'Meters/Sec<sup>2</sup> * 39.37'
            },
        }

    def feet (self):
        title = 'Feet/Sec Squared to Meters/Sec Squared'
        feet = 'Enter Feet/Sec Squared'
        argsOut = [title, feet]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .3048
        return (result, self.pluralize(result, 'Meters/Sec^2'))

    def meters (self):
        title = 'Meters/Sec Squared to Feet/Sec Squared'
        meter = 'Enter Meters/Sec Squared'
        argsOut = [title, meter]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.281
        return (result, self.pluralize(result, 'Feet/Sec^2'))

    def inch (self):
        title = 'Inches/Sec Squared to Meters/Sec Squared'
        inch = 'Enter Inches/Sec Squared'
        argsOut = [title, inch]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0254
        return (result, self.pluralize(result, 'Meters/Sec^2'))

    def meters2 (self):
        title = 'Meters/Sec Squared to Inches/Sec Squared'
        meter = 'Enter Meters/Sec Squared'
        argsOut = [title, meter]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 39.37
        return (result, self.pluralize(result, 'Inches/Sec^2'))


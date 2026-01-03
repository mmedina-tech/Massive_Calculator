#!/usr/bin/env python3
#SYNOPSIS: Astronomic Unit Set
#
# Astronomic_units.py
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


class Astronomic_units(FormulaBase):
    def __init__(self, name):
        super(Astronomic_units, self).__init__(name)
        self.name = name
        
#{{{ Function Strings
        self.function_strings = {
            1 : 'Celsius to Kelvin',
            2 : 'Fahrenheit to Kelvin',
            3 : 'Light Years to Astronomic Units',
            4 : 'Astronomic Units to Light Years',
            5 : 'Light Years to Parsecs',
            6 : 'Parsecs to Light Years',
            7 : 'Celsius to Rankine',
            8 : 'Rankine to Celsius',
            9 : 'Rankine to Kelvin',
            10 : 'Kelvin to Rankine',
        }
#}}}
        
#{{{ Function List
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_celsius),
                (self.function_strings[2], self.form_fahrenheit),
                (self.function_strings[3], self.light),
                (self.function_strings[4], self.astro),
                (self.function_strings[5], self.light2),
                (self.function_strings[6], self.parsec),
                (self.function_strings[7], self.rankin),
                (self.function_strings[8], self.celsius),
                (self.function_strings[9], self.kelvin),
                (self.function_strings[10], self.rankin2),
            ]
        )
#}}}
        
#{{{ Formula Inputs
        self.functionInputs = {
            self.function_strings[2] : {
                    'number_input' : 'Fahrenheit (input): '
            },
            self.function_strings[1] : {
                    'number_input' : 'Celsius (input): '
            },
            self.function_strings[3]:{
                    'number_input' : 'Light Years (input): '
            },
            'Astronomic Units to Parsecs':{
                    'number_input' : 'Astronomic Units (input): '
            },
            self.function_strings[4]:{
                    'number_input' : 'Astronomic Units (input): '
            },
            self.function_strings[5]:{
                    'number_input' : 'Light Years (input): '
            },
            self.function_strings[6]: {
                    'number_input' : 'Parsecs (input): '
            },
            self.function_strings[7]:{
                    'number_input' : 'Celsius (input): '
            },
            self.function_strings[8]:{
                    'number_input' : 'Rankine (input): '
            },
            self.function_strings[9]:{
                    'number_input' : 'Rankine (input): '
            },
            self.function_strings[10]:{
                    'number_input' : 'Kelvin (input): '
            },
        }
#}}}

#{{{ Show Formula
        self.formula_list = {
            self.function_strings[1]:{
                'Formula:<br>' : 'Celsius + 270'
            },
            self.function_strings[2]:{
                'Formula:<br>' : '((Fahrenheit - 32) * 5/9) + 270'
            },
            self.function_strings[3]:{
                'Formula:<br>' : 'Light Years * 63241.88'
            },
            self.function_strings[4]:{
                'Formula:<br>' : 'Astronomic Units * 0.000015813'
            },
            self.function_strings[5]:{
                'Formula:<br>' : 'Light Years * 3.261587474'
            },
            self.function_strings[6]:{
                'Formula:<br>' : 'Parsecs * 0.306599166'
            },
            self.function_strings[7]:{
                'Formula:<br>' : 'Celsius * 493.47'
            },
            self.function_strings[8]:{
                'Formula:<br>' : 'Rankine * -272.594444444'
            },
            self.function_strings[9]:{
                'Formula:<br>' : 'Rankine * 0.555555556'
            },
            self.function_strings[10]:{
                'Formula:<br>' : 'Kelvin * 1.8'
            },
        }
#}}}

#{{{___ Formula Functions _____________________________________________________________________________

    def rankin2 (self):
        title = 'Kelvin to Rankine'
        kel = 'Enter Kelvin'
        argsOut = [title, kel]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.8
        return (result, self.pluralize(result, 'Rankine')) 

    def kelvin (self):
        title = "Rankine to Kelvin"
        ran = "Enter Rankine"
        argsOut = [title, ran]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .555555556
        return (result, self.pluralize(result, 'Kelvin')) 

    def celsius (self):
        title = 'Rankine to Celsius'
        ran = "Enter Rankine"
        argsOut = [title, ran]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * -272.594444444
        return (result, self.pluralize(result, 'Celsius')) 

    def rankin (self):
        title = 'Celsius to Rankine'
        cel = "Enter Celsius"
        argsOut = [title, cel]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 493.47
        return (result, self.pluralize(result, 'Rankine')) 

    def light2 (self):
        title = 'Light Years to Parsecs'
        light = "Enter Light Years"
        argsOut = [title, light]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.261587474
        return (result, self.pluralize(result, 'Parsec')) 

    def parsec (self):
        title = 'Parsecs to Light Years'
        par = "Enter Parsecs"
        argsOut = [title, par]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .306599166
        return (result, self.pluralize(result, 'Light Year')) 

    def astro (self):
        title = 'Astronomical Units to Light Years'
        au = "Enter Astronomical Units"
        argsOut = [title, au]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .000015813
        return (result, self.pluralize(result, 'Light Year')) 

    def light (self):
        title = 'Light Years to Astronomical Units'
        ly = "Enter Light Years"
        argsOut = [title, ly]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 63241.08
        return (result, self.pluralize(result, 'Astronomical Unit')) 

    def form_celsius(self):
        title = 'Celsius to Kelvin'
        cel = "Enter Celsius"
        argsOut = [title, cel]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] + 270)
        return (result, self.pluralize(result, 'Kelvin'))

    def form_fahrenheit(self):
        title = 'Fahrenheit to Kelvin'
        fah = "Enter Fahrenheit"
        argsOut = [title, fah]
        argsIn = self.prompt(argsOut)
        result = (((argsIn[0] - 32) * 5/9) + 270)
        return (result, self.pluralize(result, 'Kelvin'))
#}}}_________________________________________________________________________________________


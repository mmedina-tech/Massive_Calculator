#!/usr/bin/python 
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


from FormulaBase import *


class Astronomic_units(FormulaBase):
    def __init__(self):
        super(Astronomic_units, self).__init__()
        
        self.function_list = OrderedDict(
            [
                ('Celsius to Kelvin', self.form_celsius),
                ('Fahrenheit to Kelvin', self.form_fahrenheit),
                ('Light Years to Astronomical Units', self.light),
                ('Astronomical Units to Light Years', self.astro),
                ('Light Years to Parsecs', self.light2),
                ('Parsecs to Light Years', self.parsec),
                ('Celsius to Rankine', self.rankin),
                ('Rankine to Celsius', self.celsius),
                ('Rankine to Kelvin', self.kelvin),
                ('Kelvin to Rankine', self.rankin2),
            ]
        )
#{{{
        self.functionInputs = {
            'Fahrenheit to Kelvin' : {
                    'number_input' : 'Fahrenheit (input): '
            },
            'Celsius to Kelvin' : {
                    'number_input' : 'Celsius (input): '
            },
            'Light Years to Astronomical Units':{
                    'number_input' : 'Light Years (input): '
            },
            'Astronomical Units to Parsecs':{
                    'number_input' : 'Astronomical Units (input): '
            },
            'Astronomical Units to Light Years':{
                    'number_input' : 'Astronomical Units (input): '
            },
            'Light Years to Parsecs':{
                    'number_input' : 'Light Years (input): '
            },
            'Parsecs to Light Years': {
                    'number_input' : 'Parsecs (input): '
            },
            'Celsius to Rankine':{
                    'number_input' : 'Celsius (input): '
            },
            'Rankine to Celsius':{
                    'number_input' : 'Rankine (input): '
            },
            'Rankine to Kelvin':{
                    'number_input' : 'Rankine (input): '
            },
            'Kelvin to Rankine':{
                    'number_input' : 'Kelvin (input): '
            },
        }
    #}}}

        self.formula_list = {
            'Celsius to Kelvin':{
                'Formula:<br>' : 'Celsius + 270'
            },
            'Fahrenheit to Kelvin':{
                'Formula:<br>' : '((Fahrenheit - 32) * 5/9) + 270'
            },
            'Light Years to Astronomical Units':{
                'Formula:<br>' : 'Light Years * 63241.88'
            },
            'Astronomic Units to Light Years':{
                'Formula:<br>' : 'Astronomic Units * 0.000015813'
            },
            'Light Years to Parsecs':{
                'Formula:<br>' : 'Light Years * 3.261587474'
            },
            'Parsecs to Light Years':{
                'Formula:<br>' : 'Parsecs * 0.306599166'
            },
            'Celsius to Rankine':{
                'Formula:<br>' : 'Celsius * 493.47'
            },
            'Rankine to Celsius':{
                'Formula:<br>' : 'Rankine * -272.594444444'
            },
            'Rankine to Kelvin':{
                'Formula:<br>' : 'Rankine * 0.555555556'
            },
            'Kelvin to Rankine':{
                'Formula:<br>' : 'Kelvin * 1.8'
            },
        }
    def rankin2 (self, num):
            result = float(num) * 1.8
            return (str(self.prec2(result))+'&#65042', self.pluralize(result, 'Rankine')) 

    def kelvin (self, num):
            result = float(num) * .555555556
            return (self.prec2(result), self.pluralize(result, 'Kelvin')) 

    def celsius (self, num):
            result = float(num) * -272.594444444
            return (str(self.prec2(result))+'&#65042', self.pluralize(result, 'Celsius')) 

    def rankin (self, num):
            result = float(num) * 493.47
            return (str(self.prec2(result))+'&#65042', self.pluralize(result, 'Rankine')) 

    def light2 (self, num):
            result = float(num) * 3.261587474
            return (self.prec2(result), self.pluralize(result, 'Parsec')) 

    def parsec (self, num):
            result = float(num) * .306599166
            return (self.prec2(result), self.pluralize(result, 'Light Year')) 

    def astro (self, num):
            result = float(num) * .000015813
            return (self.prec4(result), self.pluralize(result, 'Light Year')) 

    def light (self, num):
            result = float(num) * 63241.08
            return (self.prec2(result), self.pluralize(result, 'Astronomical Unit')) 

    def form_celsius(self, num):
            result = (float(num) + 270)
            return (self.prec2(result), self.pluralize(result, 'Kelvin'))

    def form_fahrenheit(self, num):
            result = (((float(num) - 32) * 5/9) + 270)
            return (self.prec2(result), self.pluralize(result, 'Kelvin'))

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
    def __init__(self, name):
        super(Astronomic_units, self).__init__(name)
        self.name = name
        
        self.function_list = {
            'Celsius to Kelvin': self.form_celsius,
            'Fahrenheit to Kelvin': self.form_fahrenheit,
            'Light Years to Astronomical Units': self.light,
            'Astronomical Units to Light Years': self.astro,
            'Light Years to Parsecs': self.light2,
            'Parsecs to Light Years': self.parsec,
            'Celsius to Rankine': self.rankin,
            'Rankine to Celsius': self.celsius,
            'Rankine to Kelvin': self.kelvin,
            'Kelvin to Rankine': self.rankin2,
        }
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

#{{{___ Formula List _____________________________________________________________________________
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
            'Astronomical Units to Light Years':{
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
#}}}_________________________________________________________________________________________

    def rankin2 (self):
        title = 'Kelvin to Rankine'
        kel = 'Enter Kelvin'
        argsOut = [title, kel]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.8
        return (str(self.prec2(result)), self.pluralize(result, 'Rankine')) 

    def kelvin (self):
        title = "Rankine to Kelvin"
        ran = "Enter Rankine"
        argsOut = [title, ran]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .555555556
        return (self.prec2(result), self.pluralize(result, 'Kelvin')) 

    def celsius (self):
        title = 'Rankine to Celsius'
        ran = "Enter Rankine"
        argsOut = [title, ran]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * -272.594444444
        return (str(self.prec2(result)), self.pluralize(result, 'Celsius')) 

    def rankin (self):
        title = 'Celsius to Rankine'
        cel = "Enter Celsius"
        argsOut = [title, cel]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 493.47
        return (str(self.prec2(result)), self.pluralize(result, 'Rankine')) 

    def light2 (self):
        title = 'Light Years to Parsecs'
        light = "Enter Light Years"
        argsOut = [title, light]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.261587474
        return (self.prec2(result), self.pluralize(result, 'Parsec')) 

    def parsec (self):
        title = 'Parsecs to Light Years'
        par = "Enter Parsecs"
        argsOut = [title, par]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .306599166
        return (self.prec2(result), self.pluralize(result, 'Light Year')) 

    def astro (self):
        title = 'Astronomical Units to Light Years'
        au = "Enter Astronomical Units"
        argsOut = [title, au]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .000015813
        return (self.prec4(result), self.pluralize(result, 'Light Year')) 

    def light (self):
        title = 'Light Years to Astronomical Units'
        ly = "Enter Light Years"
        argsOut = [title, ly]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 63241.08
        return (self.prec2(result), self.pluralize(result, 'Astronomical Unit')) 

    def form_celsius(self):
        title = 'Celsius to Kelvin'
        cel = "Enter Celsius"
        argsOut = [title, cel]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] + 270)
        return (self.prec2(result), self.pluralize(result, 'Kelvin'))

    def form_fahrenheit(self):
        title = 'Fahrenheit to Kelvin'
        fah = "Enter Fahrenheit"
        argsOut = [title, fah]
        argsIn = self.prompt(argsOut)
        result = (((argsIn[0] - 32) * 5/9) + 270)
        return (self.prec2(result), self.pluralize(result, 'Kelvin'))

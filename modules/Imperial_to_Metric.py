#!/usr/bin/python
#
# Imperial_to_Metric.py
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


class Imperial_to_Metric(FormulaBase):
    def __init__(self, name):
        super(Imperial_to_Metric, self).__init__(name)
        self.name = name
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Fahrenheit to Celsius',
            2 : 'Cubic Yards to Cubic Meters',
            3 : 'Feet to Meters',
            4 : 'Gallons to Liters',
            5 : 'Inches to Millimeters',
            6 : 'Inches to Centimeters',
            7 : 'Miles to Kilometers',
            8 : 'Ounces to Grams',
            9 : 'Pints to Liters',
            10 : 'Quarts to Liters',
            11 : 'Pounds to Kilograms',
            12 : 'Square Feet to Square Meters',
            13 : 'Square Miles to Square Kilometers',
            14 : 'Square Yards to Square Meters',
            15 : 'Yards to Meters',
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_fahrenheit),
                (self.function_strings[2], self.form_cuyards),
                (self.function_strings[3], self.form_feet),
                (self.function_strings[4], self.form_gallons),
                (self.function_strings[5], self.form_inches),
                (self.function_strings[6], self.form_inches2),
                (self.function_strings[7], self.form_miles),
                (self.function_strings[8], self.form_ounces),
                (self.function_strings[9], self.form_pints),
                (self.function_strings[10], self.form_quarts),
                (self.function_strings[11], self.form_pounds),
                (self.function_strings[12], self.form_sqfeet),
                (self.function_strings[13], self.form_sqmiles),
                (self.function_strings[14], self.form_sqyards),
                (self.function_strings[15], self.form_yards)
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1] : {
                    'number_input' : 'Fahrenheit: '
            },
            self.function_strings[2] : {
                    'number_input' : 'Cubic Yards: '
            },
            self.function_strings[3] : {
                    'number_input' : 'Feet: '
            },
            self.function_strings[4] : {
                    'number_input' : 'Gallons: '
            },
            self.function_strings[5] : {
                    'number_input' : 'Inches: '
            },
            self.function_strings[6] : {
                    'number_input' : 'Inches: '
            },
            self.function_strings[7] : {
                    'number_input' : 'Miles: '
            },
            self.function_strings[8] : {
                    'number_input' : 'Ounces: '
            },
            self.function_strings[9] : {
                    'number_input' : 'Pints: '
            },
            self.function_strings[10] : {
                    'number_input' : 'Quarts: '
            },
            self.function_strings[11] : {
                    'number_input' : 'Pounds: '
            },
            self.function_strings[12] : {
                    'number_input' : 'Square Feet:'
            },
            self.function_strings[13] : {
                    'number_input' : 'Square Miles: '
            },
            self.function_strings[14] : {
                    'number_input' : 'Square Yards: '
            },
            self.function_strings[15] : {
                    'number_input' : 'Yards: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{
                '' : '(Fahrenheit - 32) * 5/9'
            },
            self.function_strings[2]:{
                '' : 'Cubic Yards * 0.7646'
            },
            self.function_strings[3]:{
                '' : 'Feet * 0.3048'
            },
            self.function_strings[4]:{
                '' : 'Gallons * 3.7853'
            },
            self.function_strings[6]:{
                '' : 'Inches * 2.54'
            },
            self.function_strings[7]:{
                '' : 'Miles * 1.6093'
            },
            self.function_strings[5]:{
                '' : 'Inches * 25.4'
            },
            self.function_strings[8]:{
                '' : 'Ounces * 28.3495'
            },
            self.function_strings[11]:{
                '' : 'Pounds * 0.4536'
            },
            self.function_strings[9]:{
                '' : 'Pints * 1.4732'
            },
            self.function_strings[10]:{
                '' : 'Quarts * 0.9463'
            },
            self.function_strings[12]:{
                '' : 'Square Feet * 0.929'
            },
            self.function_strings[13]:{
                '' : 'Square Miles * 2.59'
            },
            self.function_strings[14]:{
                '' : 'Square Yards * 0.8361'
            },
            self.function_strings[15]:{
                '' : 'Yards * 0.9144'
            },
        }
#}}}_________________________________________________________________________________________
            
#{{{___ Functions _____________________________________________________________________________

    def form_fahrenheit(self):
        argsOut = [self.function_strings[1], 'Enter Fahrenheit']
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] - 32) * 5/9
        return (result, self.pluralize(result, 'Celsius'))
            
    def form_cuyards(self):
        argsOut = [self.function_strings[2], 'Enter Cubic Yards']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .7646
        return (result, self.pluralize(result, 'Cubic Meter'))
            
    def form_feet(self):
        argsOut = [self.function_strings[3], 'Enter Feet']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .3048
        return (result, self.pluralize(result, 'Meter'))
            
    def form_gallons(self):
        argsOut = [self.function_strings[4], 'Enter Gallons']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.7853
        return (result, self.pluralize(result, 'Liter'))
            
    def form_inches2(self):
        argsOut = [self.function_strings[5], 'Enter Inches']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.54
        return (result, self.pluralize(result, 'Centimter'))
            
    def form_inches(self):
        argsOut = [self.function_strings[6], 'Enter Inches']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 25.4
        return (result, self.pluralize(result, 'Millimeter'))
            
    def form_miles(self):
        argsOut = [self.function_strings[7], 'Enter Miles']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.6093
        return (result, self.pluralize(result, 'Kilometer'))
            
    def form_ounces(self):
        argsOut = [self.function_strings[8], 'Enter Ounces']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 28.3495
        return (result, self.pluralize(result, 'Gram'))
            
    def form_pounds(self):
        argsOut = [self.function_strings[9], 'Enter Pounds']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .4536
        return (result, self.pluralize(result, 'Kilogram'))
            
    def form_pints(self):
        argsOut = [self.function_strings[10], 'Enter Pints']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.4732
        return (result, self.pluralize(result, 'Liter'))
            
    def form_quarts(self):
        argsOut = [self.function_strings[11], 'Enter Quarts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .9463
        return (result, self.pluralize(result, 'Liter'))
            
    def form_sqfeet(self):
        argsOut = [self.function_strings[12], 'Enter Square Feet']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .929
        return (result, self.pluralize(result, 'Square Meter'))
            
    def form_sqmiles(self):
        argsOut = [self.function_strings[13], 'Enter Square Miles']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.59
        return (result, self.pluralize(result, 'Square Kilometer'))
            
    def form_sqyards(self):
        argsOut = [self.function_strings[14], 'Enter Square Yards']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .8361
        return (result, self.pluralize(result, 'Square Meter'))
            
    def form_yards(self):
        argsOut = [self.function_strings[15], 'Enter Yards']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .9144
        return (result, self.pluralize(result, 'Meter'))
#}}}_________________________________________________________________________________________


#!/usr/bin/env python3
# SYNOPSIS: Power Module for Massive Calculator
# 
# Power.py
#
# Author: Marcus Medina,,,
# Date: Thu 15 Apr 2021 08:18:08 AM PDT
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or 
# (at your option) any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABLILITY of FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You Should have recieved a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
#
#

from .FormulaBase import *

class Power(FormulaBase):
    def __init__(self, name):
        super(Power, self).__init__(name)
        self.name = name 
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'BTU per Hour to Watts',
            2 : 'Horsepower to Foot-Pounds per Minute',
            3 : 'Horsepower to Foot-Pounds per Second',
            4 : 'Horsepower to Watts',
            5 : 'KiloWatts to Horsepower',
            6 : 'Foot-Pounds per Minute to Watts',
            7 : 'Watts to Foot-Pounds per Minute',
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.form_btuhour),
                (self.function_strings[2], self.form_hpftlbsm),
                (self.function_strings[3], self.form_hpftlbss),
                (self.function_strings[4], self.form_hpw),
                (self.function_strings[5], self.form_kwhp),
                (self.function_strings[6], self.ftlbs),
                (self.function_strings[7], self.watts),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1] : {
                    'number_input' : 'BTU per Hour: '
            },
            self.function_strings[2] : {
                    'number_input' : 'Horsepower: '
            },
            self.function_strings[3] : {
                    'number_input' : 'Horsepower: '
            },
            self.function_strings[4] : {
                    'number_input' : 'Horsepower: '
            },
            self.function_strings[5] : {
                    'number_input' : 'KiloWatts: '
            },
            self.function_strings[6]:{
                    'number_input' : 'Foot-Pounds per Minute: '
            },
            self.function_strings[7]:{
                    'number_input' : 'Watts: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        
        self.formula_list = {
            self.function_strings[6]:{
                '' : 'Foot-Pounds * 0.0226'
            },
            self.function_strings[7]:{
                '' : 'Watts * 44.25'
            },
            self.function_strings[1]:{
                '' : 'BTU per Hour * 0.293'
            },
            self.function_strings[2]:{
                '' : 'Horsepower * 33000'
            },
            self.function_strings[3]:{
                '' : 'Horsepower * 550.0'
            },
            self.function_strings[4]:{
                '' : 'Horsepower * 746'
            },
            self.function_strings[5]:{
                '' : 'KiloWatts * 1.341'
            },
        }
#}}}_________________________________________________________________________________________
        
    def form_btuhour(self):
        argsOut = [self.function_strings[1], 'Enter BTUs']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .293
        return (result, self.pluralize(result, 'Watt'))
            
    def form_hpftlbsm(self):
        argsOut = [self.function_strings[2], 'Enter Horse Power']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 33000
        return (result, self.pluralize(result, 'Foot/Pounds per Minute'))
            
    def form_hpftlbss(self):
        argsOut = [self.function_strings[3], 'Enter Horse Power']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 550.0
        return (result, self.pluralize(result, 'Foot/Pounds per Second'))
            
    def form_hpw(self):
        argsOut = [self.function_strings[4], 'Enter Horse Power']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 746.0
        return (result, self.pluralize(result, 'Watt'))
            
    def form_kwhp(self):
        argsOut = [self.function_strings[5], 'Enter Kilo Watts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.341
        return (result, self.pluralize(result, 'Horse Power'))
    
    def ftlbs (self):
        argsOut = [self.function_strings[6], 'Enter Foot/Pounds ']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0226
        return (result, self.pluralize(result, 'Watt'))

    def watts (self):
        argsOut = [self.function_strings[7], 'Enter Watts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 44.25
        return (result, self.pluralize(result, 'Foot-Pounds per Minute'))

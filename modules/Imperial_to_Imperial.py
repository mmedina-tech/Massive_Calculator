#!/usr/bin/python
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

from FormulaBase import *
from collections import OrderedDict


class Imperial_to_Imperial(FormulaBase):
    def __init__(self, name):
        super(Imperial_to_Imperial, self).__init__(name)
        self.name = name
        
        self.function_list = {
            'Feet to Miles': self.form_feet,
            'Miles to Feet': self.form_miles,
            'Ounces to Pounds': self.form_ounces,
            'Pounds to Ounces': self.form_pounds,
            'Tons to Pounds': self.form_tons,
            'Yards to Miles': self.form_yards
        }
#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Feet to Miles':{
                '' : 'Feet * 0.0001894'
            },
            'Miles to Feet':{
                '' : 'Miles * 5280'
            },
            'Ounces to Pounds':{
                '' : 'Ounces * 0.0625'
            },
            'Pounds to Ounces':{
                '' : 'Pounds * 16'
            },
            'Tons to Pounds':{
                '' : 'Tons * 2000'
            },
            'Yards to Miles':{
                '' : 'Yards * 0.0005682'
            },
        }
#}}}_________________________________________________________________________________________
    
    def form_feet(self):
            argsOut = ['Feet to Miles', 'Enter Feet']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * .0001894
            return (result, self.pluralize(result, 'Mile'))
            
    def form_miles(self):
            argsOut = ['Miles to Feet', 'Enter Miles']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * 5280
            return (result, self.pluralize(result, 'Foot'))
            
    def form_ounces(self):
            argsOut = ['Ounces to Pounds', 'Enter Ounces']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * .0625
            return (result, self.pluralize(result, 'Pound'))
            
    def form_pounds(self):
            argsOut = ['Pounds to Ounces', 'Enter Pounds']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * 16
            return (result, self.pluralize(result, 'Ounce'))
            
    def form_tons(self):
            argsOut = ['Tons to Pounds', 'Enter Tons']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * 2000
            return (result, self.pluralize(result, 'Pound'))
            
    def form_yards(self):
            argsOut = ['Yards to Miles', 'Enter Yards']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * .0005682
            return (result, self.pluralize(result, 'Mile'))

#!/usr/bin/env python3
#
# Torque.py
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
from collections import OrderedDict

class Torque(FormulaBase):
    def __init__(self, name):
        super(Torque, self).__init__(name)
        self.name = name
        
        self.function_list = {
            'Gram-Centimeters to Ounce-Inches': self.form_gramcent,
            'Newton-Meters to Pound-Feet': self.form_newtmeter,
            'Newton-Meters to Pound-Inches': self.form_newtmeter2,
            'Ounce-Inches to Gram-Centimeters': self.form_ouncein,
            'Pound-Feet to Newton-Meters': self.form_poundfeet,
            'Pound-Inhces to Newton-Meters': self.form_poundinch
        }
#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            'Gram-Centimeters to Ounce-Inches':{
                '': 'Gram-Centimeters * 0.139'
            },
            'Newton-Meters to Pound-Feet':{
                '' : 'Newton-Meters * 0.7376'
            },
            'Newton-Meters to Pound-Inches':{
                '' : 'Newton-Meters * 8.851'
            },
            'Ounce-Inches to Gram-Centimeters':{
                '' : 'Ounce-Inches * 72'
            },
            'Pound/Feet to Newton/Meters':{
                '' : 'Pound/Feet * 1.3558'
            },
            'Pound-Inches to Newton-Meters':{
                '' : 'Pound-Inches * 0.113'
            }
        }

#}}}_________________________________________________________________________________________
            
    def form_gramcent(self):
        argsOut = ['Gram-Centimeters to Ounce-Inches', 'Enter Gram-Centimeters']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0139
        return (result, self.pluralize(result, 'Ounce-Inch'))
            
    def form_newtmeter(self):
        argsOut = ['Newton-Meters to Pound-Feet', 'Enter Newton-Meters',]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .7376
        return (result, self.pluralize(result, 'Pound-Foot'))
            
    def form_newtmeter2(self):
        argsOut = ['Newton-Meters to Pound-Inches', 'Enter Newton-Meters']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 8.851
        return (result, self.pluralize(result, 'Pound-Inch'))
            
    def form_ouncein(self):
        argsOut = ['Ounce-Inches to Gram-Centimeters', 'Enter Ounce-Inches']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 72.0
        return (result, self.pluralize(result, 'Gram-Centimeter'))
            
    def form_poundfeet(self):
        argsOut = ['Pound-Feet to Newton-Meters', 'Enter Pound-Feet']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.3558
        return (result, self.pluralize(result, 'Newton-Meter'))
            
    def form_poundinch(self):
        argsOut = ['Pound-Inches to Newton-Meters', 'Enter Pound-Inches']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .113
        return (result, self.pluralize(result, 'Newton-Meter'))
            
    

#!/usr/bin/python
#
# Light.py
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

class Light(FormulaBase):
    def __init__(self, name): 
        super(Light, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Foot Candles to Lumens/Meter Squared',
            2 : 'Lumens/Meter Squared to Foot Candles',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.foot),
                (self.function_strings[2], self.lumens),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[1]:{
                    'number_input' : 'Foot Candles: '
            },
            self.function_strings[2]:{
                    'number_input' : 'Lumens/Meter<sup>2</sup>: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{
                '' : 'Foot Candles * 10.76'
            },
            self.function_strings[2]:{
                '' : 'Lumens/Meter Squared * 0.0929'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def foot (self):
        title = self.function_strings[1]
        fc = "Enter Foot Candles"
        argsOut = [title, fc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 10.76
        return (self.prec(result, 2), self.pluralize(result, 'Lumens/Meter<sup>2</sup>'))

    def lumens (self):
        title = self.function_strings[2]
        lms = "Enter Lumens/Meter Squared"
        argsOut = [title, lms]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0929
        return (self.prec(result, 2), self.pluralize(result, 'Foot Candle'))
#}}}_________________________________________________________________________________________


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

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                ('Foot Candles to Lumens/Meter Squared', self.foot),
                ('Lumens/Meter Squared to Foot Candles', self.lumens),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            'Foot Candles to Lumens/Meter Squared':{
                    'number_input' : 'Foot Candles: '
            },
            'Lumens/Meter Squared to Foot Candles':{
                    'number_input' : 'Lumens/Meter<sup>2</sup>: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            'Foot Candles to Lumens/Meter Squared':{
                '' : 'Foot Candles * 10.76'
            },
            'Lumens/Meter Squared to Foot Candles':{
                '' : 'Lumens/Meter Squared * 0.0929'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def foot (self):
        title = "Foot Candles to Lumens/Meter Squared"
        fc = "Enter Foot Candles"
        argsOut = [title, fc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 10.76
        return (self.prec2(result), self.pluralize(result, 'Lumens/Meter<sup>2</sup>'))

    def lumens (self):
        title = "Lumens/Meter Squared to Foot Candles"
        lms = "Enter Lumens/Meter Squared"
        argsOut = [title, lms]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0929
        return (self.prec2(result), self.pluralize(result, 'Foot Candle'))
#}}}_________________________________________________________________________________________


#!/usr/bin/python
#
# Mass.py
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

class Mass(FormulaBase):
    def __init__(self):
        super (Mass, self).__init__()

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
                [
                    ('Tons to Kilograms', self.tons),
                    ('Kilograms to Tons', self.kilo),
                    ('Tons to Metric Tons', self.tons2),
                    ('Metric Tons to Tons', self.tons3),
                    ('Grains to Drams', self.grains),
                    ('Grains to Ounces', self.grains2),
                    ('Grains to Grams', self.grains3),
                ]
            )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
                'Tons to Kilograms':{
                    'number_input' : 'Tons (input): '
                    },
                'Kilograms to Tons':{
                    'number_input' : 'Kilograms (input): '
                    },
                'Tons to Metric Tons':{
                    'number_input' : 'Tons (input): '
                    },
                'Metric Tons to Tons':{
                    'number_input' : 'Metric Tons (input): '
                    },
                'Grains to Drams':{
                    'number_input' : 'Grains (input): '
                    },
                'Grains to Ounces':{
                    'number_input' : 'Grains (input): '
                    },
                'Grains to Grams':{
                    'number_input' : 'Grains (input): '
                    },
            }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Tons to Kilograms':{
                '' : 'Tons * 907.18'
            },
            'Kilograms to Tons':{
                '' : 'Kilograms * 0.001102'
            },
            'Tons to Metric Tons':{
                '' : 'Tons * 0.90718'
            },
            'Metric Tons to Tons':{
                '' : 'Metric Tons * 1.1023'
            },
            'Grains to Drams':{
                '' : 'Grains * 0.0365764447696'
            },
            'Grains to Ounces':{
                '' : 'Grains * 0.00228571'
            },
            'Grains to Grams':{
                '' : 'Grains * 15.43236'
            },
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Formula Functions _____________________________________________________________________________

    def tons(self, num):
        result = float(num) * 907.18
        return (self.prec2(result), self.pluralize(result, 'Kilogram'))

    def kilo(self, num):
        result = float(num) * .001102
        return (self.prec2(result), self.pluralize(result, 'Ton'))

    def tons2(self, num):
        result = float(num) * .90718
        return (self.prec2(result), self.pluralize(result, 'Metric Ton'))

    def tons3(self, num):
        result = float(num) * 1.1023
        return (self.prec2(result), self.pluralize(result, 'Ton'))

    def grains(self, num):
        result = float(num) * .0365764447696
        return (self.prec2(result), self.pluralize(result, 'Dram'))

    def grains2(self, num):
        result = float(num) * .00228571
        return (self.prec2(result), self.pluralize(result, 'Ounce'))

    def grains3(self, num):
        result = float(num) * 15.43236
        return (self.prec2(result), self.pluralize(result, 'Gram'))
#}}}_________________________________________________________________________________________


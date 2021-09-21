#!/usr/bin/python
#SYNOPSIS: Converting Maritime Measurements to statute/metric
#
# Maritime_Measurements.py
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

class Maritime_Measurements(FormulaBase):
    """
    This class represents Converting Maritime Measurements
    """

    def __init__(self, name):
        super(Maritime_Measurements, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Fathoms to Feet',
            2 : 'Cable to Fathom',
            3 : 'Nautical Miles to Feet',
            4 : 'Fathoms to Meters',
            5 : 'Nautical Miles to Cables',
            6 : 'Nautical Miles to Meters',
            7 : 'Nautical Miles to Statute Miles',
            8 : 'Knots to Nautical Miles per Hour',
            9 : 'Meters to Fathoms',
            10 : 'Nautical Miles to Kilometers',
            11 : 'Kilometers to Nautical Miles',
            12 : 'Miles to Nautical Miles',
            13 : 'Knots to Kilometers per Hour',
            14 : 'Kilometers per Hour to Knots',
            15 : 'Knots to Miles per Hour',
            16 : 'Miles per Hour to Knots',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.ff),
                (self.function_strings[2], self.cf),
                (self.function_strings[3], self.nmf),
                (self.function_strings[4], self.fm),
                (self.function_strings[5], self.nmc),
                (self.function_strings[6], self.nmm),
                (self.function_strings[7], self.nmsm),
                (self.function_strings[8], self.knots),
                (self.function_strings[9], self.mf),
                (self.function_strings[10], self.nmk),
                (self.function_strings[11], self.knm),
                (self.function_strings[12], self.Mnm),
                (self.function_strings[13], self.Kkph),
                (self.function_strings[14], self.kphK),
                (self.function_strings[15], self.Kmph),
                (self.function_strings[16], self.mphK),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
            self.function_strings[1]:{
                'number_input' : 'Fathoms (input):'
                    },
            self.function_strings[2]:{
                'number_input' : 'Cable (input):'
                    },
            self.function_strings[3]:{
                'number_input' : 'Nautical Miles (input):'
                    },
            self.function_strings[4]:{
                'number_input' : 'Fathom (input):'
                    },
            self.function_strings[5]:{
                'number_input' : 'Nautical Miles (input):'
                    },
            self.function_strings[6]:{
                'number_input' : 'Nautical Miles (input):'
                    },
            self.function_strings[7]:{
                'number_input' : 'Nautical Miles (input):'
                    },
            self.function_strings[8]:{
                'number_input' : 'Knots (input):'
                    },
            self.function_strings[9]:{
                'number_input' : 'Meter (input):'
                    },
            self.function_strings[10]:{
                'number_input' : 'Nautical Miles (input):'
                    },
            self.function_strings[11]:{
                'number_input' : 'Kilometers (input):'
                    },
            self.function_strings[12]:{
                'number_input' : 'Miles (input):'
                    },
            self.function_strings[13]:{
                'number_input' : 'Knots (input):'
                    },
            self.function_strings[14]:{
                'number_input' : 'Kilometers per Hour (input):'
                    },
            self.function_strings[15]:{
                'number_input' : 'Knots (input):'
                    },
            self.function_strings[16]:{
                'number_input' : 'Miles per Hour (input):'
                    },
            }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{
                '' : 'Fathom * 6'
            },
            self.function_strings[2]:{
                '' : 'Cable * 0.01'
            },
            self.function_strings[3]:{
                '' : 'Nautical Miles * 6076'
            },
            self.function_strings[4]:{
                '' : 'Fathoms * 0.546448087'
            },
            self.function_strings[5]:{
                '' : 'Nautical Miles * 10'
            },
            self.function_strings[6]:{
                '' : 'Nautical Miles * 1852'
            },
            self.function_strings[7]:{
                '' : 'Nautical Miles * 1.15'
            },
            self.function_strings[8]:{
                '' : 'Knots * 1'
            },
            self.function_strings[9]:{
                '' : 'Meters * 1.83'
            },
            self.function_strings[10]:{
                '' : 'Nautical Miles * 0.539956803456'
            },
            self.function_strings[11]:{
                '' : 'Kilometers * 1.852'
            },
            self.function_strings[12]:{
                '' : 'Miles * 1.150775577122'
            },
            self.function_strings[13]:{
                '' : 'Kilometer * 1.93968964967'
            },
            self.function_strings[14]:{
                '' : 'Kilometers per Hour * 0.59'
            },
            self.function_strings[16]:{
                '' : 'Miles per Hour * 1.69491525424'
            },
            self.function_strings[15]:{
                '' : 'Knots * 0.59'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def ff(self):
        title = self.function_strings[1]
        fath = "Enter Fathoms"
        argsOut = [title, fath]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 6
        return (self.prec2(result), self.pluralize(result, "Foot"))

    def cf(self):
        title = self.function_strings[2]
        cb = "Enter Cables"
        argsOut = [title, cb]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .01
        return (self.prec2(result) , self.pluralize(result, "Fathom"))

    def nmf(self):
        title = self.function_strings[3]
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 6076
        return (self.prec2(result), self.pluralize(result, "Foot"))

    def fm(self):
        title = self.function_strings[4]
        fath = "Enter Fathoms"
        argsOut = [title, fath]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .546448087
        return (self.prec2(result), self.pluralize(result, "Meter"))

    def nmc(self):
        title = self.function_strings[5]
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 10
        return (self.prec2(result), self.pluralize(result, "Cable"))

    def nmm(self):
        title = self.function_strings[6]
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1852
        return (self.prec2(result), self.pluralize(result, "Meter"))

    def nmsm(self):
        title = self.function_strings[7]
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.15
        return (self.prec2(result), self.pluralize(result, "Statute Mile"))

    def knots(self):
        title = self.function_strings[8]
        knot = "Enter Knots"
        argsOut = [title, knot]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1
        return (self.prec2(result), self.pluralize(result, "Nautical Mile"))

    def mf(self):
        title = self.function_strings[9]
        m = "Enter Meters"
        argsOut = [title, m]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.83
        return (self.prec2(result), self.pluralize(result, "Fathom"))

    def nmk(self):
        title = self.function_strings[10]
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .539956803456
        return (self.prec2(result), self.pluralize(result, "Kilometer"))

    def knm(self):
        title = self.function_strings[11]
        k = "Enter Kilometers"
        argsOut = [title, k]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.852
        return (self.prec2(result), self.pluralize(result, "Nautical Mile"))

    def Mnm(self):
        title = self.function_strings[12]
        M = "Enter Miles"
        argsOut = [title, M]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.150774477122
        return (self.prec2(result), self.pluralize(result, "Nautical Mile"))

    def Kkph(self):
        title = self.function_strings[13]
        K = "Enter Kilometers"
        argsOut = [title, K]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.93968964967
        return (self.prec2(result), self.pluralize(result, "Kilometer per Hour"))

    def kphK(self):
        title = self.function_strings[14]
        kph = "Enter Kilometers per Hour"
        argsOut = [title, kph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .515546391749
        return (self.prec2(result), self.pluralize(result, "Knot"))

    def Kmph(self):
        title = self.function_strings[15]
        K = "Enter Knots"
        argsOut = [title, K]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .59
        return (self.prec2(result), self.pluralize(result, "Mile per Hour"))

    def mphK(self):
        title = self.function_strings[16]
        mph = "Enter Miles per Hour"
        argsOut = [title, mph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.69491525424
        return (self.prec2(result), self.pluralize(result, "Knot"))
#}}}_________________________________________________________________________________________


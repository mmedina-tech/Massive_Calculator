#!/usr/bin/python
#
# Fuel_Economy.py
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

class Fuel_Economy(FormulaBase):
    def __init__(self, name): 
        super(Fuel_Economy, self).__init__(name)
        self.name = name

        self.function_list = {
#{{{___ Function List _____________________________________________________________________________
            'Miles/Gal to Kilometers/Liter': self.miles,
            'Kilometers/Liter to Miles/Gal': self.kilo,
#}}}_________________________________________________________________________________________

        }

        self.functionInputs = {
#{{{___ Inputs _____________________________________________________________________________

            'Miles/Gal to Kilometers/Liter':{
                    'number_input' : 'Miles/Gal: '
            },
            'Kilometers/Liter to Miles/Gal':{
                    'number_input' : 'Kilometers/Liter: '
            },
#}}}_________________________________________________________________________________________

        }

        self.formula_list = {
#{{{___ Formula List _____________________________________________________________________________

            'Miles/Gal to Kilometers/Liter':{
                '' : 'Miles/Gal * 0.42514'
            },
            'Kilometers/Liter to Miles/Gal':{
                '' : 'Kilometers/Liter * 2.3522'
            }
#}}}_________________________________________________________________________________________

        }

#{{{___ Formula Functions _____________________________________________________________________________

    def miles (self):
        title = "Miles/Gal to Kilometers/Liter"
        mpg = "Enter Miles/Gal"
        argsOut = [title, mpg]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .42514
        return (self.prec2(result), self.pluralize(result, 'Kilometers/Liter'))

    def kilo (self):
        title = "Kilometers/Liter to Miles/Gal"
        kpl = "Enter Kilometers/Liter"
        argsOut = [title, kpl]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.3522
        return (self.prec2(result), self.pluralize(result, 'Miles/Gal'))

#}}}_________________________________________________________________________________________


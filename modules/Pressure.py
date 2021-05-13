#!/usr/bin/python
#
# Pressure.py
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

class Pressure(FormulaBase):
    def __init__(self, name): 
        super(Pressure, self).__init__(name)
        self.name = name

#{{{___ Function List _____________________________________________________________________________

        self.function_list = {
            'Bars to KiloPascals': self.bars,
            'Bars to PSI': self.bars2,
            'Inches of Mercury to KiloPascals': self.InHg,
            'Inches of Water to KiloPascals': self.InH2O,
            'KiloPascals to Bars': self.kbars,
            'KiloPascals to Inches of Mercury': self.KpHg,
            'KiloPascals to PSI': self.KpPSI,
            'Pascals to Pounds per Square Foot': self.pascal,
            'Pounds per Square Foot to Pascals': self.psf,
            'PSI to KiloPascals': self.PSI,
        }
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            'Bars to KiloPascals':{
                    'number_input' : 'Bars: '
            },
            'Bars to PSI':{
                    'number_input' : 'Bars: '
            },
            'Inches of Mercury to KiloPascals':{
                    'number_input' : 'Inches ot Mercury: '
            },
            'Inches of Water to KiloPascals':{
                    'number_input' : 'Inches of Water: '
            },
            'KiloPascals to Bars':{
                    'number_input' : 'KiloPascals: '
            },
            'KiloPascals to Inches of Mercury':{
                    'number_input' : 'KiloPascals: '
            },
            'KiloPascals to Inches of Water':{
                    'number_input' : 'KiloPascals: '
            },
            'Pascals to Pounds per Square Foot':{
                    'number_input' : 'Pascals: '
            },
            'Pounds per Square Foot to Pascals':{
                    'number_input' : 'Pounds: '
            },
            'PSI to KiloPascals':{
                    'number_input' : 'PSI: '
            },
        }	
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.fomrula_list = {
            'Inches of Mercury to KiloPascals':{
                '' : 'Inches of Mercury * 3.377'
            },
            'KiloPascals to Inches of Mercury':{
                '' : 'KiloPascals * 0.2961'
            },
            'PSI to KiloPascals':{
                '' : 'PSI * 6.895'
            },
            'KiloPascals to PSI':{
                '' : 'KiloPascals * 0.145'
            },
            'Inches of Water to KiloPascals':{
                '' : 'Inches of Water * 0.2488'
            },
            'Bars to KiloPascals':{
                '' : 'Bars * 100'
            },
            'KiloPascals to Bars':{
                '' : 'KiloPascals * 0.01'
            },
            'Pascals to Pounds per Square Foot':{
                '' : 'Pascals * 0.02088'
            },
            'Pounds per Square Foot to Pascals':{
                '' : 'Pounds per Square Foot * 47.88'
            },
            'Bars to PSI':{
                '' : '(Bars * 100) * .145'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def InHg (self):
        title = "Inches of Mercury to KiloPascals"
        InHg = "Enter Inches of Mercury"
        argsOut = [title, InHg]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.377
        return (self.prec4(result), self.pluralize(result, 'KiloPascal'))

    def KpHg (self):
        title = "KiloPascals to Inches of Mercury"
        Kp = "Enter KiloPascals"
        argsOut = [title, Kp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2961
        return (self.prec4(result), self.pluralize(result, 'Inches of Mercury'))

    def PSI (self):
        title = "PSI to KiloPascals"
        psi = "Enter PSI"
        argsOut = [title, psi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 6.895
        return (self.prec4(result), self.pluralize(result, 'KiloPascal'))

    def KpPSI (self):
        title = "KiloPascals to PSI"
        Kp = "Enter KiloPascals"
        argsOut = [title, Kp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .145
        return (self.prec4(result), self.pluralize(result, 'PSI'))
    
    def InH2O (self):
        title = "Inches of Water to KiloPascals"
        InH2O = "Enter Inches of Water"
        argsOut = [title, InH2O]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2488
        return (self.prec4(result), self.pluralize(result, 'KiloPascal'))

    def bars (self):
        title = "Bars to KiloPascals"
        bar = "Enter Bars"
        argsOut = [title, bar]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 100
        return (self.prec4(result), self.pluralize(result, 'KiloPascal'))

    def kbars (self):
        title = "KiloPascals to Bars"
        Kp = "Enter KiloPascals"
        argsOut = [title, Kp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .01
        return (self.prec4(result), self.pluralize(result, 'Bar'))

    def psf (self):
        title = "Pounds per Square Foot to Pascals"
        psf = "Enter Pounds per Square Foot"
        argsOut = [title, psf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 47.88
        return (self.prec4(result), self.pluralize(result, 'Pascal'))

    def pascal (self):
        title = "Pascal to Pounds per Square Foot"
        pas = "Enter Pascal"
        argsOut = [title, pas]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .02088
        return (self.prec4(result), self.pluralize(result, 'Pounds per Square Foot'))

    def bars2 (self):
        title = "Bars to PSI"
        bar = "Enter Bars"
        argsOut = [title, bar]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] * 100) * .145
        return (self.prec4(result), self.pluralize(result, 'PSI'))
#}}}_________________________________________________________________________________________


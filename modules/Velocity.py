#!/usr/bin/python
#
# Velocity.py
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

class Velocity (FormulaBase):
    def __init__(self, name):
        super (Velocity, self).__init__(name)
        self.name = name

#{{{___ Function List _____________________________________________________________________________

        self.function_list = {
            'Miles/hr to Kilometers/hr': self.mph,
            'Kilometers/hr to Miles/hr': self.kph,
            'Feet/Sec to Meters/Sec': self.ftmt,
            'Meters/Sec to Feet/Sec': self.mtft,
            'Kilometers/hr to Meters/Sec': self.kphmt,
            'Meters/Sec to Kilometers/hr': self.mtkph,
            'Miles/hr to Meters/Sec': self.mphmt,
            'Meters/Sec to Miles/hr': self.mtmph,
        }
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
                'Miles/hr to Kilometers/hr':{
                    'number_input' : 'Miles/hr (input): '
                    },
                'Kilometers/hr to Miles/hr':{
                    'number_input' : 'Kilometers/hr (input): '
                    },
                'Feet/Sec to Meters/Sec':{
                    'number_input' : 'Feet/Sec (input): '
                    },
                'Meters/Sec to Feet/Sec':{
                    'number_input' : 'Meters/Sec (input): '
                    },
                'Kilometers/hr to Meters/Sec':{
                    'number_input' : 'Kilometers/hr (input): '
                    },
                'Meters/Sec to Kilometers/hr':{
                    'number_input' : 'Meters/Sec (input): '
                    },
                'Miles/hr to Meters/Sec':{
                    'number_input' : 'Miles/hr (input): '
                    },
                'Meters/Sec to Miles/hr':{
                    'number_input' : 'Meters/Sec (input): '
                    },
            }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________
        self.formula_list = {
            'Miles/hr to Kilometers/hr':{
                '' : 'Miles/hr * 1.6093'
            },
            'Kilometers/hr to Miles/hr':{
                '' : 'Kilometers/hr * 0.6214'
            },
            'Feet/Sec to Meters/Sec':{
                '' : 'Feet/Sec * 0.3648'
            },
            'Meters/Sec to Feet/Sec':{
                '' : 'Meters/Sec * 3.281'
            },
            'Kilometers/hr to Meters/Sec':{
                '' : 'Kilometers/hr * 0.27778'
            },
            'Meters/Sec to Kilometers/hr':{
                '' : 'Meters/Sec * 3.6'
            },
            'Miles/hr to Meters/Sec':{
                '' : 'Miles/hr * 0.4470'
            },
            'Meters/Sec to Miles/hr':{
                '' : 'Meters/Sec * 2.237'
            }
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def mph(self):
        title = "Miles per Hour to Kilometers per Hour"
        mph = "Enter Miles per Hour"
        argsOut = [title, mph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.6093
        return (self.prec(result, 2), self.pluralize(result, 'Kilometers/hr'))

    def kph(self):
        title = "Kilometers per Hour to Miles per Hour"
        kph = "Enter Kilometers per Hour"
        argsOut = [title, kph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .6214
        return (self.prec(result, 2), self.pluralize(result, 'Miles/hr'))

    def ftmt(self):
        title = "Feet/Sec to Meters/Sec"
        ft = 'Enter Feet/Sec'
        argsOut = [title, ft]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .3648
        return (self.prec(result, 2), self.pluralize(result, 'Meters/Sec'))

    def mtft(self):
        title = 'Meters/Sec to Feet/Sec'
        mt = 'Enter Meters/Sec'
        argsOut = [title, mt]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.281
        return (self.prec(result, 2), self.pluralize(result, 'Feet/Sec'))

    def kphmt(self):
        title = 'Kilometers per Hour to Meters/Sec'
        kph = 'Enter Kilometers per Hour'
        argsOut = [title, kph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .27778
        return (self.prec(result, 2), self.pluralize(result, 'Meters/Sec'))

    def mtkph(self):
        title = 'Meters/Sec to Kilometers per Hour'
        mt = 'Enter Meters/Sec'
        argsOut = [title, mt]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.6
        return (self.prec(result, 2), self.pluralize(result, 'Kilometers/hr'))

    def mphmt(self):
        title = 'Miles per Hour to Meters/Sec'
        mph = 'Enter Miles per Hour'
        argsOut = [title, mph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .4470
        return (self.prec(result, 2), self.pluralize(result, 'Meters/Sec'))

    def mtmph(self):
        title = 'Meters/Sec to Miles per Hour'
        mt = 'Enter Meters/Sec'
        argsOut = [title, mt]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.237
        return (self.prec(result, 2), self.pluralize(result, 'Miles/hr'))
#}}}_________________________________________________________________________________________


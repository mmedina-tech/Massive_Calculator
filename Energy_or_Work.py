#!/usr/bin/python
#
# Energy_or_Work.py
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


class Energy_or_Work(FormulaBase):
	def __init__(self, name):
            super(Energy_or_Work, self).__init__(name)
            self.name = name
            
            self.function_list = {
                'BTU to Foot-Pounds': self.form_btu,
                'BTU to Gram-Calories': self.form_btu2
            }
	
	def form_btu(self):
		argsOut = ['BTU to Foot-Pounds', 'Enter BTUs']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 778.2
		return (result, self.pluralize(result, 'Foot-Pound'))
		
	def form_btu2(self):
		argsOut = ['BTU to Gram-Calories', 'Enter BTUs']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 252.0
		return (result, self.pluralize(result, 'Gram-Calorie'))

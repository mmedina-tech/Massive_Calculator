#!/usr/bin/python
#
# PlaneAngle.py
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

class PlaneAngle(FormulaBase):
	def __init__(self, name):
		super(PlaneAngle, self).__init__(name)
		self.name = name
		
		self.function_list = {
                    'Degrees to Radians': self.form_degrees,
                    'Minutes to Degrees': self.form_minutes,
                    'Quadrants to Degrees': self.form_quadrants,
                    'Quadrants to Radians': self.form_quadrants2,
                    'Radians to Degress': self.form_radians
                }
		
	def form_degrees(self):
		argsOut = ['Degrees to Radians', 'Enter Degrees']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0175
		return (result, self.pluralize(result, 'Radian'))
		
	def form_minutes(self):
		argsOut = ['Minutes to Degrees', 'Enter Minutes']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .1667
		return (result, self.pluralize(result, 'Degree'))
		
	def form_minutes2(self):
		argsOut = ['Minutes to Radians', 'Enter Minutes']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * (2.9 * 10 ** (-4))
		return (result, self.pluralize(result, 'Radian'))
		
	def form_quadrants(self):
		argsOut = ['Quadrants to Degrees', 'Enter Quadrant']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 90.0
		return (result, self.pluralize(result, 'Degree'))
		
	def form_quadrants2(self):
		argsOut = ['Quadrants to Radians', 'Enter Quadrant']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.5708
		return (result, self.pluralize(result, 'Radian'))
		
	def form_radians(self):
		argsOut = ['Radians to Degrees', 'Enter Radians']
		argsIn =self.prompt(argsOut)
		result = argsIn[0] * 57.3
		return (result, self.pluralize(result, 'Degree'))

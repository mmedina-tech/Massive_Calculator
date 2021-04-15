#!/usr/bin/python
# SYNOPSIS: Power Module for Massive Calculator
# 
# Power.py
#
# Author: Marcus Medina,,,
# Date: Thu 15 Apr 2021 08:18:08 AM PDT
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or 
# (at your option) any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABLILITY of FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You Should have recieved a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
#
#

from FormulaBase import *
from collections import OrderedDict

class Power(FormulaBase):
	def __init__(self, name):
		super(Power, self).__init__(name)
		self.name = name 
		
		self.function_list = {
                    'BTU per Hour to Watts': self.form_btuhour,
                    'Horse Power to Foot/Pounds per Minute': self.form_hpftlbsm,
                    'Horse Power to Foot/Pounds per Second': self.form_hpftlbss,
                    'Horse Power to Watts': self.form_hpw,
                    'Kilo Watts to Horse Power': self.form_kwhp
                }
		
	def form_btuhour(self):
		argsOut = ['BTU per Hour to Watts', 'Enter BTUs']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .293
		return (result, self.pluralize(result, 'Watt'))
		
	def form_hpftlbsm(self):
		argsOut = ['Horse Power to Foot/Pounds per Minute', 'Enter Horse Power']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 33000
		return (result, self.pluralize(result, 'Foot/Pounds per Minute'))
		
	def form_hpftlbss(self):
		argsOut = ['Horse Power to Foor/Pounds per Second', 'Enter Horse Power']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 550.0
		return (result, self.pluralize(result, 'Foot/Pounds per Second'))
		
	def form_hpw(self):
		argsOut = ['Horse Power to Watts', 'Enter Horse Power']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 746.0
		return (result, self.pluralize(result, 'Watt'))
		
	def form_kwhp(self):
		argsOut = ['Kilo Watts to Horse Power', 'Enter Kilo Watts']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.341
		return (result, self.pluralize(result, 'Horse Power'))

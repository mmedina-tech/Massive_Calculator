#!/usr/bin/env python

from FormulaBase import *
from collections import OrderedDict


class Energy_or_Work(FormulaBase):
	def __init__(self, name):
		super(Energy_or_Work, self).__init__(name)
		self.name = name
		
		self.function_list = OrderedDict(
		[
			('BTU to Foot-Pounds', self.form_btu),
			('BTU to Gram-Calories', self.form_btu2)
		]
	)
	
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

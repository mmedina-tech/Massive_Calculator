#!/usr/bin/env python

from FormulaBase import *
from collections import OrderedDict


class Imperial_to_Imperial(FormulaBase):
	def __init__(self, name):
		super(Imperial_to_Imperial, self).__init__(name)
		self.name = name
		
		self.function_list = OrderedDict(
		[
			('Feet to Miles', self.form_feet),
			('Miles to Feet', self.form_miles),
			('Ounces to Pounds', self.form_ounces),
			('Pounds to Ounces', self.form_pounds),
			('Tons to Pounds', self.form_tons),
			('Yards to Miles', self.form_yards)
		]
	)
	
	def form_feet(self):
		argsOut = ['Feet to Miles', 'Enter Feet']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0001894
		return (result, self.pluralize(result, 'Mile'))
		
	def form_miles(self):
		argsOut = ['Miles to Feet', 'Enter Miles']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 5280
		return (result, self.pluralize(result, 'Foot'))
		
	def form_ounces(self):
		argsOut = ['Ounces to Pounds', 'Enter Ounces']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0625
		return (result, self.pluralize(result, 'Pound'))
		
	def form_pounds(self):
		argsOut = ['Pounds to Ounces', 'Enter Pounds']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 16
		return (result, self.pluralize(result, 'Ounce'))
		
	def form_tons(self):
		argsOut = ['Tons to Pounds', 'Enter Tons']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 2000
		return (result, self.pluralize(result, 'Pound'))
		
	def form_yards(self):
		argsOut = ['Yards to Miles', 'Enter Yards']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0005682
		return (result, self.pluralize(result, 'Mile'))

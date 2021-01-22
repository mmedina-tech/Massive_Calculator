#!/usr/bin/env python

from FormulaBase import *
from collections import OrderedDict

class Torque(FormulaBase):
	def __init__(self, name):
		super(Torque, self).__init__(name)
		self.name = name
		
		self.function_list = OrderedDict(
		[
			('Gram-Centimeters to Ounce-Inches', self.form_gramcent),
			('Newton-Meters to Pound-Feet', self.form_newtmeter),
			('Newton-Meters to Pound-Inches', self.form_newtmeter2),
			('Ounce-Inches to Gram-Centimeters', self.form_ouncein),
			('Pound-Feet to Newton-Meters', self.form_poundfeet),
			('Pound-Inhces to Newton-Meters', self.form_poundinch)
		]
	)
		
	def form_gramcent(self):
		argsOut = ['Gram-Centimeters to Ounce-Inches', 'Enter Gram-Centimeters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0139
		return (result, self.pluralize(result, 'Ounce-Inch'))
		
	def form_newtmeter(self):
		argsOut = ['Newton-Meters to Pound-Feet', 'Enter Newton-Meters',]
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .7376
		return (result, self.pluralize(result, 'Pound-Foot'))
		
	def form_newtmeter2(self):
		argsOut = ['Newton-Meters to Pound-Inches', 'Enter Newton-Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 8.851
		return (result, self.pluralize(result, 'Pound-Inch'))
		
	def form_ouncein(self):
		argsOut = ['Ounce-Inches to Gram-Centimeters', 'Enter Ounce-Inches']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 72.0
		return (result, self.pluralize(result, 'Gram-Centimeter'))
		
	def form_poundfeet(self):
		argsOut = ['Pound-Feet to Newton-Meters', 'Enter Pound-Feet']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.3558
		return (result, self.pluralize(result, 'Newton-Meter'))
		
	def form_poundinch(self):
		argsOut = ['Pound-Inches to Newton-Meters', 'Enter Pound-Inches']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .113
		return (result, self.pluralize(result, 'Newton-Meter'))
		
	

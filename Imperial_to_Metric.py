#!/usr/bin/env python

from FormulaBase import *
from collections import OrderedDict


class Imperial_to_Metric(FormulaBase):
	def __init__(self, name):
		super(Imperial_to_Metric, self).__init__(name)
		self.name = name
		
		self.function_list = OrderedDict(
		[
			('Fahrenheit to Celsius', self.form_fahrenheit),
			('Cubic Yards to Cubic Meters', self.form_cuyards),
			('Feet to Meters', self.form_feet),
			('Gallons to Liters', self.form_gallons),
			('Inches to Millimeters', self.form_inches),
			('Inches to Centimeters', self.form_inches2),
			('Miles to Kilometers', self.form_miles),
			('Ounces to Grams', self.form_ounces),
			('Pints to Liters', self.form_pints),
			('Quarts to Liters', self.form_quarts),
			('Pounds to Kilograms', self.form_pounds),
			('Square Feet to Square Meters', self.form_sqfeet),
			('Square Miles to Square Meters', self.form_sqmiles),
			('Sqaure Yards to Square Meters', self.form_sqyards),
			('Yards to Meters', self.form_yards)
		]
	)
		
	def form_fahrenheit(self):
		argsOut = ['Fahrenheit to Celsius', 'Enter Fahrenheit']
		argsIn = self.prompt(argsOut)
		result = (argsIn[0] - 32) * 5/9
		return (result, self.pluralize(result, 'Celsius'))
		
	def form_cuyards(self):
		argsOut = ['Cubic Yards to Cubic Meters', 'Enter Cubic Yards']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .7646
		return (result, self.pluralize(result, 'Cubic Meter'))
		
	def form_feet(self):
		argsOut = ['Feet to Meters', 'Enter Feet']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .3048
		return (result, self.pluralize(result, 'Meter'))
		
	def form_gallons(self):
		argsOut = ['Gallons to Liters', 'Enter Gallons']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 3.7853
		return (result, self.pluralize(result, 'Liter'))
		
	def form_inches2(self):
		argsOut = ['Inches to Centimeters', 'Enter Inches']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 2.54
		return (result, self.pluralize(result, 'Centimter'))
		
	def form_inches(self):
		argsOut = ['Inches to Millimeters', 'Enter Inches']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 25.4
		return (result, self.pluralize(result, 'Millimeter'))
		
	def form_miles(self):
		argsOut = ['Miles to Kilometers', 'Enter Miles']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.6093
		return (result, self.pluralize(result, 'Kilometer'))
		
	def form_ounces(self):
		argsOut = ['Ounces to Grams', 'Enter Ounces']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 28.3495
		return (result, self.pluralize(result, 'Gram'))
		
	def form_pounds(self):
		argsOut = ['Pounds to Kilograms', 'Enter Pounds']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .4536
		return (result, self.pluralize(result, 'Kilogram'))
		
	def form_pints(self):
		argsOut = ['Pints to Liters', 'Enter Pints']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.4732
		return (result, self.pluralize(result, 'Liter'))
		
	def form_quarts(self):
		argsOut = ['Quarts to Liters', 'Enter Quarts']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .9463
		return (result, self.pluralize(result, 'Liter'))
		
	def form_sqfeet(self):
		argsOut = ['Square Feet to Square Meters', 'Enter Square Feet']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .929
		return (result, self.pluralize(result, 'Square Meter'))
		
	def form_sqmiles(self):
		argsOut = ['Square Miles to Square Kilometers', 'Enter Square Miles']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 2.59
		return (result, self.pluralize(result, 'Square Kilometer'))
		
	def form_sqyards(self):
		argsOut = ['Square Yards to Square Meters', 'Enter Square Yards']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .8361
		return (result, self.pluralize(result, 'Square Meter'))
		
	def form_yards(self):
		argsOut = ['Yards to Meters', 'Enter Yards']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .9144
		return (result, self.pluralize(result, 'Meter'))

#!/usr/bin/python

from FormulaBase import *
from collections import OrderedDict


class Metric_to_Imperial(FormulaBase):
	def __init__(self, name):
		super(Metric_to_Imperial, self).__init__(name)
		self.name = name
		
		self.function_list = OrderedDict(
		[
			('Celsius to Fahrenheit', self.form_celsius),
			('Centimeters to Inches', self.form_centimeters),
			('Centimeters to Feet', self.form_centimeters2),
			('Cubic Meters to Cubic Feet', self.form_cumeters),
			('Cubic Meters to Cubic Yards', self.form_cumeters2),
			('Grams to Ounces', self.form_grams),
			('Kilograms to Pounds', self.form_kilograms),
			('Liters to Gallons', self.form_liters),
			('Liters to Pints', self.form_liters2),
			('Liters to Quarts', self.form_liters3),
			('Meters to Feet', self.form_meters),
			('Meters to Miles', self.form_meters2),
			('Meters to Yards', self.form_meters3),
			('Millimeters to Inches', self.form_millimeters),
			('Square Kilometers to Square Miles', self.form_sqkilometers),
			('Square Meters to Square Feet', self.form_sqmeters),
			('Square Meters to Square Yards', self.form_sqmeters2),
			('Kilometers to Miles', self.form_kilometers)
		]
	)
	
	def form_celsius(self):
		argsOut = ['Celsius to Fahrenheit', 'Enter Celsius']
		argsIn = self.prompt(argsOut)
		result = (argsIn[0] * 9/5) + 32
		return (result, self.pluralize(result, 'Fahrenheit'))
		
	def form_centimeters(self):
		argsOut = ['Centimeters to Inches', 'Enter Centimeters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .3937
		return (result, self.pluralize(result, 'Inch'))
		
	def form_centimeters2(self):
		argsOut = ['Centimeters to Feet', 'Enter Centimeters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .03281
		return (result, self.pluralize(result, 'Foot'))
		
	def form_cumeters(self):
		argsOut = ['Cubic Meters to Cubic Feet', 'Enter Cubic Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 35.3145
		return (result, self.pluralize(result, 'Cubic Foot'))
		
	def form_cumeters2(self):
		argsOut = ['Cubic Meters to Cubic Yards', 'Enter Cubic Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.3079
		return (result, self.pluralize(result, 'Cubic Yard'))
		
	def form_kilograms(self):
		argsOut = ['Kilograms to Pounds', 'Enter Kilograms']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 2.2046
		return (result, self.pluralize(result, 'Pound'))
		
	def form_liters(self):
		argsOut = ['Liters to Gallons', 'Enter Liters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .2642
		return (result, self.pluralize(result, 'Gallon'))
		
	def form_liters2(self):
		argsOut = ['Liters to Pints', 'Enter Liters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 2.1134
		return (result, self.pluralize(result, 'Pint'))
		
	def form_liters3(self):
		argsOut = ['Liters to Quarts', 'Enter Liters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.0567
		return (result, self.pluralize(result, 'Quart'))
		
	def form_meters(self):
		argsOut = ['Meters to Feet', 'Enter Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 3.2808
		return (result, self.pluralize(result, 'Foot'))
		
	def form_meters2(self):
		argsOut = ['Meters to Miles', 'Enter Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0006214
		return (result, self.pluralize(result, 'Mile'))
		
	def form_meters3(self):
		argsOut = ['Meters to Yards', 'Enter Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.0936
		return (result, self.pluralize(result, 'Yard'))
		
	def form_millimeters(self):
		argsOut = ['Millimeters to Inches', 'Enter Millimeters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .0394
		return (result, self.pluralize(result, 'Inch'))
		
	def form_sqkilometers(self):
		argsOut = ['Square Kilometers to Square Miles', 'Enter Square Kilometers']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .3861
		return (result, self.pluralize(result, 'Square Mile'))
		
	def form_sqmeters(self):
		argsOut = ['Square Meters to Square Feet', 'Enter Square Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 10.7639
		return (result, self.pluralize(result, 'Square Foot'))
		
	def form_sqmeters2(self):
		argsOut = ['Square Meters to Square Yards', 'Enter Square Meters']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 1.196
		return (result, self.pluralize(result, 'Square Yard'))
		
	def form_kilometers(self):
		argsOut = ['Kilometers to Miles', 'Enter Kilometers']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * .6214
		return (result, self.pluralize(result, 'Mile'))

	def form_grams(self):
		argsOut = ['Grams to Ounces', 'Enter Grams']
		argsIn = self.prompt(argsOut)
		result = argsIn[0] * 128
		return (result, self.pluralize(result, 'Ounce'))

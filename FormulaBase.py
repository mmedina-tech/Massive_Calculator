#!/usr/bin/python
#SYNOPSIS: Setup for The Massive Calculator Back End 
#
# FormulaBase.py
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


import os
from collections import OrderedDict
from math import *
from modules.formats import commas, money

class FormulaBase(object):
	def __init__(self, name=None):
		if name is not None:
			self.menuname = name
		else:
			return None
			
		self.function_list = {}
		
	def get_formla(self, formulaName):
		return self.formula
		
	def get_menu_name(self):
		return self.menuname
		
	def get_category_name(self):
		return self.categoryname
		
	def prompt(self, args):
		argList = []
		print "\nRunning... "+args[0]
		for arg in args[1:]:
                    userStr = raw_input("\t"+arg+": ")
                    argList.append(float(userStr))
		return argList
		
	def pluralize(self, a, b):
		oddplur = {
                #{{{
		'Celsius' : 'Celsius',
		'Fahrenheit' : 'Fahrenheit',
                'Rankine' : 'Rankine',
		'Foot' : 'Feet',
		'Square Foot' : 'Square Feet',
		'Cubic Foot' : 'Cubic Feet',
		'Inch' : 'Inches',
		'Ounce-Inch' : 'Ounce-Inches',
		'Pound-Foot' : 'Pound-Feet',
                'Pound-Inch' : 'Pound-Inches',
		'Horse Power' : 'Horse Power',
		'Foot/Pounds per Minute' : 'Foot/Pounds per Minute',
		'Foot/Pounds per Second' : 'Foot/Pounds per Second',
		'Resistance' : 'Resistance',
		'Kelvin' : 'Kelvin',
		'Inductive Reactance' : 'Inductive Reactance',
		'Impedance' : 'Impedance',
		'Power Factor' : 'Power Factor',
		'Inductor Rating' : 'Inductor Rating',
		'Equity Ratio' : 'Equity Ratio',
		'Trend Percentage' : 'Trend Percentage',
		'Current Ratio' : 'Current Ratio',
		'Gross Margin Percentage' : 'Gross Margin Percentage',
		'Gross Margin' : 'Gross Margin', 
		'Turn-Over Ratio' : 'Turn-Over Ratio',
		'Quick Ratio' : 'Quick Ratio',
		'Receivable Turn-Over' : 'Receivable Turn-Over',
		'Rate of Return' : 'Rate of Return',
		'Total Assets Turn-Over' : 'Total Assets Turn-Over',
		'Earning Per Share' : 'Earnings Per Share',
		'Payout Ratio' : 'Payout Ratio',
		'Cost per Unit' : 'Cost per Unit',
		'Cost Per Portion' : 'Cost Per Portion',
		'Selling Price' : 'Selling Price',
                'New Quantity' : 'New Quantity',
		'Capacitive Reactance' : 'Capacitive Reactance',
		'Capacitor Rating' : 'Capacitor Rating',
		'Body Mass (estimated)' : 'Body Mass (estimated)',
		'Meters/Sec<sup>2</sup>' : 'Meters/Sec<sup>2</sup>',
		'Feet/Sec<sup>2</sup>' : 'Feet/Sec<sup>2</sup>',
		'Inches/Sec<sup>2</sup>' : 'Inches/Sec<sup>2</sup>',
                'Kilometer<sup>2</sup>' : 'Kilometers<sup>2</sup>',
                'Mile<sup>2</sup>' : 'Miles<sup>2</sup>',
                'Inch<sup>2</sup>' : 'Inches<sup>2</sup>',
                'Meter<sup>2</sup>' : 'Meters<sup>2</sup>',
                'Centimeter<sup>2</sup>' : 'Centimeters<sup>2</sup>',
		'Lumens/Meter<sup>2</sup>' : 'Lumens/Meter<sup>2</sup>',
                'Lumens/Meter Squared' : 'Lumens/Meter Squared',
		'Inches of Mercury' : 'Inches of Mercury', 
		'PSI' : 'PSI',
		'Pounds per Foot<sup>2</sup>' : 'Pounds per Feet<sup>2</sup>',
                'Surface Area' : 'Surface Area',
                'Volume' : 'Volume',
                'Triangle Area' : 'Triangle Area',
                'Circle Area' : 'Circle Area',
                'Rectangle Area' : 'Rectangle Area',
                'Parallelogram Area' : 'Parallelogram Area',
                'Trapezoid Area' : 'Trapezoid Area',
                'Miles/hr' : 'Miles/hr',
                'Kilometers/hr' : 'Kilometers/hr',
                'Meters/Sec' : 'Meters/Sec',
                'Feet/Sec' : 'Feet/Sec',
                'Are' : 'Ares',
                'Yard<sup>2</sup>' : 'Yards<sup>2</sup>',
                'Centiare' : 'Centiares',
                'Hectare' : 'Hectares',
                'Link<sup>2</sup>' : 'Links<sup>2</sup>',
                'Pole<sup>2</sup>' :  'Poles<sup>2</sup>',
                'Chain<sup>2</sup>' : 'Chains<sup>2</sup>',
                'Mile<sup>2</sup>' : 'Miles<sup>2</sup>',
                'Section' : 'Sections',
                'Township' : 'Townships',
                'Foot<sup>2</sup>' : 'Feet<sup>2</sup>',
                'Cylinder Surface Area' : 'Cylinder Surface Area',
                'Cylinder Volume' : 'Cylinder Volume',
                'Cone Surface Area' : 'Cone Surface Area',
                'Cone Volume' : 'Cone Volume',
                'Sphere Surface Area' : 'Sphere Surface Area',
                'Sphere Volume' : 'Sphere Volume',
                'Rectange / Right Prism Volume' : 'Rectangle / Right Prism Volume',
                'Pyramid Surface Area' : 'Pyramid Surface Area',
                'Pyramid Volume' : 'Pyramid Volume',
                'Pounds per Square Foot' : 'Pounds per Square Foot',
                'Inductive Reactance Rating' : 'Inductive Reactance Rating',
                #}}}
		}
		
		if a > 1:
			if b in oddplur.keys():
				return oddplur[b]
                        elif b == '':
                            return b
			else:
				return b+'s'
		else:
			return b

	def prec(self, result):
		result = round(result, 1)
		result = str(result)
		return result

	def prec2(self, result):
		result = round(result, 2)
		result = str(result)
		return result

	def prec3(self, result):
		result = round(result, 3)
		result = str(result)
		return result

	def prec4(self, result):
		result = round(result, 4)
		result = str(result)
		return result
	
        def for_loop(self, fname):
		mystr = ''
		for label, name in self.functionInputs[fname].iteritems():
		    mystr += '<p>{}</p><br>&nbsp<input type="text" name="{}" required autofocus><br>\n'.format(name, label)

		return mystr
		
        def show_Formulas(self, fname):
                mystr = ''
                for formula in self.formula_list[fname].values():
                    mystr += 'Formula:<br> {}'.format(formula)

                return mystr

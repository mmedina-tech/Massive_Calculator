#!/usr/bin/python
#SYNOPSIS: Culinary Formula Set 
#
# Culinary.py
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

class Culinary(FormulaBase):
    def __init__(self): 
        super(Culinary, self).__init__()
        
        self.function_list = OrderedDict(
            [
                #{{{___Function List _____________________________________________________________________________
                ('Cups to Liters', self.liters),
                ('Cups to Pints', self.pints),
                ('Dashes to Teaspoons', self.teaspoon),
                ('Fluid Ounces to Milliliters', self.milliliters3),
                ('Gallons to Liters', self.liters2),
                ('Gallons to Pecks', self.pecks),
                ('Grams to Ounces', self.form_grams),
                ('Grams to Pounds', self.pounds),
                ('Kilograms to Pounds', self.form_kilograms),
                ('Liters to Gallons', self.form_liters),
                ('Liters to Pints', self.form_liters2),
                ('Liters to Quarts', self.form_liters3),
                ('Pecks to Bushels', self.bushels),
                ('Pints to Liters', self.form_pints2),
                ('Pints to Quarts', self.quarts),
                ('Pounds to Kilograms', self.form_pounds),
                ('Portion Size', self.portion),
                ('Quarts to Gallons', self.gallons),
                ('Quarts to Liters', self.form_quarts),
                ('Tablespoons to Cups', self.cups),
                ('Tablespoons to Fluid Ounces', self.fl_ounce),
                ('Tablespoons to Milliliters', self.milliliters2),
                ('Teaspoons to Tablespoons', self.tablespoon),
                ('Teaspoons to Milliliters', self.milliliters),
                ('Unit Cost', self.unit),
                ('Recipe Cost', self.recipe),
                ('Selling Price', self.selling),
                #}}}_________________________________________________________________________________________
                
            ]
        )

        self.functionInputs = {
#{{{___ Inputs _____________________________________________________________________________
                
            'Portion Size':OrderedDict(
                [
                    ('number_input', 'Original Yield (input): '),
                    ('number_input2', 'Original Serving Size (input): '),
                    ('number_input3', 'Desired Portions (input): '),
                    ('number_input4', 'Desired Portion Size (input): '),
                    ('number_input5', 'Old Ingrediant Quantity (input): ')
                ]
            ),
            'Dashes to Teaspoons':{
                    'number_input' : 'Dashes (input): '
            },
            'Teaspoons to Tablespoons':{
                    'number_input' : 'Teaspoons (input): '
            },
            'Tablespoons to Fluid Ounces':{
                    'number_input' : 'Tablespoons (input): '
            },
            'Tablespoons to Cups':{
                    'number_input' : 'Tablespoons (input): '
            },
            'Cups to Pints':{
                    'number_input' : 'Cups (input): '
            },
            'Pints to Quarts':{
                    'number_input' : 'Pints (input): '
            },
            'Quarts to Gallons':{
                    'number_input' : 'Quarts (input): '
            },
            'Gallons to Pecks':{
                    'number_input' : 'Gallons (input): '
            },
            'Pecks to Bushels':{
                    'number_input' : 'Pecks (input): '
            },
            'Grams to Pounds':{
                    'number_input' : 'Grams (input): '
            },
            'Teaspoons to Milliliters':{
                    'number_input' : 'Teaspoons (input): '
            },
            'Tablespoons to Milliliters':{
                    'number_input' : 'Tablespoons (input): '
            },
            'Fluid Ounces to Milliliters':{
                    'number_input' : 'Fluid Ounces (input): '
            },
            'Cups to Liters':{
                    'number_input' : 'Cups (input): '
            },
            'Gallons to Liters':{
                    'number_input' : 'Gallons (input): '
            },
            'Pecks to Bushels':{
                    'number_input' : 'Bushels (input): '
            },
            'Grams to Pounds':{
                    'number_input' : 'Grams (input): '
            },
            'Teaspoons to Milliliters':{
                    'number_input' : 'Teaspoons (input): '
            },
            'Tablespoons to Milliliters':{
                    'number_input' : 'Tablespoons (input): '
            },
            'Fluid Ounces to Milliliters':{
                    'number_input' : 'Fluid Ounces (input): '
            },
            'Cups to Liters':{
                    'number_input' : 'Cups (input): '
            },
            'Gallons to Liters':{
                    'number_input' : 'Gallons (input): '
            },
            'Unit Cost':{
                    'number_input' : 'As Purchased Cost (input): ',
                    'number_input2' : 'Number of Units (input): '
            },
            'Recipe Cost': OrderedDict(
                    [
                            ('number_input', 'Total Recipe Cost (input): '),
                            ('number_input2', 'Number of Portions (input): ')
                    ]
            ),
            'Selling Price': OrderedDict(
                    [
                            ('number_input', 'Plate Cost (input): '),
                            ('number_input2', 'Food Cost Percentage (input): ')
                    ]
            ),
#}}}_________________________________________________________________________________________

        }

        self.formula_list = {
                #{{{___Formula List_____________________________________________________________________________
                
            'Cups to Liters':{
                '' : 'Cups * 0.24'
            },
            'Cups to Pints':{
                '' : 'Cups * 0.5'
            },
            'Dashes to Teaspoons':{
                '' : 'Dashes * 0.125'
            },
            'Fluid Ounces to Milliliters':{
                '' : 'Fluid Ounces * 28.35'
            },
            'Gallons to Liters':{
                '' : 'Gallons * 3.8'
            },
            'Gallons to Pecks':{
                '' : 'Gallons * 0.5'
            },
            'Grams to Ounces':{
                '' : 'Grams * 28.3495'
            },
            'Grams to Pounds':{
                '' : 'Grams * 0.0022'
            },
            'Kilograms to Pounds':{
                '' : 'Kilograms * 2.2046'
            },
            'Liters to Gallons':{
                '' : 'Liters * 0.2642'
            },
            'Liters to Pints':{
                '' : 'Liters * 2.1134'
            },
            'Liters to Quarts':{
                '' : 'Liters * 1.0567'
            },
            'Pecks to Bushels':{
                '': 'Pecks * 0.25'
            },
            'Pints to Liters':{
                '' : 'Pints * 1.4732'
            },
            'Pints to Quarts':{
                '' : 'Pints * 0.9463'
            },
            'Pounds to Kilograms':{
                '' : 'Pounds * 0.4536'
            },
            'Potion Size':{
                '' : '((Original Yield * Original Serving Size) / (Desired Portions * Desired Portion Size)) * Old Ingrediant Quantity'
            },
            'Quarts to Gallons':{
                '' : 'Quarts * 0.25'
            },
            'Quarts to Liters':{
                '' : 'Quarts * 0.5'
            },
            'Tablespoons to Cups':{
                '' : 'Tablespoons * 0.0625'
            },
            'Tablespoons to Fluid Ounces':{
                '' : 'Tablespoons * 0.5'
            },
            'Tablespoons to Milliliters':{
                '' : 'Tablespoons * 15'
            },
            'Teaspoons to Tablespoons':{
                '' : 'Teaspoons * 0.333333'
            },
            'Teaspoons to Milliliters':{
                '' : 'Teaspoons * 5'
            },
            'Unit Cost':{
                '' : 'As Purchased Cost / Number Of Units'
            },
            'Recipe Cost':{
                '' : 'Total Recipe Cost / Number of Portions'
            },
            'Selling Price':{
                '' : 'Plate Cost / (Food Cost Percentage / 100)'
            },
            #}}}_________________________________________________________________________________________
        }

#{{{___Formula Functions _____________________________________________________________________________

    def portion (self, num, num2, num3, num4, num5):
            old_yield = float(num) * float(num2)
            new_yield = float(num3) * float(num4)
            conversion_factor = new_yield / old_yield
            result = float(num5) * conversion_factor
            return (self.prec(result), self.pluralize(result, 'New Quantity')) 

    def teaspoon (self, num):
            result = float(num) * .125
            return (self.prec(result), self.pluralize(result, 'Teaspoon'))

    def tablespoon (self, num):
            result = float(num) * .333333
            return (self.prec(result), self.pluralize(result, 'Tablespoon'))

    def fl_ounce (self, num):
            result = float(num) * .5
            return (self.prec(result), self.pluralize(result, 'Fluid Ounce')) 

    def cups (self, num):
            result = float(num) * .0625
            return (self.prec(result), self.pluralize(result, 'Cup'))

    def pints (self, num):
            result = float(num) * .5
            return (self.prec(result), self.pluralize(result, 'Pint')) 

    def quarts (self, num):
            result = float(num) * .5
            return (self.prec(result), self.pluralize(result, 'Quart')) 
            
    def gallons (self, num):
            result = float(num) * .25
            return (self.prec(result), self.pluralize(result, 'Gallon')) 

    def pecks (self, num):
            result = float(num) * .5
            return (self.prec(result), self.pluralize(result, 'Peck'))
    
    def bushels (self, num):
            result = float(num) * .25
            return (self.prec(result), self.pluralize(result, 'Bushel')) 

    def pounds (self, num):
            result = float(num) * .0022
            return (self.prec(result), self.pluralize(result, 'Pound')) 

    def milliliters (self, num):
            result = float(num) * 5
            return (self.prec(result), self.pluralize(result, 'Milliliter')) 

    def milliliters2 (self, num): 
            result = float(num) * 15
            return (self.prec(result), self.pluralize(result, 'Milliliter')) 

    def milliliters3 (self, num):
            result = float(num) * 28.35
            return (self.prec(result), self.pluralize(result, 'Milliliter')) 

    def liters (self, num):
            result = float(num) * .24
            return (self.prec(result), self.pluralize(result, 'Liter')) 

    def liters2 (self, num):
            result = float(num) * 3.8
            return (self.prec(result), self.pluralize(result, 'Liter')) 

    def form_grams(self, num):
#		argsOut = ['Grams to Ounces', 'Enter Grams']
#		argsIn = self.prompt(argsOut)
            result = float(num) * 28.3495
            return (self.prec(result), self.pluralize(result, 'Ounce'))

    def form_kilograms(self, num):
#		argsOut = ['Kilograms to Pounds', 'Enter Kilograms']
#		argsIn = self.prompt(argsOut)
            result = float(num) * 2.2046
            return (self.prec(result), self.pluralize(result, 'Pound'))
            
    def form_liters(self, num):
#		argsOut = ['Liters to Gallons', 'Enter Liters']
#		argsIn = self.prompt(argsOut)
            result = float(num) * .2642
            return (self.prec(result), self.pluralize(result, 'Gallon'))
            
    def form_liters2(self, num):
#		argsOut = ['Liters to Pints', 'Enter Liters']
#		argsIn = self.prompt(argsOut)
            result = float(num) * 2.1134
            return (self.prec(result), self.pluralize(result, 'Pint'))
            
    def form_liters3(self, num):
#		argsOut = ['Liters to Quarts', 'Enter Liters']
#		argsIn = self.prompt(argsOut)
            result = float(num) * 1.0567
            return (self.prec(result), self.pluralize(result, 'Quart'))

    def form_ounces(self, num):
#		argsOut = ['Ounces to Grams', 'Enter Ounces']
#		argsIn = self.prompt(argsOut)
            result = float(num) * 28.3495
            return (self.prec(result), self.pluralize(result, 'Gram'))
            
    def form_pounds(self, num):
#		argsOut = ['Pounds to Kilograms', 'Enter Pounds']
#		argsIn = self.prompt(argsOut)
            result = float(num) * .4536
            return (self.prec(result), self.pluralize(result, 'Kilogram'))
            
    def form_pints2(self, num):
#		argsOut = ['Pfloats to Liters', 'Enter Pfloats']
#		argsIn = self.prompt(argsOut)
            result = float(num) * 1.4732
            return (self.prec(result), self.pluralize(result, 'Liter'))
            
    def form_quarts(self, num):
#		argsOut = ['Quarts to Liters', 'Enter Quarts']
#		argsIn = self.prompt(argsOut)
            result = float(num) * .9463
            return (self.prec(result), self.pluralize(result, 'Liter'))
    
    def unit (self, num, num2):
            result = float(num) / float(num2)
            return (self.prec(result), self.pluralize(result, 'Cost per Unit')) 

    def recipe (self, num, num2):
            result = float(num) / float(num2)
            return (round(result, 2), self.pluralize(result, 'Cost Per Portion')) 
    def selling (self, num, num2):
            result = float(num) / (float(num2) / 100)
            return (round(result, 2), self.pluralize(result, 'Selling Price')) 
#}}}_________________________________________________________________________________________


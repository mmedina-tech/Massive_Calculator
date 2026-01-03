#!/usr/bin/env python3
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


from .FormulaBase import * 

class Culinary(FormulaBase):
    def __init__(self, name): 
        super(Culinary, self).__init__(name)
        self.name = name
        
#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : "Cups to Liters",
            2 : "Cups to Pints",
            3 : "Dashes to Teaspoons",
            4 : "Fluid Ounces to Milliliters",
            5 : "Gallons to Liters",
            6 : "Gallons to Pecks",
            7 : "Grams to Ounces",
            8 : "Grams to Pounds",
            9 : "Kilograms to Pounds",
            10 : "Liters to Gallons",
            11 : "Liters to Pints",
            12 : "Liters to Quarts",
            13 : "Pecks to Bushels",
            14 : "Pints to Liters",
            15 : "Pints to Quarts",
            16 : "Pounds to Kilograms",
            17 : "Portion Size",
            18 : "Quarts to Gallons",
            19 : "Quarts to Liters",
            20 : "Tablespoons to Cups",
            21 : "Tablespoons to Fluid Ounces",
            22 : "Tablespoons to Milliliters",
            23 : "Teaspoons to Tablespoons",
            24 : "Teaspoons to Milliliters",
            25 : "Unit Cost",
            26 : "Recipe Cost",
            27 : "Selling Price",
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________
        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.liters),
                (self.function_strings[2], self.pints),
                (self.function_strings[3], self.teaspoon),
                (self.function_strings[4], self.milliliters3),
                (self.function_strings[5], self.liters2),
                (self.function_strings[6], self.pecks),
                (self.function_strings[7], self.form_grams),
                (self.function_strings[8], self.pounds),
                (self.function_strings[9], self.form_kilograms),
                (self.function_strings[10], self.form_liters),
                (self.function_strings[11], self.form_liters2),
                (self.function_strings[12], self.form_liters3),
                (self.function_strings[13], self.bushels),
                (self.function_strings[14], self.form_pints2),
                (self.function_strings[15], self.quarts),
                (self.function_strings[16], self.form_pounds),
                (self.function_strings[17], self.portion),
                (self.function_strings[18], self.gallons),
                (self.function_strings[19], self.form_quarts),
                (self.function_strings[20], self.cups),
                (self.function_strings[21], self.fl_ounce),
                (self.function_strings[22], self.milliliters2),
                (self.function_strings[23], self.tablespoon),
                (self.function_strings[24], self.milliliters),
                (self.function_strings[25], self.unit),
                (self.function_strings[26], self.recipe),
                (self.function_strings[27], self.selling),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
                
            self.function_strings[17]:OrderedDict(
                [
                    ("number_input", "Original Yield (input): "),
                    ("number_input2", "Original Serving Size (input): "),
                    ("number_input3", "Desired Portions (input): "),
                    ("number_input4", "Desired Portion Size (input): "),
                    ("number_input5", "Old Ingrediant Quantity (input): ")
                ]
            ),
            self.function_strings[3]:{
                    "number_input" : "Dashes (input): "
            },
            self.function_strings[23]:{
                    "number_input" : "Teaspoons (input): "
            },
            self.function_strings[21]:{
                    "number_input" : "Tablespoons (input): "
            },
            self.function_strings[20]:{
                    "number_input" : "Tablespoons (input): "
            },
            self.function_strings[2]:{
                    "number_input" : "Cups (input): "
            },
            self.function_strings[15]:{
                    "number_input" : "Pints (input): "
            },
            self.function_strings[18]:{
                    "number_input" : "Quarts (input): "
            },
            self.function_strings[6]:{
                    "number_input" : "Gallons (input): "
            },
            self.function_strings[13]:{
                    "number_input" : "Pecks (input): "
            },
            self.function_strings[7]:{
                    "number_input" : "Grams (input): "
            },
            self.function_strings[24]:{
                    "number_input" : "Teaspoons (input): "
            },
            self.function_strings[22]:{
                    "number_input" : "Tablespoons (input): "
            },
            self.function_strings[4]:{
                    "number_input" : "Fluid Ounces (input): "
            },
            self.function_strings[1]:{
                    "number_input" : "Cups (input): "
            },
            self.function_strings[5]:{
                    "number_input" : "Gallons (input): "
            },
            self.function_strings[13]:{
                    "number_input" : "Bushels (input): "
            },
            self.function_strings[8]:{
                    "number_input" : "Grams (input): "
            },
            self.function_strings[24]:{
                    "number_input" : "Teaspoons (input): "
            },
            self.function_strings[22]:{
                    "number_input" : "Tablespoons (input): "
            },
            self.function_strings[4]:{
                    "number_input" : "Fluid Ounces (input): "
            },
            self.function_strings[1]:{
                    "number_input" : "Cups (input): "
            },
            self.function_strings[5]:{
                    "number_input" : "Gallons (input): "
            },
            self.function_strings[25]:OrderedDict(
                [
                    ("number_input" , "As Purchased Cost (input): "),
                    ("number_input2" , "Number of Units (input): ")
                ]
            ),
            self.function_strings[26]: OrderedDict(
                [
                    ("number_input", "Total Recipe Cost (input): "),
                    ("number_input2", "Number of Portions (input): ")
                ]
            ),
            self.function_strings[27]: OrderedDict(
                [
                    ("number_input", "Plate Cost (input): "),
                    ("number_input2", "Food Cost Percentage (input): ")
                ]
            ),
            self.function_strings[9]:{
                    "number_input" : "Kilograms (input): "
            },
            self.function_strings[10]:{
                    "number_input" : "Liters (input): "
            },
            self.function_strings[11]:{
                    "number_input" : "Liters (input): "
            },
            self.function_strings[12]:{
                    "number_input" : "Liters (input): "
            },
            self.function_strings[14]:{
                    "number_input" : "Pints (input): "
            },
            self.function_strings[16]:{
                    "number_input" : "Pounds (input): "
            },
            self.function_strings[19]:{
                    "number_input" : "Quarts (input): "
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List_____________________________________________________________________________
        self.formula_list = {
                
            self.function_strings[1]:{
                "" : "Cups * 0.24"
            },
            self.function_strings[2]:{
                "" : "Cups * 0.5"
            },
            self.function_strings[3]:{
                "" : "Dashes * 0.125"
            },
            self.function_strings[4]:{
                "" : "Fluid Ounces * 28.35"
            },
            self.function_strings[5]:{
                "" : "Gallons * 3.8"
            },
            self.function_strings[6]:{
                "" : "Gallons * 0.5"
            },
            self.function_strings[7]:{
                "" : "Grams * 28.3495"
            },
            self.function_strings[8]:{
                "" : "Grams * 0.0022"
            },
            self.function_strings[9]:{
                "" : "Kilograms * 2.2046"
            },
            self.function_strings[10]:{
                "" : "Liters * 0.2642"
            },
            self.function_strings[11]:{
                "" : "Liters * 2.1134"
            },
            self.function_strings[12]:{
                "" : "Liters * 1.0567"
            },
            self.function_strings[13]:{
                "": "Pecks * 0.25"
            },
            self.function_strings[14]:{
                "" : "Pints * 1.4732"
            },
            self.function_strings[15]:{
                "" : "Pints * 0.9463"
            },
            self.function_strings[16]:{
                "" : "Pounds * 0.4536"
            },
            self.function_strings[17]:{
                "" : "((Original Yield * Original Serving Size) / (Desired Portions * Desired Portion Size)) * Old Ingrediant Quantity"
            },
            self.function_strings[18]:{
                "" : "Quarts * 0.25"
            },
            self.function_strings[19]:{
                "" : "Quarts * 0.5"
            },
            self.function_strings[20]:{
                "" : "Tablespoons * 0.0625"
            },
            self.function_strings[21]:{
                "" : "Tablespoons * 0.5"
            },
            self.function_strings[22]:{
                "" : "Tablespoons * 15"
            },
            self.function_strings[23]:{
                "" : "Teaspoons * 0.333333"
            },
            self.function_strings[24]:{
                "" : "Teaspoons * 5"
            },
            self.function_strings[25]:{
                "" : "As Purchased Cost / Number Of Units"
            },
            self.function_strings[26]:{
                "" : "Total Recipe Cost / Number of Portions"
            },
            self.function_strings[27]:{
                "" : "Plate Cost / (Food Cost Percentage / 100)"
            },
        }
#}}}_________________________________________________________________________________________

#{{{___Formula Functions _____________________________________________________________________________

    def portion (self):
        title = "Portion Size"
        old_yield = "Enter Old Yield"
        orig_size = "Enter Original Serving Size"
        des_port = "Enter Desired Portions"
        des_size = "Enter Desired Portion Size"
        old_quantity = "Enter Old Ingrediant Quantity"
        argsOut = [title, old_yield, orig_size, des_port, des_size, old_quantity]
        argsIn = self.prompt(argsOut)
        old_yield = argsIn[0] * argsIn[1]
        new_yield = argsIn[2] * argsIn[3]
        conversion_factor = new_yield / old_yield
        result = argsIn[4] * conversion_factor
        return (result, self.pluralize(result, 'New Quantity')) 

    def teaspoon (self):
        title = "Dashes to Teaspoons"
        dash = "Enter Dashes"
        argsOut = [title, dash]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .125
        return (result, self.pluralize(result, 'Teaspoon'))

    def tablespoon (self):
        title = "Teaspoons to Tablespoons"
        tea = "Enter Teaspoons"
        argsOut = [title, tea]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .333333
        return (result, self.pluralize(result, 'Tablespoon'))

    def fl_ounce (self):
        title = 'Tablespoons to Fluid Ounces'
        table = "Enter Tablespoons"
        argsOut = [title, table]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .5
        return (result, self.pluralize(result, 'Fluid Ounce')) 

    def cups (self):
        title = "Tablespoons to Cups"
        table = "Enter Tablespoons"
        argsOut = [title, table]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0625
        return (result, self.pluralize(result, 'Cup'))

    def pints (self):
        title = "Cups to Pints"
        cup = "Enter Cups"
        argsOut = [title, cup]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .5
        return (result, self.pluralize(result, 'Pint')) 

    def quarts (self):
        title = 'Pints to Quarts'
        pint = "Enter Pints"
        argsOut = [title, pint]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .5
        return (result, self.pluralize(result, 'Quart')) 
            
    def gallons (self):
        title = "Quarts to Galloons"
        quart = "Enter Quarts"
        argsOut = [title, quart]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .25
        return (result, self.pluralize(result, 'Gallon')) 

    def pecks (self):
        title = "Gallons to Pecks"
        gal = "Enter Gallons"
        argsOut = [title, gal]
        argsIn = self.prompt(argsOut)
        result = argsIn[0]* .5
        return (result, self.pluralize(result, 'Peck'))
    
    def bushels (self):
        title = 'Pecks to Bushels'
        peck = 'Enter Pecks'
        argsOut = [title, peck]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .25
        return (result, self.pluralize(result, 'Bushel')) 

    def pounds (self):
        title = 'Grams to Pounds'
        gram = "Enter Grams"
        argsOut = [title, gram]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .0022
        return (result, self.pluralize(result, 'Pound')) 

    def milliliters (self):
        title = "Teaspoons to Milliliters"
        tea = "Enter Teaspoons"
        argsOut = [title, tea]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 5
        return (result, self.pluralize(result, 'Milliliter')) 

    def milliliters2 (self): 
        title = "Tablespoons to Milliliters"
        table = "Enter Tablespoons"
        argsOut = [title, table]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 15
        return (result, self.pluralize(result, 'Milliliter')) 

    def milliliters3 (self):
        title = 'Fluid Ounces to Milliliters'
        flo = "Enter Fluid Ounces"
        argsOut = [title, flo]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 28.35
        return (result, self.pluralize(result, 'Milliliter')) 

    def liters (self):
        title = "Cups to Liters"
        cup = "Enter Cups"
        argsOut = [title, cup]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .24
        return (result, self.pluralize(result, 'Liter')) 

    def liters2 (self):
        title = "Gallons to Liters"
        gal = "Enter Gallons"
        argsOut = [title, gal]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 3.8
        return (result, self.pluralize(result, 'Liter')) 

    def form_grams(self):
        argsOut = ['Grams to Ounces', 'Enter Grams']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 28.3495
        return (result, self.pluralize(result, 'Ounce'))

    def form_kilograms(self):
        argsOut = ['Kilograms to Pounds', 'Enter Kilograms']
        argsIn = self.prompt(argsOut)
        result =  argsIn[0] * 2.2046
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
            
    def form_pints2(self):
        argsOut = ['Pfloats to Liters', 'Enter Pfloats']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.4732
        return (result, self.pluralize(result, 'Liter'))
            
    def form_quarts(self):
        argsOut = ['Quarts to Liters', 'Enter Quarts']
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .9463
        return (result, self.pluralize(result, 'Liter'))
    
    def unit (self):
        title = 'Unit Cost'
        units = "Enter Number of Units"
        purch = "Enter Purchased Cost"
        argsOut [title, units, purch]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (money(result), self.pluralize(result, 'Cost per Unit')) 

    def recipe (self):
        title = 'Recipe Cost'
        total = 'Enter Total Recipe Cost'
        port = 'Enter Number of Portions'
        argsOut = [title, total, port]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (money(result), self.pluralize(result, 'Cost Per Portion')) 

    def selling (self):
        title = 'Selling Price'
        plate = 'Enter Plate Cost'
        cost_perc = "Enter Food Cost Percent"
        argsOut = [title, plate, cost_perc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / (argsIn[1] / 100)
        return (money(result), self.pluralize(result, 'Selling Price')) 
#}}}_________________________________________________________________________________________


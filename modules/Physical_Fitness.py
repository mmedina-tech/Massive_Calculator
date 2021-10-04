#!/usr/bin/python
#
# Physical_Fitness.py
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

class Physical_Fitness(FormulaBase):
    def __init__(self, name): 
        super(Physical_Fitness, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Calories burned in Work-Out',
            2 : 'Calories to Joules',
            3 : 'Joules to Calories',
            4 : 'Newtons to Pounds',
            5 : 'Pounds to Newtons',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
            #    ('Body Mass Index', self.bmi),
                (self.function_strings[1], self.work),
                (self.function_strings[2], self.calories),
                (self.function_strings[3], self.joules),
                (self.function_strings[4], self.newtons),
                (self.function_strings[5], self.pounds),

            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1]: OrderedDict(
                [
                    ('number_input', 'Enter Weight: '),
                    ('number_input2', 'Enter Angle: '),
                    ('number_input3', 'Enter Distance of Lift: '),
                ]
            ),
       #     'Body Mass Index': OrderedDict(
        #        [
         #           ('number_input', 'Weight in pounds: '),
          #          ('number_input2' , 'Height in Inches: ')
           #     ]
            #),
            self.function_strings[4]:{
                    'number_input' : 'Newtons: '
            },
            self.function_strings[5]:{
                    'number_input' : 'Pounds: '
            },
            self.function_strings[3]:{
                    'number_input' : 'Joules: '
            },
            self.function_strings[2]:{
                    'number_input' : 'Calories: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{
                '' : '((Weight * 4.448) * cos(Angle) * (Distance or Lift * 3.2808)) * 0.239'
            },
            self.function_strings[2]:{
                '' : 'Calories * 4.186'
            },
            self.function_strings[3]:{
                '' : 'Joules * 0.239'
            },
            self.function_strings[4]:{
                '' : 'Newtons * 0.2248'
            },
            self.function_strings[5]:{
                '' : 'Pounds * 4.448'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    #def bmi (self, num, num2):
     #       result = (float(num) * 703) / float(num2)) / float(num2)
      #      return (result+'%', self.pluralize(result, 'Body Mass (estimated)'))

    def work (self):
        title = self.function_strings[1]
        weight = "Enter Weight"
        angle = "Enter Angle"
        lift = "Enter Distance of Lift"
        argsOut = [title, weight, angle, lift]
        argsIn = self.prompt(argsOut)
        result = (((argsIn[0] * 4.448) * cos(argsIn[1]) * (argsIn[2] * 3.2808))) * .239
        result = result * pow(10, -3)
        return (result, self.pluralize(result, 'Calorie')) 

    def calories (self):
        title = self.function_strings[2]
        cal = "Enter Calories"
        argsOut = [title, cal]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4.186
        return (result, self.pluralize(result, 'Joule')) 

    def joules (self):
        title = self.function_strings[3]
        joul = "Enter Joules"
        argsOut = [title, joul]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .239
        return (result, self.pluralize(result, 'Calorie')) 
    
    def newtons (self):
        title = self.function_strings[4]
        newt = "Enter Newtons"
        argsOut = [title, newt]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2248
        return (result, self.pluralize(result, 'Pound'))

    def pounds (self):
        title = self.function_strings[5]
        pound = "Enter Pounds"
        argsOut = [title, pound]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4.448
        return (result, self.pluralize(result, 'Newton')) 
#}}}_________________________________________________________________________________________


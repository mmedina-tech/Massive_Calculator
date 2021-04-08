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

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
            #    ('Body Mass Index', self.bmi),
                ('Calories burned in Work-Out', self.work),
                ('Calories to Joules', self.calories),
                ('Joules to Calories', self.joules),
                ('Newtons to Pounds', self.newtons),
                ('Pounds to Newtons', self.pounds),

            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            'Calories burned in Work-Out': OrderedDict(
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
            'Newtons to Pounds':{
                    'number_input' : 'Newtons: '
            },
            'Pounds to Newtons':{
                    'number_input' : 'Pounds: '
            },
            'Joules to Calories':{
                    'number_input' : 'Joules: '
            },
            'Calories to Joules':{
                    'number_input' : 'Calories: '
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Calories burned in Work-out':{
                '' : '((Weight * 4.448) * cos(Angle) * (Distance or Lift * 3.2808)) * 0.239'
            },
            'Calories to Joules':{
                '' : 'Calories * 4.186'
            },
            'Joules to Calories':{
                '' : 'Joules * 0.239'
            },
            'Newtons to Pounds':{
                '' : 'Newtons * 0.2248'
            },
            'Pounds to Newtons':{
                '' : 'Pounds * 4.448'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    #def bmi (self, num, num2):
     #       result = (float(num) * 703) / float(num2)) / float(num2)
      #      return (self.prec2(result)+'%', self.pluralize(result, 'Body Mass (estimated)'))

    def work (self):
        title = "Calories burned in Work-Out"
        weight = "Enter Weight"
        angle = "Enter Angle"
        lift = "Enter Distance of Lift"
        argsOut = [title, weight, angle, lift]
        argsIn = self.prompt(argsOut)
        result = (((argsIn[0] * 4.448) * cos(argsIn[1]) * (argsIn[2] * 3.2808))) * .239
        result = result * pow(10, -3)
        return (self.prec4(result), self.pluralize(result, 'Calorie')) 

    def calories (self):
        title = "Calories to Joules"
        cal = "Enter Calories"
        argsOut = [title, cal]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4.186
        return (self.prec4(result), self.pluralize(result, 'Joule')) 

    def joules (self):
        title = "Joules to Calories"
        joul = "Enter Joules"
        argsOut = [title, joul]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .239
        return (self.prec2(result), self.pluralize(result, 'Calorie')) 
    
    def newtons (self):
        title = "Newtons to Pounds"
        newt = "Enter Newtons"
        argsOut = [title, newt]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .2248
        return (self.prec2(result), self.pluralize(result, 'Pound'))

    def pounds (self):
        title = "Pounds to Newton"
        pound = "Enter Pounds"
        argsOut = [title, pound]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4.448
        return (self.prec2(result), self.pluralize(result, 'Newton')) 
#}}}_________________________________________________________________________________________


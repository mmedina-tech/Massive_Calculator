#!/usr/bin/python
#
# GED_Practice.py
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

class GED_Practice (FormulaBase):
    def __init__(self, name):
        super (GED_Practice, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________
        self.function_strings = {
            1 : 'Triangle',
            2 : 'Circle',
            3 : 'Rectangle',
            4 : 'Parallelogram',
            5 : 'Trapazoid',
            6 : 'Rectangular/Right Prism Surface Area',
            7 : 'Rectangular/Right Prism Volume',
            8 : 'Cylinder Surface Area',
            9 : 'Cylinder Volume',
            10 : 'Pyramid Surface Area',
            11 : 'Pyramid Volume',
            12 : 'Cone Surface Area',
            13 : 'Cone Volume',
            14 : 'Sphere Surface Area',
            15 : 'Sphere Volume',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
                [
                    (self.function_strings[1], self.tri),
                    (self.function_strings[2], self.circle),
                    (self.function_strings[3], self.rectangle),
                    (self.function_strings[4], self.para),
                    (self.function_strings[5], self.trap),
                    (self.function_strings[6], self.rect),
                    (self.function_strings[7], self.rect2),
                    (self.function_strings[8], self.cyl),
                    (self.function_strings[9], self.cyl2),
                    (self.function_strings[10], self.pyr),
                    (self.function_strings[11], self.pyr2),
                    (self.function_strings[12], self.cone),
                    (self.function_strings[13], self.cone2),
                    (self.function_strings[14], self.sphere),
                    (self.function_strings[15], self.sphere2),
                ]
            )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
                self.function_strings[1]: OrderedDict(
                    [
                        ( 'number_input', 'Base (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[2]: OrderedDict(
                    [
                        ( 'number_input', 'Radius (input): '),
                    ]
                ),
                self.function_strings[3]:OrderedDict(
                    [
                        ( 'number_input', 'Length (input): '),
                        ( 'number_input2', 'Width (input): '),
                    ]
                ),
                self.function_strings[4]:OrderedDict(
                    [
                        ( 'number_input', 'Base (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[5]:OrderedDict(
                    [
                        ( 'number_input', 'Height (input): '),
                        ( 'number_input2', 'Base 1 (input): '),
                        ( 'number_input3', 'Base 2 (input): '),
                    ]
                ),
                self.function_strings[6]: OrderedDict(
                    [
                        ('number_input', 'Perimeter of Base (input): '),
                        ('number_input2', 'Height (input): '),
                        ('number_input3', 'Area of Base (input): '),
                    ]
                ),
                self.function_strings[7]: OrderedDict(
                    [
                        ('number_input', 'Base (input): '),
                        ('number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[8]: OrderedDict(
                    [
                        ('number_input', 'Radius (input): '),
                        ('number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[9]: OrderedDict(
                    [
                        ('number_input', 'Radius (input): '),
                        ('number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[10]: OrderedDict(
                    [
                        ('number_input', 'Perimeter of Base (input): '),
                        ('number_input2', 'Slant Length (input): '),
                        ('number_input3', 'Area of Base (input): '),
                    ]
                ),
                self.function_strings[11]: OrderedDict(
                    [
                        ( 'number_input', 'Base (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[12]: OrderedDict(
                    [
                        ( 'number_input', 'Radius (input): '),
                        ( 'number_input2', 'Slant Length (input): '),
                    ]
                ),
                self.function_strings[13]: OrderedDict(
                    [
                        ( 'number_input', 'Radius (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                self.function_strings[14]: OrderedDict(
                        [
                            ( 'number_input', 'Radius (input): '),
                        ]
                    ),
                self.function_strings[15]: OrderedDict(
                        [
                            ( 'number_input', 'Radius (input): '),
                        ]
                    ),
            }
            #}}}

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{
                '' : '(0.5 * Base) * Height'
            },
            self.function_strings[2]:{
                '' : '3.14 * (Radius<sup>2</sup>)'
            },
            self.function_strings[3]:{
                '' : 'Length * Width'
            },
            self.function_strings[4]:{
                '' : 'Base * Height'
            },
            self.function_strings[5]:{
                '' : '0.5 * Height * (Base 1 + Base 2)'
            },
            self.function_strings[6]:{
                '' : 'Perimeter of Base * Height + (2 * Area of Base)'
            },
            self.function_strings[7]:{
                '' : 'Base * Height'
            },
            self.function_strings[8]:{
                '' : '(2 * 3.14 * Radius * Height) + (2 * 3.14 * Height<sup>2</sup>)'
            },
            self.function_strings[9]:{
                '' : '3.14 * Radius<sup>2</sup> * Height'
            },
            'Pyramid Surface Volume':{
                '' : '0.5 * Perimeter of Base * Slant Length + Area of Base'
            },
            self.function_strings[10]:{
                '' : '0.5 * Perimeter of Base * Slant Length + Area Of Base'
            },
            self.function_strings[11]:{
                '' : '0.33333333333 * Base * Height'
            },
            self.function_strings[12]:{
                '' : '(3.14 * Radius * Slant Length) + (3.14 * Slant Length)'
            },
            self.function_strings[13]:{
                '' : '0.33333333333 * Radius<sup>2</sup> * Height'
            },
            self.function_strings[14]:{
                '' : '4 * 3.14 * Radius'
            },
            self.function_strings[15]:{
                '' : '1.333333333 * 3.14 * Radius'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def rect(self):
        title = self.function_strings[6]
        rect = "Enter Perimeter of Base"
        height = "Enter Height"
        area = "Enter Area Base"
        argsOut = [title, rect, height, area]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1] + (2*argsIn[2])
        return (result, self.pluralize(result, 'Surface Area'))

    def rect2(self):
        title = self.function_strings[7]
        rect = "Enter Base"
        height = "Enter Height"
        argsOut = [title, rect, height]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (result, self.pluralize(result, 'Rectange / Right Prism Volume'))

    def cyl(self):
        title = self.function_strings[8]
        cyl = "Enter Radius"
        height = "Enter Height"
        argsOut = [title, cyl, height]
        argsIn = self.prompt(argsOut)
        result = (2*3.14*argsIn[0]*argsIn[1])+(2*3.14*(argsIn[1]**2))
        return (result, self.pluralize(result, 'Cylinder Surface Area'))

    def cyl2(self):
        title = self.function_strings[9]
        radius = "Enter Radius"
        height = "Enter Height"
        argsOut = [title, radius, height]
        argsIn = self.prompt(argsOut)
        result = 3.14*(argsIn[0]**2)*argsIn[1]
        return (result, self.pluralize(result, 'Cylinder Volume'))

    def pyr(self):
        title = self.function_strings[10]
        perm = "Enter Perimeter of Base"
        slant = "Enter Slant Length"
        base = "Enter Area of Base"
        argsOut = [title, perm, slant, base]
        argsIn = self.prompt(argsOut)
        result = 0.5*argsIn[0]*argsIn[1]+argsIn[2]
        return (result, self.pluralize(result, 'Pyramid Surface Area'))

    def pyr2(self):
        title = self.function_strings[11]
        base = "Enter Base"
        height = "Enter Height"
        argsOut = [title, base, height]
        argsIn = self.prompt(argsOut)
        result = (.33333333333*argsIn[0]*argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Pyramid Volume'))

    def cone(self):
        title = self.function_strings[12]
        radius = "Enter Radius"
        slant = 'Enter Slant'
        argsOut = [title, radius, slant]
        argsIn = self.prompt(argsOut)
        result = (3.14*argsIn[0]*argsIn[1])+(3.14*argsIn[1])
        return (result, self.pluralize(result, 'Cone Surface Area'))

    def cone2(self):
        title = self.function_strings[13]
        radius = "Enter Radius"
        height = "Enter Height"
        argsOut = [title, radius, height]
        argsIn = self.prompt(argsOut)
        result = .333333333333333333*(argsIn[0]**2)*argsIn[1]
        return (result, self.pluralize(result, 'Cone Volume'))

    def sphere(self):
        title = self.function_strings[14]
        radius = "Enter Radius"
        argsOut = [title, radius]
        argsIn = self.prompt(argsOut)
        result = 4*3.14*argsIn[0]
        return (result, self.pluralize(result, 'Sphere Surface Area'))

    def sphere2(self, num):
        title = self.function_strings[15]
        radius = "Enter Radius"
        argsOut = [title, radius]
        argsIn = self.prompt(argsOut)
        result = 1.333333333*3.14*argsIn[0]
        return (result, self.pluralize(result, 'Sphere Volume'))

    def tri(self):
        title = self.function_strings[1]
        base = "Enter Base"
        height = "Enter Height"
        argsOut = [title, base, height]
        argsIn = self.prompt(argsOut)
        result = (0.5*argsIn[0]*argsIn[1])
        return (result, self.pluralize(result, 'Triangle Area'))

    def circle(self):
        title = self.function_strings[2]
        radius = "Enter Radius"
        argsOut = [title, radius]
        argsIn = self.prompt(argsOut)
        result = 3.14 * (argsIn[0]**2)
        return (result, self.pluralize(result, 'Circle Area'))

    def rectangle(self):
        title = self.function_strings[3]
        length = "Enter Length"
        width = "Enter Width"
        argsOut = [title, length, width]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (result, self.pluralize(result, 'Rectangle Area'))

    def para(self):
        title = self.function_strings[4]
        base = "Enter Base"
        height = "Enter Height"
        argsOut = [title, base, height]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (result, self.pluralize(result, 'Parallelogram Area'))

    def trap(self):
        title = self.function_strings[5]
        height = "Enter Height"
        base1 = "Enter Base 1"
        base2 = "Enter Base 2"
        argsOut = [title, height, base1, base2]
        argsIn = self.prompt(argsOut)
        result = 0.5*argsIn[0]*(argsIn[1]+argsIn[2])
        return (result, self.pluralize(result, 'Trapezoid Area'))
#}}}_________________________________________________________________________________________


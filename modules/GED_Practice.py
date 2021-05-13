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

#{{{___ Function List _____________________________________________________________________________

        self.function_list = {
            'Triangle': self.tri,
            'Circle': self.circle,
            'Rectangle': self.rectangle,
            'Parallelogram': self.para,
            'Trapazoid': self.trap,
            'Rectangular/Right Prism Surface Area': self.rect,
            'Rectangular/Right Prism Volume': self.rect2,
            'Cylinder Surface Area': self.cyl,
            'Cylinder Volume': self.cyl2,
            'Pyramid Surface Area': self.pyr,
            'Pyramid Volume': self.pyr2,
            'Cone Surface Area': self.cone,
            'Cone Volume': self.cone2,
            'Sphere Surface Area': self.sphere,
            'Sphere Volume': self.sphere2,
        }
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________
        self.functionInputs = {
                'Triangle': OrderedDict(
                    [
                        ( 'number_input', 'Base (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                'Circle': OrderedDict(
                    [
                        ( 'number_input', 'Radius (input): '),
                    ]
                ),
                'Rectangle':OrderedDict(
                    [
                        ( 'number_input', 'Length (input): '),
                        ( 'number_input2', 'Width (input): '),
                    ]
                ),
                'Parallelogram':OrderedDict(
                    [
                        ( 'number_input', 'Base (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                'Trapazoid':OrderedDict(
                    [
                        ( 'number_input', 'Height (input): '),
                        ( 'number_input2', 'Base 1 (input): '),
                        ( 'number_input3', 'Base 2 (input): '),
                    ]
                ),
                'Rectangular/Right Prism Surface Area': OrderedDict(
                    [
                        ('number_input', 'Perimeter of Base (input): '),
                        ('number_input2', 'Height (input): '),
                        ('number_input3', 'Area of Base (input): '),
                    ]
                ),
                'Rectangular/Right Prism Volume': OrderedDict(
                    [
                        ('number_input', 'Base (input): '),
                        ('number_input2', 'Height (input): '),
                    ]
                ),
                'Cylinder Surface Area': OrderedDict(
                    [
                        ('number_input', 'Radius (input): '),
                        ('number_input2', 'Height (input): '),
                    ]
                ),
                'Cylinder Volume': OrderedDict(
                    [
                        ('number_input', 'Radius (input): '),
                        ('number_input2', 'Height (input): '),
                    ]
                ),
                'Pyramid Surface Area': OrderedDict(
                    [
                        ('number_input', 'Perimeter of Base (input): '),
                        ('number_input2', 'Slant Length (input): '),
                        ('number_input3', 'Area of Base (input): '),
                    ]
                ),
                'Pyramid Volume': OrderedDict(
                    [
                        ( 'number_input', 'Base (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                'Cone Surface Area': OrderedDict(
                    [
                        ( 'number_input', 'Radius (input): '),
                        ( 'number_input2', 'Slant Length (input): '),
                    ]
                ),
                'Cone Volume': OrderedDict(
                    [
                        ( 'number_input', 'Radius (input): '),
                        ( 'number_input2', 'Height (input): '),
                    ]
                ),
                'Sphere Surface Area': OrderedDict(
                        [
                            ( 'number_input', 'Radius (input): '),
                        ]
                    ),
                'Sphere Volume': OrderedDict(
                        [
                            ( 'number_input', 'Radius (input): '),
                        ]
                    ),
            }
            #}}}

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Triangle Area':{
                '' : '(0.5 * Base) * Height'
            },
            'Circle Area':{
                '' : '3.14 * (Radius<sup>2</sup>)'
            },
            'Rectangle Area':{
                '' : 'Length * Width'
            },
            'Parallelogram Area':{
                '' : 'Base * Height'
            },
            'Trapazoid Area':{
                '' : '0.5 * Height * (Base 1 + Base 2)'
            },
            'Rectangular/Right Prism Surface Area':{
                '' : 'Perimeter of Base * Height + (2 * Area of Base)'
            },
            'Rectangular/Right Prism Volume':{
                '' : 'Base * Height'
            },
            'Cylinder Surface Area':{
                '' : '(2 * 3.14 * Radius * Height) + (2 * 3.14 * Height<sup>2</sup>)'
            },
            'Cylinder Volume':{
                '' : '3.14 * Radius<sup>2</sup> * Height'
            },
            'Pyramid Surface Volume':{
                '' : '0.5 * Perimeter of Base * Slant Length + Area of Base'
            },
            'Pyramid Volume':{
                '' : '0.33333333333 * Base * Height'
            },
            'Cone Surface Area':{
                '' : '(3.14 * Radius * Slant Length) + (3.14 * Slant Length)'
            },
            'Cone Volume':{
                '' : '0.33333333333 * Radius<sup>2</sup> * Height'
            },
            'Sphere Surface Area':{
                '' : '4 * 3.14 * Radius'
            },
            'Shpere Volume':{
                '' : '1.333333333 * 3.14 * Radius'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def rect(self):
        title = "Rectangle/Right Prism Surface Area"
        rect = "Enter Perimeter of Base"
        height = "Enter Height"
        area = "Enter Area Base"
        argsOut = [title, rect, height, area]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1] + (2*argsIn[2])
        return (self.prec(result), self.pluralize(result, 'Surface Area'))

    def rect2(self):
        title = "Rectangular/Right Prism Volume"
        rect = "Enter Base"
        height = "Enter Height"
        argsOut = [title, rect, height]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec2(result), self.pluralize(result, 'Rectange / Right Prism Volume'))

    def cyl(self):
        title = "Cylinder Surface Area"
        cyl = "Enter Radius"
        height = "Enter Height"
        argsOut = [title, cyl, height]
        argsIn = self.prompt(argsOut)
        result = (2*3.14*argsIn[0]*argsIn[1])+(2*3.14*(argsIn[1]**2))
        return (self.prec(result), self.pluralize(result, 'Cylinder Surface Area'))

    def cyl2(self):
        title = "Cylinder Volume"
        radius = "Enter Radius"
        height = "Enter Height"
        argsOut = [title, radius, height]
        argsIn = self.prompt(argsOut)
        result = 3.14*(argsIn[0]**2)*argsIn[1]
        return (self.prec(result), self.pluralize(result, 'Cylinder Volume'))

    def pyr(self):
        title = "Pyramid Surface Area"
        perm = "Enter Perimeter of Base"
        slant = "Enter Slant Length"
        base = "Enter Area of Base"
        argsOut = [title, perm, slant, base]
        argsIn = self.prompt(argsOut)
        result = 0.5*argsIn[0]*argsIn[1]+argsIn[2]
        return (self.prec(result), self.pluralize(result, 'Pyramid Surface Area'))

    def pyr2(self):
        title = "Pyramid Volume"
        base = "Enter Base"
        height = "Enter Height"
        argsOut = [title, base, height]
        argsIn = self.prompt(argsOut)
        result = (.33333333333*argsIn[0]*argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Pyramid Volume'))

    def cone(self):
        title = "Cone Surface Area"
        radius = "Enter Radius"
        slant = 'Enter Slant'
        argsOut = [title, radius, slant]
        argsIn = self.prompt(argsOut)
        result = (3.14*argsIn[0]*argsIn[1])+(3.14*argsIn[1])
        return (self.prec(result), self.pluralize(result, 'Cone Surface Area'))

    def cone2(self):
        title = "Cone Volume"
        radius = "Enter Radius"
        height = "Enter Height"
        argsOut = [title, radius, height]
        argsIn = self.prompt(argsOut)
        result = .333333333333333333*(argsIn[0]**2)*argsIn[1]
        return (self.prec(result), self.pluralize(result, 'Cone Volume'))

    def sphere(self):
        title = "Sphere Surface Area"
        radius = "Enter Radius"
        argsOut = [title, radius]
        argsIn = self.prompt(argsOut)
        result = 4*3.14*argsIn[0]
        return (self.prec(result), self.pluralize(result, 'Sphere Surface Area'))

    def sphere2(self, num):
        title = "Sphere Volume"
        radius = "Enter Radius"
        argsOut = [title, radius]
        argsIn = self.prompt(argsOut)
        result = 1.333333333*3.14*argsIn[0]
        return (self.prec(result), self.pluralize(result, 'Sphere Volume'))

    def tri(self):
        title = "Triangle Area"
        base = "Enter Base"
        height = "Enter Height"
        argsOut = [title, base, height]
        argsIn = self.prompt(argsOut)
        result = (0.5*argsIn[0]*argsIn[1])
        return (self.prec4(result), self.pluralize(result, 'Triangle Area'))

    def circle(self):
        title = "Circle Area"
        radius = "Enter Radius"
        argsOut = [title, radius]
        argsIn = self.prompt(argsOut)
        result = 3.14 * (argsIn[0]**2)
        return (self.prec2(result), self.pluralize(result, 'Circle Area'))

    def rectangle(self):
        title = "Rectangle Area"
        length = "Enter Length"
        width = "Enter Width"
        argsOut = [title, length, width]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec2(result), self.pluralize(result, 'Rectangle Area'))

    def para(self):
        title = "Parallelogram Area"
        base = "Enter Base"
        height = "Enter Height"
        argsOut = [title, base, height]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * argsIn[1]
        return (self.prec2(result), self.pluralize(result, 'Parallelogram Area'))

    def trap(self):
        title = "Trapazoid Area"
        height = "Enter Height"
        base1 = "Enter Base 1"
        base2 = "Enter Base 2"
        argsOut = [title, height, base1, base2]
        argsIn = self.prompt(argsOut)
        result = 0.5*argsIn[0]*(argsIn[1]+argsIn[2])
        return (self.prec4(result), self.pluralize(result, 'Trapezoid Area'))
#}}}_________________________________________________________________________________________


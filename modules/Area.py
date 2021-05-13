#!/usr/bin/python
#SYNOPSIS: Area Formula Set
#
# Area.py
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
# This Module is for Area Formuals 


from FormulaBase import *  

class Area (FormulaBase):
    def __init__(self, name):
        super (Area, self).__init__(name)
        self.name = name

        self.function_list = {
#{{{
            'Acres to Hectares': self.acre,
            'Hectares to Acres': self.hect,
            'Square Inches to Square Feet': self.sqin,
            'Square Feet to Square Yards': self.sqft,
            'Square Feet to Square Rods': self.sqft2,
            'Square Rods to Acres': self.sqrd,
            'Acres to Square Miles': self.acre2,
            'Square Feet to Square Miles': self.sqft3,
            'Square Feet to Acres': self.sqft4,
            'Centiare to Square Inches': self.cent,
            'Are to Square Yard': self.are,
            'Square Kilometer to Acre': self.ska,
            'Square Link to Square Inch': self.link,
            'Square Link to Square Centimeter': self.link2,
            'Square Pole to Square Link': self.spole,
            'Square Pole to Square Yard': self.spole2,
            'Square Pole to Square Meter': self.spole3,
            'Square Chain to Square Pole': self.schain,
            'Square Chain to Square Yard': self.schain2,
            'Square Chain to Square Meter': self.schain3,
            'Acre to Square Chain': self.acre3,
            'Acre to Square Yard': self.acre4,
            'Acre to Square Meter': self.acre5,
            'Section to Acre': self.section,
            'Section to Square Mile': self.section2,
            'Section to Square Kilometer': self.section3,
            'Township to Section': self.town,
            'Township to Square Mile': self.town2,
            'Township to Square Kilometer': self.town3,
            'Square Inch to Centiare': self.sqin2,
            'Square Yard to Are': self.sqyrd,
            'Acre to Square Kilometer': self.acre6,
            'Square Kilometer to Square Mile': self.sqkm,
            'Square Centimeter to Square Inch': self.sqcm,
            'Square Inch to Square Link': self.sqin3,
            'Square Meter to Square Yard': self.sqm,
            'Square Yard to Square Link': self.sqyrd2,
            'Square Link to Square Pole': self.link3,
            'Square Yard to Square Pole': self.sqyrd3,
            'Square Pole to Square Chain': self.spole4,
            'Square Chain to Acre': self.schain4,
            'Acre to Section': self.acre7,
            'Section to Township': self.section4,
            'Acre to Square Feet': self.acre8,
        }
#}}}

        self.functionInputs = {
#{{{
            'Square Feet to Acres':{
                'number_input' : 'Square Feet (input): '
                },
            'Square Feet to Square Miles':{
                'number_input' : 'Square Feet (input): '
                },
            'Acres to Hectares':{
                'number_input' : 'Acres (input): '
                },
            'Hectares to Acres':{
                'number_input' : 'Hectares (input): '
                },
            'Square Inches to Square Feet':{
                'number_input' : 'Square Inches (input): '
                },
            'Square Feet to Square Yards':{
                'number_input' : 'Square Feet (input): '
                },
            'Square Feet to Square Rods':{
                'number_input' : 'Square Feet (input): '
                },
            'Square Rods to Acres':{
                'number_input' : 'Square Rods (input): '
                },
            'Acres to Square Miles':{
                'number_input' : 'Acres (input): '
                },
            'Centiare to Square Inches':{
                'number_input' : 'Centiare (input): '
                },
            'Square Inch to Centiare':{
                'number_input' : 'Square Inch (input): '
                },
            'Are to Square Yard':{
                'number_input' : 'Are (input): '
                },
            'Are to Centiare':{
                'number_input' : 'Are (input): '
                },
            'Square Yard to Are':{
                'number_input' : 'Square Yard (input): '
                },
            'Centiare to Are':{
                'number_input' : 'Centiare (input): '
                },
            'Hectare to Are':{
                'number_input' : 'Hectare (input): '
                },
            'Hectare to Acres':{
                'number_input' : 'Hectare (input): '
                },
            'Acre to Are':{
                'number_input' : 'Acre (input): '
                },
            'Are to Hectare':{
                'number_input' : 'Are (input): '
                },
            'Square Kilometer to Hectare':{
                'number_input' : 'Square Kilometer (input): '
                },
            'Square Kilometer to Acre':{
                'number_input' : 'Square Kilometer (input): '
                },
            'Square Kilometer to Square Mile':{
                'number_input' : 'Square Kilometers (input): '
                },
            'Square Mile to Square Kilometer':{
                    'number_input' : 'Square Mile (input): '
                    },
            'Acre to Square Kilometer':{
                    'number_input' : 'Acre (input): '
                    },
            'Hectare to Square Kilometer':{
                    'number_input' : 'Hectare (input): '
                    },
            'Square Link to Square Inch':{
                'number_input' : 'Square Link (input): '
                },
            'Square Link to Square Centimeter':{
                'number_input' : 'Square Link (input): '
                },
            'Square Centimeter to Square Link':{
                    'number_input' : 'Square Centimeter (input): '
                    },
            'Square Inch to Square Link':{
                    'number_input' : 'Square Inch (input): '
                    },
            'Square Meter to Square Pole':{
                    'number_input' : 'Square Meter (input): '
                    },
            'Square Yard to Square Pole':{
                    'number_input' : 'Square Yard (input): '
                    },
            'Square Link to Square Pole':{
                    'number_input' : 'Square Link (input): '
                    },
            'Square Pole to Square Link':{
                'number_input' : 'Square Pole (input): '
                },
            'Square Pole to Square Yard':{
                'number_input' : 'Square Pole (input): '
                },
            'Square Pole to Square Meter':{
                'number_input' : 'Square Pole (input): '
                },
            'Square Chain to Square Pole':{
                'number_input' : 'Square Chain (input): '
                },
            'Square Chain to Square Yard':{
                    'number_input' : 'Square Chain (input): '
                    },
            'Square Chain to Square Meter':{
                    'number_input' : 'Square Chain (input): '
                    },
            'Square Meter to Square Chain':{
                    'number_input' : 'Square Meter (input): '
                    },
            'Square Yard to Square Chain':{
                    'number_input' : 'Square Yard (input): '
                    },
            'Square Pole to Square Chain':{
                    'number_input' : 'Square Pole (input): '
                    },
            'Acre to Square Chain':{
                    'number_input' : 'Acre (input): '
                    },
            'Acre to Square Yard':{
                    'number_input' : 'Acre (input): '
                    },
            'Acre to Square Meter':{
                    'number_input' : 'Acre (input): '
                    },
            'Square Meter to Acre':{
                    'number_input' : 'Square Meter (input): '
                    },
            'Square Yard to Acre':{
                    'number_input' : 'Square Yard (input): '
                    },
            'Square Chain to Acre':{
                    'number_input' : 'Square Chain (input): '
                    },
            'Section to Acre':{
                    'number_input' : 'Section (input): '
                    },
            'Section to Square Mile':{
                    'number_input' : 'Section (input): '
                    },
            'Section to Square Kilometer':{
                    'number_input' : 'Section (input): '
                    },
            'Square Kilometer to Section':{
                    'number_input' : 'Square Kilometer (input): '
                    },
            'Square Mile to Section':{
                    'number_input' : 'Square Mile (input): '
                    },
            'Acre to Section':{
                    'number_input' : 'Acre (input): '
                    },
            'Township to Section':{
                    'number_input' : 'Township (input): '
                    },
            'Township to Square Mile':{
                    'number_input' : 'Township (input): '
                    },
            'Township to Square Kilometer':{
                    'number_input' : 'Township (input): '
                    },
            'Acre to Square Feet':{
                    'number_input' : 'Acre (input): '
                    },
#}}}
        }

        self.formula_list = {
                #{{{___  _____________________________________________________________________________
                
            'Acres to Hectares':{                   #acre
                'Formula:<br>': 'Acres * 0.4047'
                },
            'Hectares to Acres':{                   #hect
                'Formula:<br>': 'Hectare * 2.471'
                },
            'Square Inches to Square Feet':{        #sqin
                'Formula:<br>': 'Square Inch * 0.006944444'
                },
            'Square Feet to Square Yards':{         #sqft
                'Formula:<br>': 'Square Foot * 0.11111111'
                },
            'Square Feet to Square Rods':{          #sqft2
                'Formula:<br>' : 'Square Foot * 0.003673095'
                },
            'Square Rods to Acres':{                #sqrd
                'Formula:<br>' : 'Square Rod * 0.00625'
                },
            'Acres to Square Miles':{               #acre2
                'Formula:<br>' : 'Acre * 0.0015625'
                },
            'Square Feet to Square Miles':{         #sqft3
                'Formula:<br>' : 'Square Feet / 5280 / 5280'
                },
            'Square Feet to Acres':{                #sqft4
                'Formula:<br>' : 'Square Feet * 0.003673095 * 0.00625'
                },
            'Centiare to Square Inches':{           #cent
                'Formula:<br>' : 'Centiare * 0.000645161'
                },
            'Are to Square Yard':{                  #are
                'Formula:<br>' : 'Are * 0.008361204'
                },
            'Square Kilometer to Acre':{            #ska
                'Formula:<br>' : 'Square Kilometer * 0.004046863'
                },
            'Square Link to Square Inch':{          #link
                'Formula:<br>' : 'Square Link * 0.015941336'
                },
            'Square Link to Square Centimeter':{    #link2
                'Formula:<br>' : 'Square Link * 0.002417052'
                },
            'Square Pole to Square Link':{          #spole
                'Formula:<br>' : 'Square Pole * 0.0016'
                },
            'Square Pole to Square Yard':{          #spole2
                'Formula:<br>' : 'Square Pole * 0.033057851'
                },
            'Square Pole to Square Meter':{         #spole3
                'Formula:<br>' : 'Square Pole * 0.039536631'
                },
            'Square Chain to Square Pole':{         #schain
                'Formula:<br>' : 'Square Chain * 0.0625'
                },
            'Square Chain to Square Yard':{         #schain2
                'Formula:<br>' : 'Square Chain * 0.002066116'
                },
            'Square Chain to Square Meter':{        #schain3
                'Formula:<br>' : 'Square Chain * 0.002471052'
                },
            'Acre to Square Chain':{                #acre3
                'Formula:<br>' : 'Acre * 0.01'
                },
            'Acre to Square Yard':{                 #acre4
                'Formula:<br>' : 'Acre * 0.000206612'
                },
            'Acre to Square Meter':{                #acre5
                'Formula:<br>' : 'Acre * 0.0002471052'
                },
            'Section to Acre':{                     #section
                'Formula:<br>' : 'Section * 0.0015625'
                },
            'Section to Square Mile':{              #section2
                'Formula:<br>' : 'Section * 0.0015625'
                },
            'Section to Square Kilometer':{         #section3
                'Formula:<br>' : 'Section * 1'
                },
            'Township to Section':{                 #town
                'Formula:<br>' : 'Township * 0.027777778'
                },
            'Township to Square Mile':{             #town2
                'Formula:<br>' : 'Township * 0.027777778'
                },
            'Township to Square Kilometer':{        #town3
                'Formula:<br>' : 'Township * 0.010725011'
                },
            'Square Inch to Centiare':{             #sqin2
                'Formula:<br>' : 'Square Inch * 1550'
                },
            'Square Yard to Are':{                  #sqyrd
                'Formula:<br>' : 'Square Yard * 119.6'
                },
            'Acre to Square Kilometer':{            #acre6
                'Formula:<br>' : 'Acre * 247.105'
                },
            'Square Kilometer to Square Mile':{     #sqkm
                'Formula:<br>' : 'Square Kilometer * 25.9000259'
                },
            'Square Centimeter to Square Inch':{    #sqcm
                'Formula:<br>' : 'Square Centimeter * 0.15500031'
                },
            'Square Inch to Square Link':{          #sqin3
                'Formula:<br>' : 'Square Inch * 62.73'
                },
            'Square Meter to Square Yard':{         #sqm
                'Formula:<br>' : 'Square Meter * 119.6'
                },
            'Square Yard to Square Link':{          #sqyrd2
                'Formula:<br>' : 'Square Yard * 20.661157025'
                },
            'Square Link to Square Pole':{          #link3
                'Formula:<br>' : 'Square Link * 625'
                },
            'Square Yard to Square Pole':{          #sqyrd3
                'Formula:<br>' : 'Square Yard * 30.25'
                },
            'Square Pole to Square Chain':{         #spole4
                'Formula:<br>' : 'Square Pole * 16'
                },
            'Square Chain to Acre':{                #schain4
                'Formula:<br>' : 'Square Chain * 10'
                },
            'Acre to Section':{                     #acre7
                'Formula:<br>' : 'Acre * 640'
                },
            'Section to Township':{                 #section4
                'Formula:<br>' : 'Section * 36'
                },
            'Acre to Square Feet':{                 #acre8
                'Formula:<br>' : 'Acre * 4840 * 9'
                }
            #}}}_________________________________________________________________________________________
        }

    def acre8(self):
        # Acres to Square Feet 
        title = "Acres to Square Feet"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4840 * 9
        return (self.prec2(result), self.pluralize(result, 'Foot<sup>2</sup>'))

    def acre7(self):
        # Acre to Section 
        title = "Acre to Section"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 640
        return (self.prec2(result), self.pluralize(result, 'Section'))

    def section4(self):
        # Section to Township 
        title = "Section to Township"
        sec = "Enter Section"
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 36
        return (self.prec2(result), self.pluralize(result, 'Township'))

    def sqin3(self):
        # Square Inches to Square Link 
        title = "Square Inches to Square Link"
        sqi = "Enter Square Inch"
        argsOut = [title, sqi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 62.73
        return (self.prec2(result), self.pluralize(result, 'Link<sup>2</sup>'))

    def sqm(self):
        # Square Meters to Square Yards 
        title = "Square Meters to Square Yards"
        sqm = "Enter Square Meter"
        argsOut = [title, sqm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 119.6
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def sqyrd2(self):
        # Square Yards to Square Links 
        title = "Square Yards to Square Links"
        sqy = "Enter Square Yard"
        argsOut = [title, sqy]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 20.661157025
        return (self.prec2(result), self.pluralize(result, 'Link<sup>2</sup>'))

    def link3(self):
        # Square Link to Square Pole 
        title = "Square Link to Square Pole"
        sql = "Enter Square Link"
        argsOut = [title, sql]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 625
        return (self.prec2(result), self.pluralize(result, 'Pole<sup>2</sup>'))

    def sqyrd3(self):
        # Square Yard to Square Pole 
        title = "Square Yard to Square Pole"
        sqy = "Enter Square Yard"
        argsOut = [title, sqy]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 30.25
        return (self.prec2(result), self.pluralize(result, 'Pole<sup>2</sup>'))

    def spole4(self):
        # Square Pole to Square Chain 
        title = "Square Pole to Square Chain"
        sqp = "Enter Square Pole"
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 16
        return (self.prec2(result), self.pluralize(result, 'Chain<sup>2</sup>'))

    def schain4(self):
        # Square Chain to Acre 
        title = "Square Chain to Acre"
        sqc = "Enter Square Chain"
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 10
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def sqin2(self):
        # Square Inch to Centiare 
        title = "Square Inch to Centiare"
        sqi = "Enter Square Inch"
        argsOut = [title, sqi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1550
        return (self.prec2(result), self.pluralize(result, 'Centiare'))

    def sqyrd(self):
        # Square Yard to Are 
        title = "Square Yard to Are"
        sqy = "Enter Square Yard"
        argsOut = [title, sqy]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 119.6
        return (self.prec2(result), self.pluralize(result, 'Are'))

    def acre6(self):
        # Acre to Square Kilometer 
        title = "Acre to Square Kilometer"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 247.105
        return (self.prec2(result), self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def sqkm(self):
        # Square Kilometer to Square Mile 
        title = "Square Kilometer to Square Mile"
        sqk = "Enter Square Kilometer"
        argsOut = [title, sqk]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.59000259
        return (self.prec2(result), self.pluralize(result, 'Mile<sup>2</sup>'))

    def sqcm(self):
        # Square Centimeter to Square Inch 
        title = "Square Centimeter to Square Inch"
        sqcm = "Enter Square Centimeter"
        argsOut = [title, sqcm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.15500031
        return (self.prec2(result), self.pluralize(result, 'Inch<sup>2</sup>'))

    def acre5(self):
        # Acre to Square Mile 
        title = "Acre to Square Mile"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0002471052
        return (self.prec2(result), self.pluralize(result, 'Meter<sup>2</sup>'))

    def section(self):
        # Section to Acre 
        title = "Section to Acre"
        sec = "Enter Section"
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0015625
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def section2(self):
        # Section to Square Mile 
        title = "Section to Square Mile"
        sec = "Enter Section"
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0015625
        return (self.prec2(result), self.pluralize(result, 'Mile<sup>2</sup>'))

    def section3(self):
        # Section to Square Kilometer 
        title = "Section to Square Kilometer"
        sec = "Enter Section"
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1
        return (self.prec2(result), self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def town(self):
        # Town to Section 
        title = "Town to Section"
        town = "Enter Town"
        argsOut = [title, town]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.027777778
        return (self.prec2(result), self.pluralize(result, 'Section'))

    def town2(self):
        # Town to Square Mile 
        title = "Town to Square Mile"
        town = "Enter Town"
        argsOut = [title, town]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.027777778
        return (self.prec2(result), self.pluralize(result, 'Mile<sup>2</sup>'))

    def town3(self):
        # Town to Square Kilometer 
        title = "Town to Square Kilometer"
        town = "Enter Town"
        argsOut = [title, town]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.010725011
        return (self.prec2(result), self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def schain(self):
        # Square Chain to Square Pole 
        title = "Square Chain to Square Pole"
        sqc = "Enter Square Chain"
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0625
        return (self.prec2(result), self.pluralize(result, 'Pole<sup>2</sup>'))

    def schain2(self):
        # Square Chain to Square Yard 
        title = "Square Chain to Square Yard"
        sqc = "Enter Square Chain"
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.002066116
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def schain3(self):
        # Square Chain to Square Meter 
        title = "Square Chain to Square Meter"
        sqc = "Enter Square Chain"
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.002471052
        return (self.prec2(result), self.pluralize(result, 'Meter<sup>2</sup>'))

    def acre3(self):
        # Acre to Square Chain 
        title = "Acre to Square Chain"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.01
        return (self.prec2(result), self.pluralize(result, 'Chain<sup>2</sup>'))

    def acre4(self):
        # Acre to Square Yard 
        title = "Acre Square Yard"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.000206612
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def spole3(self):
        # Square Pole to Square Meter 
        title = "Square Pole to Square Meter"
        sqp = "Enter Square Pole"
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.039536631
        return (self.prec2(result), self.pluralize(result, 'Meter<sup>2</sup>'))

    def are(self):
        # Are to Square Yard 
        title = "Are to Square Yard"
        are = "Enter Are"
        argsOut = [title, are]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.008361204
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def cent(self):
        # Centare to Square Inch 
        title = "Centare to Square Inch"
        cent = "Enter Centare"
        argsOut = [title, cent]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.000645161
        return (self.prec2(result), self.pluralize(result, 'Inch<sup>2</sup>'))

    def ska(self):
        # Square Kilometer to Acre 
        title = "Square Kilometer to Acre"
        sqk = "Enter Square Kilometer"
        argsOut = [title, sqk]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.004046863
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def link(self):
        # Square Link to Square Inch 
        title = "Square Link to Square Inch"
        sql = "Enter Square Link"
        argsOut = [title, sql]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.015941336
        return (self.prec2(result), self.pluralize(result, 'Inch<sup>2</sup>'))

    def link2(self):
        # Square Link to Square Centimeter 
        title = "Square Link to Square Centimeter"
        sql = "Enter Square Link"
        argsOut = [title, sql]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.002417052
        return (self.prec2(result), self.pluralize(result, 'Centimeter<sup>2</sup>'))

    def spole(self):
        # Square Pole to Square Link 
        title = "Square Pole to Square Linke"
        sqp = "Enter Square Pole"
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0016
        return (self.prec2(result), self.pluralize(result, 'Link<sup>2</sup>'))

    def spole2(self):
        # Square Pole to Square Yard 
        title = "Square Pole to Square Yard"
        sqp = "Enter Square Pole"
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.033057851
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def sqft4(self):
        # Square Feet to Acre 
        title = "Square Feet to Acre"
        sqf = "Enter Square Feet"
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.003673095 * 0.00625
        return (self.prec4(result), self.pluralize(result, 'Acre'))

    def acre(self):
        # Acre to Hectare 
        title = "Acre to Hectare"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.4047
        return (self.prec2(result), self.pluralize(result, 'Hectare'))

    def hect(self):
        # Hectare to Acre 
        title = "Hectare to Acre"
        hect = "Enter Hectare"
        argsOut = [title, hect]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.471
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def sqin(self):
        # Square Inch to Square Foot 
        title = "Square Inch to Square Foor"
        sqi = "Enter Square Inch"
        argsOut = [title, sqi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.006944444
        return (self.prec2(result), self.pluralize(result, 'Square Foot'))

    def sqft(self):
        # Square Foot to Square Yard 
        title = "Square Foot to Square Yard"
        sqf = "Enter Square Foot"
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.11111111
        return (self.prec2(result), self.pluralize(result, 'Square Yard'))

    def sqft2(self):
        # Square Foot to Square Rod 
        title = "Square Foot to Square Rod"
        sqf = "Enter Square Foot"
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.003673095
        return (self.prec2(result), self.pluralize(result, 'Square Rod'))

    def sqrd(self):
        # Square Rod to Acre 
        title = "Square Rod to Acre"
        sqr = "Enter Square Rod"
        argsOut = [title, sqr]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.00625
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def acre2(self):
        # Acre to Square Mile 
        title = "Acre to Square Mile"
        acre = "Enter Acre"
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0015625
        return (self.prec2(result), self.pluralize(result, 'Square Mile'))

    def sqft3(self):
        # Square Foot to Square Mile 
        title = "Square Foot to Square Mile"
        sqf = "Enter Square Foot"
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / 5280 / 5280
        return (result, self.pluralize(result, 'Square Mile'))

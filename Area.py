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


from FormulaBase import *  

class Area (FormulaBase):
    def __init__(self):
        super (Area, self).__init__()

        self.function_list = OrderedDict(
            [
#{{{
                ('Acres to Hectares', self.acre),
                ('Hectares to Acres', self.hect),
                ('Square Inches to Square Feet', self.sqin),
                ('Square Feet to Square Yards', self.sqft),
                ('Square Feet to Square Rods', self.sqft2),
                ('Square Rods to Acres', self.sqrd),
                ('Acres to Square Miles', self.acre2),
                ('Square Feet to Square Miles', self.sqft3),
                ('Square Feet to Acres', self.sqft4),
                ('Centiare to Square Inches', self.cent),
                ('Are to Square Yard', self.are),
                ('Square Kilometer to Acre', self.ska),
                ('Square Link to Square Inch', self.link),
                ('Square Link to Square Centimeter', self.link2),
                ('Square Pole to Square Link', self.spole),
                ('Square Pole to Square Yard', self.spole2),
                ('Square Pole to Square Meter', self.spole3),
                ('Square Chain to Square Pole', self.schain),
                ('Square Chain to Square Yard', self.schain2),
                ('Square Chain to Square Meter', self.schain3),
                ('Acre to Square Chain', self.acre3),
                ('Acre to Square Yard', self.acre4),
                ('Acre to Square Meter', self.acre5),
                ('Section to Acre', self.section),
                ('Section to Square Mile', self.section2),
                ('Section to Square Kilometer', self.section3),
                ('Township to Section', self.town),
                ('Township to Square Mile', self.town2),
                ('Township to Square Kilometer', self.town3),
                ('Square Inch to Centiare', self.sqin2),
                ('Square Yard to Are', self.sqyrd),
                ('Acre to Square Kilometer', self.acre6),
                ('Square Kilometer to Square Mile', self.sqkm),
                ('Square Centimeter to Square Inch', self.sqcm),
                ('Square Inch to Square Link', self.sqin3),
                ('Square Meter to Square Yard', self.sqm),
                ('Square Yard to Square Link', self.sqyrd2),
                ('Square Link to Square Pole', self.link3),
                ('Square Yard to Square Pole', self.sqyrd3),
                ('Square Pole to Square Chain', self.spole4),
                ('Square Chain to Acre', self.schain4),
                ('Acre to Section', self.acre7),
                ('Section to Township', self.section4),
                ('Acre to Square Feet', self.acre8),
            ]
        )
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

    def acre8(self, num):
        result = float(num) * 4840 * 9
        return (self.prec2(result), self.pluralize(result, 'Foot<sup>2</sup>'))

    def acre7(self, num):
        result = float(num) * 640
        return (self.prec2(result), self.pluralize(result, 'Section'))

    def section4(self, num):
        result = float(num) * 36
        return (self.prec2(result), self.pluralize(result, 'Township'))

    def sqin3(self, num):
        result = float(num) * 62.73
        return (self.prec2(result), self.pluralize(result, 'Link<sup>2</sup>'))

    def sqm(self, num):
        result = float(num) * 119.6
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def sqyrd2(self, num):
        result = float(num) * 20.661157025
        return (self.prec2(result), self.pluralize(result, 'Link<sup>2</sup>'))

    def link3(self, num):
        result = float(num) * 625
        return (self.prec2(result), self.pluralize(result, 'Pole<sup>2</sup>'))

    def sqyrd3(self, num):
        result = float(num) * 30.25
        return (self.prec2(result), self.pluralize(result, 'Pole<sup>2</sup>'))

    def spole4(self, num):
        result = float(num) * 16
        return (self.prec2(result), self.pluralize(result, 'Chain<sup>2</sup>'))

    def schain4(self, num):
        result = float(num) * 10
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def sqin2(self, num):
        result = float(num) * 1550
        return (self.prec2(result), self.pluralize(result, 'Centiare'))

    def sqyrd(self, num):
        result = float(num) * 119.6
        return (self.prec2(result), self.pluralize(result, 'Are'))

    def acre6(self, num):
        result = float(num) * 247.105
        return (self.prec2(result), self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def sqkm(self, num):
        result = float(num) * 2.59000259
        return (self.prec2(result), self.pluralize(result, 'Mile<sup>2</sup>'))

    def sqcm(self, num):
        result = float(num) * 0.15500031
        return (self.prec2(result), self.pluralize(result, 'Inch<sup>2</sup>'))

    def acre5(self, num):
        result = float(num) * 0.0002471052
        return (self.prec2(result), self.pluralize(result, 'Meter<sup>2</sup>'))

    def section(self, num):
        result = float(num) * 0.0015625
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def section2(self, num):
        result = float(num) * 0.0015625
        return (self.prec2(result), self.pluralize(result, 'Mile<sup>2</sup>'))

    def section3(self, num):
        result = float(num) * 1
        return (self.prec2(result), self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def town(self, num):
        result = float(num) * 0.027777778
        return (self.prec2(result), self.pluralize(result, 'Section'))

    def town2(self, num):
        result = float(num) * 0.027777778
        return (self.prec2(result), self.pluralize(result, 'Mile<sup>2</sup>'))

    def town3(self, num):
        result = float(num) * 0.010725011
        return (self.prec2(result), self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def schain(self, num):
        result = float(num) * 0.0625
        return (self.prec2(result), self.pluralize(result, 'Pole<sup>2</sup>'))

    def schain2(self, num):
        result = float(num) * 0.002066116
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def schain3(self, num):
        result = float(num) * 0.002471052
        return (self.prec2(result), self.pluralize(result, 'Meter<sup>2</sup>'))

    def acre3(self, num):
        result = float(num) * 0.01
        return (self.prec2(result), self.pluralize(result, 'Chain<sup>2</sup>'))

    def acre4(self, num):
        result = float(num) * 0.000206612
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def spole3(self, num):
        result = float(num) * 0.039536631
        return (self.prec2(result), self.pluralize(result, 'Meter<sup>2</sup>'))

    def are(self, num):
        result = float(num) * 0.008361204
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def cent(self, num):
        result = float(num) * 0.000645161
        return (self.prec2(result), self.pluralize(result, 'Inch<sup>2</sup>'))

    def ska(self, num):
        result = float(num) * 0.004046863
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def link(self, num):
        result = float(num) * 0.015941336
        return (self.prec2(result), self.pluralize(result, 'Inch<sup>2</sup>'))

    def link2(self, num):
        result = float(num) * 0.002417052
        return (self.prec2(result), self.pluralize(result, 'Centimeter<sup>2</sup>'))

    def spole(self, num):
        result = float(num) * 0.0016
        return (self.prec2(result), self.pluralize(result, 'Link<sup>2</sup>'))

    def spole2(self, num):
        result = float(num) * 0.033057851
        return (self.prec2(result), self.pluralize(result, 'Yard<sup>2</sup>'))

    def sqft4(self, num):
        result = float(num) * 0.003673095 * 0.00625
        return (self.prec4(result), self.pluralize(result, 'Acre'))

    def acre(self, num):
        result = float(num) * 0.4047
        return (self.prec2(result), self.pluralize(result, 'Hectare'))

    def hect(self, num):
        result = float(num) * 2.471
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def sqin(self, num):
        result = float(num) * 0.006944444
        return (self.prec2(result), self.pluralize(result, 'Square Foot'))

    def sqft(self, num):
        result = float(num) * 0.11111111
        return (self.prec2(result), self.pluralize(result, 'Square Yard'))

    def sqft2(self, num):
        result = float(num) * 0.003673095
        return (self.prec2(result), self.pluralize(result, 'Square Rod'))

    def sqrd(self, num):
        result = float(num) * 0.00625
        return (self.prec2(result), self.pluralize(result, 'Acre'))

    def acre2(self, num):
        result = float(num) * 0.0015625
        return (self.prec2(result), self.pluralize(result, 'Square Mile'))

    def sqft3(self, num):
        result = float(num) / 5280 / 5280
        return (result, self.pluralize(result, 'Square Mile'))

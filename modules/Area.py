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

#{{{___ Function Titles _____________________________________________________________________________

        self.function_strings = {
            1 : 'Acre to Hectare',
            2 : 'Hectare to Acre',
            3 : 'Square Inch to Square Foot',
            4 : 'Square Foot to Square Yard',
            5 : 'Square Foot to Square Rod',
            6 : 'Square Rod to Acre',
            7 : 'Acre to Square Mile',
            8 : 'Square Foot to Square Mile',
            9 : 'Square Foot to Acre',
            10 : 'Centiare to Square Inch',
            11 : 'Are to Square Yard',
            12 : 'Square Kilometer to Acre',
            13 : 'Square Link to Square Inch',
            14 : 'Square Link to Square Centimeter',
            15 : 'Square Pole to Square Link',
            16 : 'Square Pole to Square Yard',
            17 : 'Square Pole to Square Meter',
            18 : 'Square Chain to Square Pole',
            19 : 'Square Chain to Square Yard',
            20 : 'Square Chain to Square Meter',
            21 : 'Acre to Square Chain',
            22 : 'Acre to Square Yard',
            23 : 'Acre to Square Meter',
            24 : 'Section to Acre',
            25 : 'Section to Square Mile',
            26 : 'Section to Square Kilometer',
            27 : 'Township to Section',
            28 : 'Township to Square Mile',
            29 : 'Township to Square Kilometer',
            30 : 'Square Inch to Centiare',
            31 : 'Square Yard to Are',
            32 : 'Acre to Square Kilometer',
            33 : 'Square Kilometer to Square Mile',
            34 : 'Square Centimeter to Square Inch',
            35 : 'Square Inch to Square Link',
            36 : 'Square Meter to Square Yard',
            37 : 'Square Yard to Square Link',
            38 : 'Square Link to Square Pole',
            39 : 'Square Yard to Square Pole',
            40 : 'Square Pole to Square Chain',
            41 : 'Square Chain to Acre',
            42 : 'Acre to Section',
            43 : 'Section to Township',
            44 : 'Acre to Square Foot',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.acre),
                (self.function_strings[2], self.hect),
                (self.function_strings[3], self.sqin),
                (self.function_strings[4], self.sqft),
                (self.function_strings[5], self.sqft2),
                (self.function_strings[6], self.sqrd),
                (self.function_strings[7], self.acre2),
                (self.function_strings[8], self.sqft3),
                (self.function_strings[9], self.sqft4),
                (self.function_strings[10], self.cent),
                (self.function_strings[11], self.are),
                (self.function_strings[12], self.ska),
                (self.function_strings[13], self.link),
                (self.function_strings[14], self.link2),
                (self.function_strings[15], self.spole),
                (self.function_strings[16], self.spole2),
                (self.function_strings[17], self.spole3),
                (self.function_strings[18], self.schain),
                (self.function_strings[19], self.schain2),
                (self.function_strings[20], self.schain3),
                (self.function_strings[21], self.acre3),
                (self.function_strings[22], self.acre4),
                (self.function_strings[23], self.acre5),
                (self.function_strings[24], self.section),
                (self.function_strings[25], self.section2),
                (self.function_strings[26], self.section3),
                (self.function_strings[27], self.town),
                (self.function_strings[28], self.town2),
                (self.function_strings[29], self.town3),
                (self.function_strings[30], self.sqin2),
                (self.function_strings[31], self.sqyrd),
                (self.function_strings[32], self.acre6),
                (self.function_strings[33], self.sqkm),
                (self.function_strings[34], self.sqcm),
                (self.function_strings[35], self.sqin3),
                (self.function_strings[36], self.sqm),
                (self.function_strings[37], self.sqyrd2),
                (self.function_strings[38], self.link3),
                (self.function_strings[39], self.sqyrd3),
                (self.function_strings[40], self.spole4),
                (self.function_strings[41], self.schain4),
                (self.function_strings[42], self.acre7),
                (self.function_strings[43], self.section4),
                (self.function_strings[44], self.acre8),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Function Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[43]:{
                'number_input' : 'Section (input): '
                },
            self.function_strings[9]:{
                'number_input' : 'Square Feet (input): '
                },
            self.function_strings[8]:{
                'number_input' : 'Square Feet (input): '
                },
            self.function_strings[1]:{
                'number_input' : 'Acres (input): '
                },
            self.function_strings[2]:{
                'number_input' : 'Hectares (input): '
                },
            self.function_strings[3]:{
                'number_input' : 'Square Inches (input): '
                },
            self.function_strings[4]:{
                'number_input' : 'Square Feet (input): '
                },
            self.function_strings[5]:{
                'number_input' : 'Square Feet (input): '
                },
            self.function_strings[6]:{
                'number_input' : 'Square Rods (input): '
                },
            self.function_strings[7]:{
                'number_input' : 'Acres (input): '
                },
            self.function_strings[10]:{
                'number_input' : 'Centiare (input): '
                },
            self.function_strings[30]:{
                'number_input' : 'Square Inch (input): '
                },
            self.function_strings[11]:{
                'number_input' : 'Are (input): '
                },
            'Are to Centiare':{
                'number_input' : 'Are (input): '
                },
            self.function_strings[31]:{
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
            self.function_strings[12]:{
                'number_input' : 'Square Kilometer (input): '
                },
            self.function_strings[33]:{
                'number_input' : 'Square Kilometers (input): '
                },
            'Square Mile to Square Kilometer':{
                    'number_input' : 'Square Mile (input): '
                    },
            self.function_strings[32]:{
                    'number_input' : 'Acre (input): '
                    },
            'Hectare to Square Kilometer':{
                    'number_input' : 'Hectare (input): '
                    },
            self.function_strings[13]:{
                'number_input' : 'Square Link (input): '
                },
            self.function_strings[14]:{
                'number_input' : 'Square Link (input): '
                },
            'Square Centimeter to Square Link':{
                    'number_input' : 'Square Centimeter (input): '
                },
            self.function_strings[35]:{
                    'number_input' : 'Square Inch (input): '
                },
            'Square Meter to Square Pole':{
                    'number_input' : 'Square Meter (input): '
                },
            self.function_strings[39]:{
                    'number_input' : 'Square Yard (input): '
                },
            self.function_strings[38]:{
                    'number_input' : 'Square Link (input): '
                },
            self.function_strings[15]:{
                'number_input' : 'Square Pole (input): '
                },
            self.function_strings[16]:{
                'number_input' : 'Square Pole (input): '
                },
            self.function_strings[17]:{
                'number_input' : 'Square Pole (input): '
                },
            self.function_strings[18]:{
                'number_input' : 'Square Chain (input): '
                },
            self.function_strings[19]:{
                    'number_input' : 'Square Chain (input): '
                },
            self.function_strings[20]:{
                    'number_input' : 'Square Chain (input): '
                },
            'Square Meter to Square Chain':{
                    'number_input' : 'Square Meter (input): '
                },
            'Square Yard to Square Chain':{
                    'number_input' : 'Square Yard (input): '
                },
            self.function_strings[40]:{
                    'number_input' : 'Square Pole (input): '
                },
            self.function_strings[21]:{
                    'number_input' : 'Acre (input): '
                },
            self.function_strings[22]:{
                    'number_input' : 'Acre (input): '
                },
            self.function_strings[23]:{
                    'number_input' : 'Acre (input): '
                },
            'Square Meter to Acre':{
                    'number_input' : 'Square Meter (input): '
                },
            'Square Yard to Acre':{
                    'number_input' : 'Square Yard (input): '
                },
            self.function_strings[41]:{
                    'number_input' : 'Square Chain (input): '
                },
            self.function_strings[24]:{
                    'number_input' : 'Section (input): '
                },
            self.function_strings[25]:{
                    'number_input' : 'Section (input): '
                },
            self.function_strings[26]:{
                    'number_input' : 'Section (input): '
                },
            'Square Kilometer to Section':{
                    'number_input' : 'Square Kilometer (input): '
                },
            'Square Mile to Section':{
                    'number_input' : 'Square Mile (input): '
                },
            self.function_strings[42]:{
                    'number_input' : 'Acre (input): '
                },
            self.function_strings[27]:{
                    'number_input' : 'Township (input): '
                },
            self.function_strings[28]:{
                    'number_input' : 'Township (input): '
                },
            self.function_strings[29]:{
                    'number_input' : 'Township (input): '
                },
            self.function_strings[44]:{
                    'number_input' : 'Acre (input): '
                },
            self.function_strings[34]:{
                    'number_input' : 'Square Centimeter (input): '
                },
            self.function_strings[36]:{
                    'number_input' : 'Square Meter (input): '
                },
            self.function_strings[37]:{
                    'number_input' : 'Square Yard (input): '
                },
        }
#}}}_________________________________________________________________________________________

#{{{___ Show Formula _____________________________________________________________________________
        self.formula_list = {
            self.function_strings[1]:{                   #acre
                'Formula:<br>': 'Acres * 0.4047'
                },
            self.function_strings[2]:{                   #hect
                'Formula:<br>': 'Hectare * 2.471'
                },
            self.function_strings[3]:{        #sqin
                'Formula:<br>': 'Square Inch * 0.006944444'
                },
            self.function_strings[4]:{         #sqft
                'Formula:<br>': 'Square Foot * 0.11111111'
                },
            self.function_strings[5]:{          #sqft2
                'Formula:<br>' : 'Square Foot * 0.003673095'
                },
            self.function_strings[6]:{                #sqrd
                'Formula:<br>' : 'Square Rod * 0.00625'
                },
            self.function_strings[7]:{               #acre2
                'Formula:<br>' : 'Acre * 0.0015625'
                },
            self.function_strings[8]:{         #sqft3
                'Formula:<br>' : 'Square Feet / 5280 / 5280'
                },
            self.function_strings[9]:{                #sqft4
                'Formula:<br>' : 'Square Feet * 0.003673095 * 0.00625'
                },
            self.function_strings[10]:{           #cent
                'Formula:<br>' : 'Centiare * 0.000645161'
                },
            self.function_strings[11]:{                  #are
                'Formula:<br>' : 'Are * 0.008361204'
                },
            self.function_strings[12]:{            #ska
                'Formula:<br>' : 'Square Kilometer * 0.004046863'
                },
            self.function_strings[13]:{          #link
                'Formula:<br>' : 'Square Link * 0.015941336'
                },
            self.function_strings[14]:{    #link2
                'Formula:<br>' : 'Square Link * 0.002417052'
                },
            self.function_strings[15]:{          #spole
                'Formula:<br>' : 'Square Pole * 0.0016'
                },
            self.function_strings[16]:{          #spole2
                'Formula:<br>' : 'Square Pole * 0.033057851'
                },
            self.function_strings[17]:{         #spole3
                'Formula:<br>' : 'Square Pole * 0.039536631'
                },
            self.function_strings[18]:{         #schain
                'Formula:<br>' : 'Square Chain * 0.0625'
                },
            self.function_strings[19]:{         #schain2
                'Formula:<br>' : 'Square Chain * 0.002066116'
                },
            self.function_strings[20]:{        #schain3
                'Formula:<br>' : 'Square Chain * 0.002471052'
                },
            self.function_strings[21]:{                #acre3
                'Formula:<br>' : 'Acre * 0.01'
                },
            self.function_strings[22]:{                 #acre4
                'Formula:<br>' : 'Acre * 0.000206612'
                },
            self.function_strings[23]:{                #acre5
                'Formula:<br>' : 'Acre * 0.0002471052'
                },
            self.function_strings[24]:{                     #section
                'Formula:<br>' : 'Section * 0.0015625'
                },
            self.function_strings[25]:{              #section2
                'Formula:<br>' : 'Section * 0.0015625'
                },
            self.function_strings[26]:{         #section3
                'Formula:<br>' : 'Section * 1'
                },
            self.function_strings[27]:{                 #town
                'Formula:<br>' : 'Township * 0.027777778'
                },
            self.function_strings[28]:{             #town2
                'Formula:<br>' : 'Township * 0.027777778'
                },
            self.function_strings[29]:{        #town3
                'Formula:<br>' : 'Township * 0.010725011'
                },
            self.function_strings[30]:{             #sqin2
                'Formula:<br>' : 'Square Inch * 1550'
                },
            self.function_strings[31]:{                  #sqyrd
                'Formula:<br>' : 'Square Yard * 119.6'
                },
            self.function_strings[32]:{            #acre6
                'Formula:<br>' : 'Acre * 247.105'
                },
            self.function_strings[33]:{     #sqkm
                'Formula:<br>' : 'Square Kilometer * 25.9000259'
                },
            self.function_strings[34]:{    #sqcm
                'Formula:<br>' : 'Square Centimeter * 0.15500031'
                },
            self.function_strings[35]:{          #sqin3
                'Formula:<br>' : 'Square Inch * 62.73'
                },
            self.function_strings[36]:{         #sqm
                'Formula:<br>' : 'Square Meter * 119.6'
                },
            self.function_strings[37]:{          #sqyrd2
                'Formula:<br>' : 'Square Yard * 20.661157025'
                },
            self.function_strings[38]:{          #link3
                'Formula:<br>' : 'Square Link * 625'
                },
            self.function_strings[39]:{          #sqyrd3
                'Formula:<br>' : 'Square Yard * 30.25'
                },
            self.function_strings[40]:{         #spole4
                'Formula:<br>' : 'Square Pole * 16'
                },
            self.function_strings[41]:{                #schain4
                'Formula:<br>' : 'Square Chain * 10'
                },
            self.function_strings[42]:{                     #acre7
                'Formula:<br>' : 'Acre * 640'
                },
            self.function_strings[43]:{                 #section4
                'Formula:<br>' : 'Section * 36'
                },
            self.function_strings[44]:{                 #acre8
                'Formula:<br>' : 'Acre * 4840 * 9'
                }
        }
#}}}_________________________________________________________________________________________

#{{{___ Functions _____________________________________________________________________________

    def acre8(self):
        # Acres to Square Feet 
        title = 'Acres to Square Foot'
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 4840 * 9
        return (result, self.pluralize(result, 'Foot<sup>2</sup>'))

    def acre7(self):
        # Acre to Section 
        title = 'Acre to Section'
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 640
        return (result, self.pluralize(result, 'Section'))

    def section4(self):
        # Section to Township 
        title = 'Section to Township'
        sec = 'Enter Section'
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 36
        return (result, self.pluralize(result, 'Township'))

    def sqin3(self):
        # Square Inches to Square Link 
        title = 'Square Inch to Square Link'
        sqi = 'Enter Square Inch'
        argsOut = [title, sqi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 62.73
        return (result, self.pluralize(result, 'Link<sup>2</sup>'))

    def sqm(self):
        # Square Meters to Square Yards 
        title = 'Square Meter to Square Yard'
        sqm = 'Enter Square Meter'
        argsOut = [title, sqm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 119.6
        return (result, self.pluralize(result, 'Yard<sup>2</sup>'))

    def sqyrd2(self):
        # Square Yards to Square Links 
        title = 'Square Yard to Square Link'
        sqy = 'Enter Square Yard'
        argsOut = [title, sqy]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 20.661157025
        return (result, self.pluralize(result, 'Link<sup>2</sup>'))

    def link3(self):
        # Square Link to Square Pole 
        title = 'Square Link to Square Pole'
        sql = 'Enter Square Link'
        argsOut = [title, sql]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 625
        return (result, self.pluralize(result, 'Pole<sup>2</sup>'))

    def sqyrd3(self):
        # Square Yard to Square Pole 
        title = 'Square Yard to Square Pole'
        sqy = 'Enter Square Yard'
        argsOut = [title, sqy]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 30.25
        return (result, self.pluralize(result, 'Pole<sup>2</sup>'))

    def spole4(self):
        # Square Pole to Square Chain 
        title = 'Square Pole to Square Chain'
        sqp = 'Enter Square Pole'
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 16
        return (result, self.pluralize(result, 'Chain<sup>2</sup>'))

    def schain4(self):
        # Square Chain to Acre 
        title = 'Square Chain to Acre'
        sqc = 'Enter Square Chain'
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 10
        return (result, self.pluralize(result, 'Acre'))

    def sqin2(self):
        # Square Inch to Centiare 
        title = 'Square Inch to Centiare'
        sqi = 'Enter Square Inch'
        argsOut = [title, sqi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1550
        return (result, self.pluralize(result, 'Centiare'))

    def sqyrd(self):
        # Square Yard to Are 
        title = 'Square Yard to Are'
        sqy = 'Enter Square Yard'
        argsOut = [title, sqy]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 119.6
        return (result, self.pluralize(result, 'Are'))

    def acre6(self):
        # Acre to Square Kilometer 
        title = 'Acre to Square Kilometer'
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 247.105
        return (result, self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def sqkm(self):
        # Square Kilometer to Square Mile 
        title = 'Square Kilometer to Square Mile'
        sqk = 'Enter Square Kilometer'
        argsOut = [title, sqk]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.59000259
        return (result, self.pluralize(result, 'Mile<sup>2</sup>'))

    def sqcm(self):
        # Square Centimeter to Square Inch 
        title = 'Square Centimeter to Square Inch'
        sqcm = 'Enter Square Centimeter'
        argsOut = [title, sqcm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.15500031
        return (result, self.pluralize(result, 'Inch<sup>2</sup>'))

    def acre5(self):
        # Acre to Square Mile 
        title = self.function_strings[7]
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0002471052
        return (result, self.pluralize(result, 'Meter<sup>2</sup>'))

    def section(self):
        # Section to Acre 
        title = 'Section to Acre'
        sec = 'Enter Section'
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0015625
        return (result, self.pluralize(result, 'Acre'))

    def section2(self):
        # Section to Square Mile 
        title = 'Section to Square Mile'
        sec = 'Enter Section'
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0015625
        return (result, self.pluralize(result, 'Mile<sup>2</sup>'))

    def section3(self):
        # Section to Square Kilometer 
        title = 'Section to Square Kilometer'
        sec = 'Enter Section'
        argsOut = [title, sec]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1
        return (result, self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def town(self):
        # Town to Section 
        title = 'Town to Section'
        town = 'Enter Town'
        argsOut = [title, town]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.027777778
        return (result, self.pluralize(result, 'Section'))

    def town2(self):
        # Town to Square Mile 
        title = 'Town to Square Mile'
        town = 'Enter Town'
        argsOut = [title, town]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.027777778
        return (result, self.pluralize(result, 'Mile<sup>2</sup>'))

    def town3(self):
        # Town to Square Kilometer 
        title = 'Town to Square Kilometer'
        town = 'Enter Town'
        argsOut = [title, town]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.010725011
        return (result, self.pluralize(result, 'Kilometer<sup>2</sup>'))

    def schain(self):
        # Square Chain to Square Pole 
        title = 'Square Chain to Square Pole'
        sqc = 'Enter Square Chain'
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0625
        return (result, self.pluralize(result, 'Pole<sup>2</sup>'))

    def schain2(self):
        # Square Chain to Square Yard 
        title = 'Square Chain to Square Yard'
        sqc = 'Enter Square Chain'
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.002066116
        return (result, self.pluralize(result, 'Yard<sup>2</sup>'))

    def schain3(self):
        # Square Chain to Square Meter 
        title = 'Square Chain to Square Meter'
        sqc = 'Enter Square Chain'
        argsOut = [title, sqc]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.002471052
        return (result, self.pluralize(result, 'Meter<sup>2</sup>'))

    def acre3(self):
        # Acre to Square Chain 
        title = 'Acre to Square Chain'
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.01
        return (result, self.pluralize(result, 'Chain<sup>2</sup>'))

    def acre4(self):
        # Acre to Square Yard 
        title = 'Acre to Square Yard'
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.000206612
        return (result, self.pluralize(result, 'Yard<sup>2</sup>'))

    def spole3(self):
        # Square Pole to Square Meter 
        title = 'Square Pole to Square Meter'
        sqp = 'Enter Square Pole'
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.039536631
        return (result, self.pluralize(result, 'Meter<sup>2</sup>'))

    def are(self):
        # Are to Square Yard 
        title = 'Are to Square Yard'
        are = 'Enter Are'
        argsOut = [title, are]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.008361204
        return (result, self.pluralize(result, 'Yard<sup>2</sup>'))

    def cent(self):
        # Centare to Square Inch 
        title = 'Centare to Square Inch'
        cent = 'Enter Centare'
        argsOut = [title, cent]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.000645161
        return (result, self.pluralize(result, 'Inch<sup>2</sup>'))

    def ska(self):
        # Square Kilometer to Acre 
        title = 'Square Kilometer to Acre'
        sqk = 'Enter Square Kilometer'
        argsOut = [title, sqk]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.004046863
        return (result, self.pluralize(result, 'Acre'))

    def link(self):
        # Square Link to Square Inch 
        title = 'Square Link to Square Inch'
        sql = 'Enter Square Link'
        argsOut = [title, sql]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.015941336
        return (result, self.pluralize(result, 'Inch<sup>2</sup>'))

    def link2(self):
        # Square Link to Square Centimeter 
        title = 'Square Link to Square Centimeter'
        sql = 'Enter Square Link'
        argsOut = [title, sql]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.002417052
        return (result, self.pluralize(result, 'Centimeter<sup>2</sup>'))

    def spole(self):
        # Square Pole to Square Link 
        title = 'Square Pole to Square Link'
        sqp = 'Enter Square Pole'
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0016
        return (result, self.pluralize(result, 'Link<sup>2</sup>'))

    def spole2(self):
        # Square Pole to Square Yard 
        title = 'Square Pole to Square Yard'
        sqp = 'Enter Square Pole'
        argsOut = [title, sqp]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.033057851
        return (result, self.pluralize(result, 'Yard<sup>2</sup>'))

    def sqft4(self):
        # Square Feet to Acre 
        title = 'Square Feet to Acre'
        sqf = 'Enter Square Feet'
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.003673095 * 0.00625
        return (self.prec4(result), self.pluralize(result, 'Acre'))

    def acre(self):
        # Acre to Hectare 
        title = self.function_strings[1]
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.4047
        return (result, self.pluralize(result, 'Hectare'))

    def hect(self):
        # Hectare to Acre 
        title = self.function_strings[2]
        hect = 'Enter Hectare'
        argsOut = [title, hect]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 2.471
        return (result, self.pluralize(result, 'Acre'))

    def sqin(self):
        # Square Inch to Square Foot 
        title = self.function_strings[3]
        sqi = 'Enter Square Inch'
        argsOut = [title, sqi]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.006944444
        return (result, self.pluralize(result, 'Square Foot'))

    def sqft(self):
        # Square Foot to Square Yard 
        title = self.function_strings[4]
        sqf = 'Enter Square Foot'
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.11111111
        return (result, self.pluralize(result, 'Square Yard'))

    def sqft2(self):
        # Square Foot to Square Rod 
        title = self.function_strings[5]
        sqf = 'Enter Square Foot'
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.003673095
        return (result, self.pluralize(result, 'Square Rod'))

    def sqrd(self):
        # Square Rod to Acre 
        title = self.function_strings[6]
        sqr = 'Enter Square Rod'
        argsOut = [title, sqr]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.00625
        return (result, self.pluralize(result, 'Acre'))

    def acre2(self):
        # Acre to Square Mile 
        title = self.function_strings[7]
        acre = 'Enter Acre'
        argsOut = [title, acre]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 0.0015625
        return (result, self.pluralize(result, 'Square Mile'))

    def sqft3(self):
        # Square Foot to Square Mile 
        title = self.function_strings[8]
        sqf = 'Enter Square Foot'
        argsOut = [title, sqf]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / 5280 / 5280
        return (result, self.pluralize(result, 'Square Mile'))

#}}}_________________________________________________________________________________________


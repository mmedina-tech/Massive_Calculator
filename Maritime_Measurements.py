#!/usr/bin/python
#SYNOPSIS: Converting Maritime Measurements to statute/metric

from FormulaBase import * 

class Maritime_Measurements(FormulaBase):
    """
    This class represents Converting Maritime Measurements
    """

    def __init__(self, name):
        super(Maritime_Measurements, self).__init__(name)
        self.name = name

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                ("Fathoms to Feet", self.ff),
                ("Cable to Fathom", self.cf),
                ("Nautical Miles to Feet", self.nmf),
                ("Fathoms to Meters", self.fm),
                ("Nautical Miles to Cables", self.nmc),
                ("Nautical Miles to Meters", self.nmm),
                ("Nautical Miles to Statute Miles", self.nmsm),
                ("Knots to Nautical Miles per Hour", self.knots),
                ("Meters to Fathoms", self.mf),
                ("Nautical Miles to Kilometers", self.nmk),
                ("Kilometers to Nautical Miles", self.knm),
                ("Miles to Nautical Miles", self.Mnm),
                ("Knots to Kilometers per Hour", self.Kkph),
                ("Kilometers per Hour to Knots", self.kphK),
                ("Knots to Miles per Hour", self.Kmph),
                ("Miles per Hour to Knots", self.mphK),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Inputs _____________________________________________________________________________

        self.functionInputs = {
            "Fathoms to Feet":{
                "number_input" : "Fathoms (input):"
                    },
            "Cable to Fathom":{
                "number_input" : "Cable (input):"
                    },
            "Nautical Miles to Feet":{
                "number_input" : "Nautical Miles (input):"
                    },
            "Fathoms to Meters":{
                "number_input" : "Fathom (input):"
                    },
            "Nautical Miles to Cables":{
                "number_input" : "Nautical Miles (input):"
                    },
            "Nautical Miles to Meters":{
                "number_input" : "Nautical Miles (input):"
                    },
            "Nautical Miles to Statute Miles":{
                "number_input" : "Nautical Miles (input):"
                    },
            "Knots to Nautical Miles per Hour":{
                "number_input" : "Knots (input):"
                    },
            "Meters to Fathoms":{
                "number_input" : "Meter (input):"
                    },
            "Nautical Miles to Kilometers":{
                "number_input" : "Nautical Miles (input):"
                    },
            "Kilometers to Nautical Miles":{
                "number_input" : "Kilometers (input):"
                    },
            "Miles to Nautical Miles":{
                "number_input" : "Miles (input):"
                    },
            "Knots to Kilometers per Hour":{
                "number_input" : "Knots (input):"
                    },
            "Kilometers per Hour to Knots":{
                "number_input" : "Kilometers per Hour (input):"
                    },
            "Knots to Miles per Hour":{
                "number_input" : "Knots (input):"
                    },
            "Miles per Hour to Knots":{
                "number_input" : "Miles per Hour (input):"
                    },
            }
#}}}_________________________________________________________________________________________

#{{{___ Formula List _____________________________________________________________________________

        self.formula_list = {
            'Fathoms to Feet':{
                '' : 'Fathom * 6'
            },
            'Cable to Fathom':{
                '' : 'Cable * 0.01'
            },
            'Nautical Miles to Feet':{
                '' : 'Nautical Miles * 6076'
            },
            'Fathoms to Meters':{
                '' : 'Fathoms * 0.546448087'
            },
            'Nautical Miles to Cables':{
                '' : 'Nautical Miles * 10'
            },
            'Nautical Miles to Meters':{
                '' : 'Nautical Miles * 1852'
            },
            'Nautical Miles to Statute Miles':{
                '' : 'Nautical Miles * 1.15'
            },
            'Knots to Nautical Miles per Hour':{
                '' : 'Knots * 1'
            },
            'Meters to Fathoms':{
                '' : 'Meters * 1.83'
            },
            'Nautical Miles to Kilometers':{
                '' : 'Nautical Miles * 0.539956803456'
            },
            'Kilometers to Nautical Miles':{
                '' : 'Kilometers * 1.852'
            },
            'Miles to Nautical Miles':{
                '' : 'Miles * 1.150775577122'
            },
            'Knots to Kilometers per Hour':{
                '' : 'Kilometer * 1.93968964967'
            },
            'Kilometers per Hour to Knots':{
                '' : 'Kilometers per Hour * 0.59'
            },
            'Miles per Hour to Knots':{
                '' : 'Miles per Hour * 1.69491525424'
            },
            'Knots to Miles per Hour':{
                '' : 'Knots * 0.59'
            },
        }
#}}}_________________________________________________________________________________________

#{{{___ Formula Functions _____________________________________________________________________________

    def ff(self, num):
        title = "Fathoms to Feet"
        fath = "Enter Fathoms"
        argsOut = [title, fath]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 6
        return (self.prec2(result), self.pluralize(result, "Foot"))

    def cf(self):
        title = "Cables to Fathoms"
        cb = "Enter Cables"
        argsOut = [title, cb]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .01
        return (self.prec2(result) , self.pluralize(result, "Fathom"))

    def nmf(self):
        title = "Nautical Miles to Feet"
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 6076
        return (self.prec2(result), self.pluralize(result, "Foot"))

    def fm(self):
        title = "Fathoms to Meters"
        fath = "Enter Fathoms"
        argsOut = [title, fath]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .546448087
        return (self.prec2(result), self.pluralize(result, "Meter"))

    def nmc(self):
        title = "Nautical Miles to Cables"
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 10
        return (self.prec2(result), self.pluralize(result, "Cable"))

    def nmm(self):
        title = "Nautical Miles to Meters"
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1852
        return (self.prec2(result), self.pluralize(result, "Meter"))

    def nmsm(self):
        title = "Nautical Miles to Statute Miles"
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.15
        return (self.prec2(result), self.pluralize(result, "Statute Mile"))

    def knots(self):
        title = "Knots to Nautical Miles"
        knot = "Enter Knots"
        argsOut = [title, knot]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1
        return (self.prec2(result), self.pluralize(result, "Nautical Mile"))

    def mf(self):
        title = "Meters to Fathoms"
        m = "Enter Meters"
        argsOut = [title, m]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.83
        return (self.prec2(result), self.pluralize(result, "Fathom"))

    def nmk(self):
        title = "Nautical Miles to Kilometers"
        nm = "Enter Nautical Miles"
        argsOut = [title, nm]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .539956803456
        return (self.prec2(result), self.pluralize(result, "Kilometer"))

    def knm(self):
        title = "Kilometers to Nautical Miels"
        k = "Enter Kilometers"
        argsOut = [title, k]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.852
        return (self.prec2(result), self.pluralize(result, "Nautical Mile"))

    def Mnm(self):
        title = "Miles to Nautical Miles"
        M = "Enter Miles"
        argsOut = [title, M]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.150774477122
        return (self.prec2(result), self.pluralize(result, "Nautical Mile"))

    def Kkph(self):
        title = "Kilometers to Kilometers per Hour"
        K = "Enter Kilometers"
        argsOut = [title, K]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.93968964967
        return (self.prec2(result), self.pluralize(result, "Kilometer per Hour"))

    def kphK(self):
        title = "Kilometers per Hour to Knots"
        kph = "Enter Kilometers per Hour"
        argsOut = [title, kph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .515546391749
        return (self.prec2(result), self.pluralize(result, "Knot"))

    def Kmph(self):
        title = "Knots to Miles per Hour"
        K = "Enter Knots"
        argsOut = [title, K]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * .59
        return (self.prec2(result), self.pluralize(result, "Mile per Hour"))

    def mphK(self):
        title = "Miles per Hour to Knots"
        mph = "Enter Miles per Hour"
        argsOut = [title, mph]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] * 1.69491525424
        return (self.prec2(result), self.pluralize(result, "Knot"))
#}}}_________________________________________________________________________________________


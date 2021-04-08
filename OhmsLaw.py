#!/usr/bin/python

from FormulaBase import *

class OhmsLaw(FormulaBase):
    def __init__(self, name):
        super(OhmsLaw, self).__init__(name)
        self.name = name 
        
        self.function_list = OrderedDict(
            [
                #{{{___  _____________________________________________________________________________
                
                ('Volts using Amps and Resistance', self.form_voltsar),
                ('Volts using Watts and Amps', self.form_voltswa),
                ('Volts using Watts and Resistance', self.form_voltswr),
                ('Amps using Volts and Resistance', self.form_ampsvr),
                ('Amps using Watts and Volts', self.form_ampswv),
                ('Amps using Watts and Resistance', self.form_ampswr),
                ('Resistance using Volts and Amps', self.form_resisva),
                ('Resistance using Watts and Amps', self.form_resiswa),
                ('Resistance using Volts and Watts', self.form_resisvw),
                ('Watts using Volts and Amps', self.form_wattsva),
                ('Watts using Resistance and Amps', self.form_wattsra),
                ('Watts using Volts and Resistance', self.form_wattsvr),
                #}}}_________________________________________________________________________________________
            ]
        )

    def form_voltsar(self):
            argsOut = ['Volts Using Amps and Resistance', 'Enter Amps', 'Enter Resistance']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (result, self.pluralize(result, 'Volt'))
            
    def form_voltswa(self):
            argsOut = ['Volts using Watts and Amps', 'Enter Watts', 'Enter Amps']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Volt'))
            
    def form_voltswr(self):
            argsOut = ['Volts using Watts and Resistance', 'Enter Watts', 'Enter Resistance']
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] * argsIn[1]) 
            return (result, self.pluralize(result, 'Volt'))
            
    def form_ampsvr(self):
            argsOut = ['Amps using Volts and Resistance', 'Enter Volts', 'Enter Resistance']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Amp'))
            
    def form_ampswv(self):
            argsOut = ['Amps using Watts and Volts', 'Enter Watts', 'Enter Volts']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Amp'))
            
    def form_ampswr(self):
            argsOut = ['Amps using Watts and Resistance', 'Enter Watts', 'Enter Resistance']
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] / argsIn[1])
            return (result, self.pluralize(result, 'Amp'))
            
    def form_resisva(self):
            argsOut = ['Resistance using Volts and Amps', 'Enter Volts', 'Enter Amps']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Resistance'))
            
    def form_resiswa(self):
            argsOut = ['Resistance using Watts and Amps', 'Enter Watts', 'Enter Amps']
            argsIn = self.prompt(argsOut)
            result = sqrt(argsIn[0] / (argsIn[1] ** 2))
            return (result, self.pluralize(result, 'Resistance'))
            
    def form_resisvw(self):
            argsOut = ['Resistance using Volts and Watts', 'Enter Volts', 'Enter Watts']
            argsIn = self.prompt(argsOut)
            result = (argsIn[0] ** 2) / argsIn[1]
            return (result, self.pluralize(result, 'Resistance'))
            
    def form_wattsva(self):
            argsOut = ['Watts using Volts and Amps', 'Enter Volts', 'Enter Amps']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (result, self.pluralize(result, 'Watt'))
            
    def form_wattsra(self):
            argsOut = ['Watts using Resistance and Amps', 'Enter Resistance', 'Enter Amps']
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * (argsIn[1] ** 2)
            return (result, self.pluralize(result, 'Watt'))
            
    def form_wattsvr(self):
            argsOut = ['Watts using Volts and Resistance', 'Enter Volts', 'Enter Resistacne']
            argsIn = self.prompt(argsOut)
            result = (argsIn[0] ** 2) / argsIn[1]
            return (result, self.pluralize(result, 'Watt'))
            
        

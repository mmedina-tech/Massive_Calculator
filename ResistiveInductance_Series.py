#!/usr/bin/env python
from FormulaBase import *
from collections import OrderedDict

class ResistiveInductance_Series(FormulaBase):
	def __init__(self, name):
            super(ResistiveInductance_Series, self).__init__(name)
            self.name = name
    
            self.function_list = OrderedDict(
            [
            ('Total Volts using Resistor Volts and Inductor Volts', self.form_tVolts),
            ('Total Volts using Total Amps and Impedance', self.form_tVolts2),
            ('Total Volts using Volt Amps and Total Amps', self.form_tVolts3),
            ('Total Volts using Resistor Volts and Power Factor', self.form_tVolts4),
            ('Power Factor using Resistance and Impedance', self.form_powerFactor),
            ('Power Factor using Watts and Volt Amps', self.form_powerFactor2),
            ('Power Factor using Resistor Volts and Total Volts', self.form_powerFactor3)
            ]
	)
	
        def form_tVolts(self):
            title = 'Total Volts using Resistor Volts and Inductor Volts'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Inductor Volts'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = sqrt((argsIn[0] ** 2) + (argsIn[1] ** 2))
            return (result, self.pluralize(result, 'Total Volt'))
		
	def form_tVolts2(self):
            title = 'Total Volts using Total Amps and Impedance'
            arg1 = 'Enter Total Amps'
            arg2 = 'Enter Impedance'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] * argsIn[1]
            return (result, self.pluralize(result, 'Total Volt'))
		
	def form_tVolts3(self):
            title = 'Total Volts using Volt Amps and Total Amps'
            arg1 = 'Enter Volt Amps'
            arg2 = 'Enter Total Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0]/argsIn[1]
            return (result, self.pluralize(result, 'Total Volt'))
		
	def form_tVolts4(self):
            title = 'Total Volts using Resistor Volts and Power Factor'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Power Factor'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Total Volt'))
		
	def form_powerFactor(self):
            title = 'Power Factor using Resistance and Impedance'
            arg1 = 'Enter Resistance'
            arg2 = 'Enter Impedance'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Power Factor'))
	
	def form_powerFactor2(self):
            title = 'Power Factor using Watts and Volt Amps'
            arg1 = 'Enter Watts'
            arg2 = 'Enter Volt Amps'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn [0] / argsIn[1]
            return (result, self.plurarlize(result, 'Power Factor'))
		
	def form_powerFactor3(self):
            title = 'Power Factor using Resistor Volts and Total Volts'
            arg1 = 'Enter Resistor Volts'
            arg2 = 'Enter Total Volts'
            argsOut = [title, arg1, arg2]
            argsIn = self.prompt(argsOut)
            result = argsIn[0] / argsIn[1]
            return (result, self.pluralize(result, 'Power Factor'))


#!/usr/bin/python

from FormulaBase import *
from collections import OrderedDict

class Budget(FormulaBase):
    def __init__(self, name):
        super(Budget, self).__init__(name)
        self.name = name
        self.function_list = OrderedDict(
                [
                    ('Monthly Budget', self.form_budgeting)
                ]
            )

    def form_budgeting(self):
        title = 'Budgeting'
        wage = 'Enter Hourly Wage'
        hourly = 'Enter Hours'
        rent = 'Enter Rent/Mortgage Bill'
        cable = 'Enter Cable Bill'
        elect = 'Enter Electricity and Water Bill'
        telephone = 'Enter Telephone Bill'
        groceries = 'Enter Groceries Bill'
        health = "Enter Health Care Insurance"
        clothing = 'Enter Clothing expenses'
        car = 'Enter Car Expenses (Insurance, Maintenance, and Gas)'
        cos = 'Enter Cost of Supervision'
        program = 'Enter Program Cost'
        rec = 'Enter Recreation Cost'
        other = 'Enter Other Expenses'
        argsOut = [title, wage, hourly, rent, cable, elect, telephone, groceries, health, clothing, car, cos, program, rec, other]
        argsIn = self.prompt(argsOut)
        income = (argsIn[0] * argsIn[1])
        expenses = (argsIn[2] + argsIn[3] + argsIn[4] + argsIn[5] + argsIn[6] + argsIn[7] + argsIn[8] + argsIn[9] + argsIn[10] + argsIn[11] + argsIn[12] + argsIn[13])
        result = income - expenses
        return ('$'+self.prec2(result), self.pluralize(result, 'Dollar'))

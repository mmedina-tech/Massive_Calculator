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
        income = 'Enter Monthly Income'
        rent = 'Enter Rent or Mortgage Bill'
        cable = 'Enter Cable Bill'
        elect = 'Enter Electricity and Water Bill'
        telephone = 'Enter Telephone Bill'
        groceries = 'Enter Groceries Bill'
        argsOut = [title, income, rent, cable, elect, telephone, groceries]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] - (argsIn[1] + argsIn[2] + argsIn[3] + argsIn[4] + argsIn[5])
        return (result, self.pluralize(result, 'Dollar'))

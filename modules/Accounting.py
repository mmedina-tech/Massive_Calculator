#!/usr/bin/python
#SYNOPSIS: Module for Massive Calculator Terminal
# 
# Accounting.py
#
# Author: mmedina
# Date: Mon 29 Jun 2020 08:40:33 AM PDT
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or 
# (at your option) any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABLILITY of FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You Should have recieved a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
# This Module is for Accounting Formulas 

from FormulaBase import *

class Accounting(FormulaBase):
    def __init__(self, name):
        """
        name -- Accounting
        """
        super(Accounting, self).__init__(name)
        self.name = name

#{{{___ Function Titles _____________________________________________________________________________

        self.function_strings = {
            1 : 'The Equity Ratio',
            2 : 'Trend Percentage',
            3 : 'Current Ratio',
            4 : 'Gross Margin Percentage',
            5 : 'Gross Margin Ratio using Gross Profit and Revenue',
            6 : 'Inventory Turn-Over Ratio',
            7 : 'The Quick Ratio using Cash, Cash Equivalants, Short Term Investments, etc.',
            8 : 'Accounts Receivable Turn-Over',
            9 : "Number of Days' Sales in Accounts Receivable",
            10 : 'Rate of Return on Operating Assets',
            11 : 'Total Asset Turn-Over',
            12 : 'Earnings Per Share and Price Earnings Ratio',
            13 : 'Dividend Yield on Common Stock',
            14 : 'Payout Ratio on Common Stock',
            15 : 'The Quick Ratio using Total Current Assets, Inventory, Prepaid Expenses, and Current Liabilities',
            16 : 'Gross Margin Ratio using Revenue and Cost of Goods Sold',
            17 : 'Company Equity',
            18 : 'Cash to Equity',
        }
#}}}_________________________________________________________________________________________

#{{{___ Function List _____________________________________________________________________________

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.equity),
                (self.function_strings[2], self.trend),
                (self.function_strings[3], self.current),
                (self.function_strings[4], self.gross_margin),
                (self.function_strings[5], self.gross_margin2),
                (self.function_strings[6], self.inventory),
                (self.function_strings[7], self.quick),
                (self.function_strings[8], self.accounts),
                (self.function_strings[9], self.number),
                (self.function_strings[10], self.rate),
                (self.function_strings[11], self.total_asset),
                (self.function_strings[12], self.per_share),
                (self.function_strings[13], self.dividend),
                (self.function_strings[14], self.payout),
                (self.function_strings[15], self.quick2),
                (self.function_strings[16], self.gross_margin3),
                (self.function_strings[17], self.comp_equity),
                (self.function_strings[18], self.cash2equity),
            ]
        )
#}}}_________________________________________________________________________________________

#{{{___ Function Inputs _____________________________________________________________________________

        self.functionInputs = {
            self.function_strings[1] :OrderedDict(
                    [
                            ('number_input', 'Stockholders Equity (input): '),
                            ('number_input2', 'Total Equity (input): ')
                    ]
            ),
            self.function_strings[2]:OrderedDict(
                    [
                            ('number_input', 'Current Year Amount (input): '),
                            ('number_input2', 'Base Year Amount (input): ')
                    ]
            ),
            self.function_strings[3]:OrderedDict(
                    [
                            ('number_input', 'Current Assets (input): '),
                            ('number_input2', 'Current Liabilities (input): ')
                    ]
            ),
            self.function_strings[4]:OrderedDict(
                    [
                            ('number_input', 'Cost of Goods Sold (input): '),
                            ('number_input2', 'Revenue (input): ')
                    ]
            ),
            self.function_strings[5]:OrderedDict(
                    [
                            ('number_input', 'Gross Profit (input): '),
                            ('number_input2', 'Revenue (input): ')
                    ]
            ),
            self.function_strings[6]:OrderedDict(
                    [
                            ('number_input', 'Cost of Goods Sold (input): '),
                            ('number_input2', 'Average Inventory (input): ')
                    ]
            ),
            self.function_strings[7]:OrderedDict(
                    [
                            ('number_input', 'Cash (input): '),
                            ('number_input2', 'Cash Equivalants (input): '),
                            ('number_input3', 'Short Term Investments (input): '),
                            ('number_input4', 'Current Receivables (input): '),
                            ('number_input5', 'Current Liabilities (input): ')
                    ]
            ),
            self.function_strings[8]:OrderedDict(
                    [
                            ('number_input', 'Net Credit Sales (input): '),
                            ('number_input2', 'Average Accounts (input): ')
                    ]
            ),
            self.function_strings[9]:OrderedDict(
                    [
                            ('number_input', 'Sales (input): '),
                            ('number_input2', 'Account Receivable (input): ')
                    ]
            ),
            self.function_strings[10]:OrderedDict(
                    [
                            ('number_input', 'Net Income (input): '),
                            ('number_input2', 'Operating Assets (input): ')
                    ]
            ),
            self.function_strings[11]:OrderedDict(
                    [
                            ('number_input', 'Net Sales (input): '),
                            ('number_input2', 'Average Total Assets (input): ')
                    ]
            ),
            self.function_strings[12]:OrderedDict(
                    [
                            ('number_input', 'Income Available to Common Stockholders (input): '),
                            ('number_input2', 'Weighted-Average Number of Common Shares Outstanding (input): ')
                    ]
            ),
            self.function_strings[13]:OrderedDict(
                    [
                            ('number_input', 'Dividend Per Share of Common Stock (input): '),
                            ('number_input2', 'Current Market Price per Share (input): ')
                    ]
            ),
            self.function_strings[14]:OrderedDict(
                    [
                            ('number_input', 'Dividend per Share of Common Stock (input): '),
                            ('number_input2', 'Earnings per Share (EPS) (input): ')
                    ]
            ),
            self.function_strings[15]:OrderedDict(
                    [
                            ('number_input', 'Total Current Assets (input): '),
                            ('number_input2', 'Inventory (input): '),
                            ('number_input3', 'Prepaid Expenses (input): '),
                            ('number_input4' , 'Current Liabilities (input): ')
                    ]
            ),
            self.function_strings[16]:OrderedDict(
                    [
                            ('number_input', 'Revenue (input): '),
                            ('number_input2', 'Cost of Goods Sold (input): ')
                    ]
            ),
            self.function_strings[17]:OrderedDict(
                    [
                        ('number_input', 'Cash Amount Asking (input): '),
                        ('number_input2', 'Amount of Equity Given (input): '),
                    ]
            ),
            self.function_strings[18]:OrderedDict(
                    [
                        ('number_input', 'Company Worth (input): '),
                        ('number_input2', 'Buy in Amount (input): '),
                    ]
            ),
        }
#}}}_________________________________________________________________________________________

#{{{___ Show Formula _____________________________________________________________________________

        self.formula_list = {
            self.function_strings[1]:{
                'Formula:<br>': "Stockholders Equity / Total Equity"
            },
            self.function_strings[2]:{
                'Formula:<br>': 'Current Year Amount / Base Year Amount'
            },
            self.function_strings[3]:{
                'Formula:<br>': 'Current Assets / Current Liabilities'
            },
            self.function_strings[4]:{
                'Formula:<br>': '((Cost of Goods Sold - Revenue) / Revenue)* 100'
            },
            self.function_strings[5]:{
                'Formula:<br>': 'Gross Profit / Revenue'
            },
            self.function_strings[6]:{
                'Formula:<br>': 'Cost of Goods Sold / Average Inventory'
            },
            self.function_strings[7]:{
                'Formula:<br>': '(Cash + Cash Equivalants + Short Term Investments + Current Receivables) / Current Liabilities'
            },
            self.function_strings[8]:{
                'Formula:<br>': 'Net Credit Sales / Average Accounts'
            },
            self.function_strings[9]:{
                'Formula:<br>': '365 / (Sales / Account Receivable)'
            },
            self.function_strings[10]:{
                'Formula:<br>': 'Net Income / Operating Assets'
            },
            self.function_strings[11]:{
                'Formula:<br>': 'Net Sales / Average Total Assets'
            },
            self.function_strings[12]:{
                'Formula:<br>': 'Income Available to Common Stockholders / Weighted-Average Number of Common Shares Outstanding'
            },
            self.function_strings[13]:{
                'Formula:<br>': 'Dividend Per Share of Common Stock / Current Market Price per Share'
             },
            self.function_strings[14]:{
                'Formula:<br>': 'Dividend per Share of Common Stock / Earnings Per Share (EPS)'
            },
            self.function_strings[15]:{
                'Formula:<br>': '(Total Current Assets - Inventory - Prepaid Expenses) / Current Liabilities'
            },
            self.function_strings[16]:{
                'Formula:<br>': '(Revenue - Cost of Goods Sold) / Cost of Goods Sold'
            },
            self.function_strings[17]:{
                'Formula:<br>': 'Cash Amount Asking / (Amount of Equity Given * (10^-2))'
            },
            self.function_strings[18]:{
                'Formula:<br>': 'Company Worth / Amount Put In'
            },
        }
#}}}_________________________________________________________________________________________
        
#{{{___ Formula Functions _____________________________________________________________________________

    def equity_ratio(self):
        """
        The Equity Ratio
        """
        title = self.function_strings[1]
        stock_equity = "Enter Stockholder's Equity"
        total_equity = "Enter Total Equity"
        argsOut = [title, stock_equity, total_equity]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Equity'))

    def trend_percent(self):
        """
        Trend Percentage
        """
        title = self.function_strings[2]
        current_amount = 'Enter Current Year Amount'
        current_liability = 'Enter Current Liabilities'
        argsOut = [title, current_amount, current_liability]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return ('%'+self.prec2(result), self.pluralize(result, 'Trend Percentage'))

    def current_ratio(self):
        """
        Current Ratio
        """
        title = self.function_strings[3]
        current_assets = 'Enter Current Assets'
        current_liability = 'Enter Current Liabilities'
        argsOut = [title, current_assets, current_liability]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Current Ratio'))

    def gross_margin(self):
        """
        Gross Margin Percentage
        """
        title = self.function_strings[4]
        cost = 'Enter cost of goods sold'
        revenue = 'Enter revenue'
        argsOut = [title, cost, revenue]
        argsIn = self.prompt(argsOut)
        result = ((argsIn[0] - argsIn[1]) / argsIn[1]) * 100
        return ('%'+self.prec2(result), self.pluralize(result, 'Gross Margin Percentage'))

    def gross_ratio(self):
        """
        Gross Margin Ratio
        """
        title = self.function_strings[5]
        gross_profit = 'Enter Gross Profit'
        revenue = 'Enter Revenue'
        argsOut = [title, gross_profit, revenue]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Gross Margin Ratio'))

    def inventory(self):
        """
        Inventory Turn-Over Ratio
        """
        title = self.function_strings[6]
        cost = 'Enter Cost of Goods Sold'
        average = 'Enter Average Inventory'
        argsOut = [title, cost, average]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Inventory Turn-Over Ratio'))

    def quick(self):
        """
        The Quick Ratio
        """
        title = self.function_strings[7]
        cash = 'Enter Cash'
        cash_eq = 'Enter Cash Equivalents'
        short_term = 'Enter Short Term Investments'
        current_recieve = 'Enter Current Recievables'
        current_liability = 'Enter Current Liabilities'
        argsOut = [title, cash, cash_eq, short_term, current_recieve, current_liability]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] + argsIn[1] + argsIn[2] + argsIn[3]) / argsIn[4]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Quick Ratio'))

    def accounts_receive(self):
        """
        Accounts Recievable Turn-Over
        """
        title = self.function_strings[8]
        net_credit = 'Enter Net Credit Sales'
        avg_accounts = 'Enter Average Accounts'
        argsOut = [title, net_credit, avg_accounts]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Accounts Receivable'))

    def number_days(self):
        """
        Number of Days Sales in Accounts Recievable
        """
        title = self.function_strings[9]
        sales = 'Enter Sales'
        accounts = 'Enter Account Recievables'
        argsOut = [title, sales, accounts]
        argsIn = self.prompt(argsOut)
        result = 365 / (argsIn[0] / argsIn[1])
        return (result, self.pluralize(result, 'Viable Days'))

    def return_rate(self):
        """
        Rate of Return on Operating Assets
        """
        title = self.function_strings[10]
        net_income = 'Enter Net Income'
        op_assets = 'Enter Operating Assets'
        argsOut = [title, net_income, op_assets]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Rate of Return'))
        
    def total_asset(self):
        """
        Total Asset Turn-Over
        """
        title = self.function_strings[11]
        net_sales = 'Enter Net Sales'
        avg_total_assets = 'Enter Average Total Assets'
        argsOut = [title, net_sales, avg_total_assets]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsin[1]
        return (result, self.pluralize(result, title))

    def per_share(self):
        """
        Earnings Per Share and Price Earnings Ratio
        """
        title = self.function_strings[12]
        income = 'Enter Income Available to Common Stockholders'
        wgt_avg = 'Enter Weighted-Average Number of Common Shares Outstanding'
        argsOut = [title, income, wgt_avg]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Earnings Per Share'))

    def dividend(self):
        """
        Dividend Yield on Common Stock
        """
        title = self.function_strings[13]
        dividend_per_share = 'Enter Dividend Per Share on Common Stock'
        market = 'Enter Current Market Price per Share'
        argsOut = [title, dividend_per_share, market]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Dividend Yield'))

    def payout(self):
        """
        Payout Ratio on Common Stock
        """
        title = self.function_strings[14]
        per_share = 'Enter Dividend Per Share on Common Stock'
        eps = 'Enter Earnings Per Share (EPS)'
        argsOut = [title, per_share, eps]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Payout Ratio'))

    def quick2(self):
        """
        The Quick Ratio 2
        """
        title = self.function_strings[15]
        total_current = 'Enter Total Current Asstes'
        inventory = 'Enter Inventory'
        prepaid = 'Enter Prepaid Expenses'
        liability = 'Enter Current Liabilities'
        argsOut = [title, total_current, inventory, prepaid, liability]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] - argsIn[1] - argsIn[2]) / argsIn[3]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Quick Ratio'))

    def gross_margin3(self):
        """
        Gross Margin Ratio using Revenue and Cost of Goods Sold
        """
        title = self.function_strings[16]
        revenue = 'Enter Revenue'
        cost_goods = 'Enter Cost of Goods Sold'
        argsOut = [title, revenue, cost_goods]
        argsInt = self.prompt(argsOut)
        result = (argsIn[0] - argsIn[1]) / argsIn[2]
        return (result, self.pluralize(result, 'Gross Margin'))

    def cash2equity(self):
        """
        Cash to Equity
        """
        title = self.function_strings[17]
        cmpy_worth = 'Enter Company Worth'
        in_amount = 'Enter Buy in Amount'
        argsOut = [title, cmpy_worth, in_amount]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return ('%'+self.prec2(result), self.pluralize(result, 'Equity'))

    def comp_equity(self):
        """
        Company Equity
        """
        title = self.function_strings[18]
        cash = 'Enter Cash Amount Asking'
        equity = 'Enter Amount of Equity Given'
        argsOut = [title, cash, equity]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] / argsIn[1])
        return ('$'+self.prec2(result), self.pluralize(result, 'Company Valuation'))

    #}}}_________________________________________________________________________________________
    

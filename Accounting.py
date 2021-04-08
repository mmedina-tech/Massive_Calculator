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
        self.function_list = OrderedDict(
                [
                    ('The Equity Ratio', self.equity_ratio),
                    ('Trend Percentage', self.trend_percent),
                    ('Current Ratio', self.current_ratio),
                    ('Gross Margin Percentage', self.gross_margin),
                    ('Gross Margin Ratio', self.gross_ratio),
                    ('Inventory Turn-Over Ratio', self.inventory),
                    ('The Quick Ratio', self.quick),
                    ('Accounts Recievable Turn-Over', self.accounts_recieve),
                    ('Number of Days Sales in Accounts Recievable', self.number_days),
                    ('Rate of Return on Operating Assets', self.return_rate),
                    ('Total Asset Turn-Over', self.total_asset),
                    ('Earnings Per Share and Price Earnings Ratio', self.per_share),
                    ('Dividend Yield on Common Stock', self.dividend),
                    ('Payout Ratio on Common Stock', self.payout),
                    ('The Quick Ratio using Total Current Assets, Inventory, Prepaid Expenses, and Current Liabilities', self.quick2),
                    ('Gross Margin Ratio using Revenue and Cost of Goods Sold', self.gross_margin3),
                    ('Company Equity', self.comp_equity),
                    ('Cash to Equity', self.cash2equity),
                ]
            )

    def equity_ratio(self):
        """
        The Equity Ratio
        """
        title = "The Equity Ratio"
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
        title = 'Trend Percentage'
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
        title = 'Current Ratio'
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
        title = 'Gross Margin Percentage'
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
        title = 'Gross Margin Ratio'
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
        title = 'Inventory Turn-Over Ratio'
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
        title = 'The Quick Ratio'
        cash = 'Enter Cash'
        cash_eq = 'Enter Cash Equivalents'
        short_term = 'Enter Short Term Investments'
        current_recieve = 'Enter Current Recievables'
        current_liability = 'Enter Current Liabilities'
        argsOut = [title, cash, cash_eq, short_term, current_recieve, current_liability]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] + argsIn[1] + argsIn[2] + argsIn[3]) / argsIn[4]
        return (self.prec2(result)+'/1', self.pluralize(result, 'Quick Ratio'))

    def accounts_recieve(self):
        """
        Accounts Recievable Turn-Over
        """
        title = 'Accounts Recievable Turn-Over'
        net_credit = 'Enter Net Credit Sales'
        avg_accounts = 'Enter Average Accounts'
        argsOut = [title, net_credit, avg_accounts]
        argsIn = self.prompt(argsOut)
        result = argsIn[0] / argsIn[1]
        return (result, self.pluralize(result, 'Accounts Recievable'))

    def number_days(self):
        """
        Number of Days Sales in Accounts Recievable
        """
        title = 'Number of Days Sales in Accounts Recievable'
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
        title = 'Rate of Return on Operating Assets'
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
        title = 'Total Asset Turn-Over'
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
        title = 'Earnings Per Share and Price Earnings Ratio'
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
        title = 'Dividend Yield on Common Stock'
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
        title = 'Payout Ratio on Common Stock'
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
        title = 'The Quick Ratio using Total Current Assets, Inventory, Prepaid Expenses, and Current Liabilities'
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
        title = 'Gross Margin Ratio using Revenue and Cost of Goods Sold'
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
        title = 'Cash to Equity'
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
        title = 'Company Equity'
        cash = 'Enter Cash Amount Asking'
        equity = 'Enter Amount of Equity Given'
        argsOut = [title, cash, equity]
        argsIn = self.prompt(argsOut)
        result = (argsIn[0] / argsIn[1])
        return ('$'+self.prec2(result), self.pluralize(result, 'Company Valuation'))

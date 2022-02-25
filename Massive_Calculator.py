#!/usr/bin/python
#
# Author: Marcus Medina
# Co-Author: Gail Long
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You Should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import os
from collections import OrderedDict
from importlib import import_module
from modules.FormulaBase import *
from modules.allowances import *
from load_screen import *


# Sets up prompt strings
prompts = {
    'categoryprompt' : "\nEnter Category - 'h' for Help or 'q' to Quit: ",
    'formulaprompt' : "\nEnter Formula or 'b' to go back, or 'q' to Quit: ",
    'continueprompt' : 'Press Enter to Continue'
        }
# strings for titles, exit messages, error messages, and help strings
strings = {
    'mainmenutitle' : '\nThe Massive Calculator\n',
    'endnote' : '\nThank you for using the Massive Calculator\n',
    'cathelpstring' : '\nPress the number of the formula or conversion you want\n',
    'tryagain' : 'Please Try Again'
        }
# Category Module list for Menu list
list_category = {
    'Acceleration': 'Acceleration',
    'Accounting': 'Accounting',
    'Area': 'Area',
    'Astronomic Units': 'Astronomic_units',
    'Budget': 'Budget',
    'Culinary': 'Culinary',
    'Energy or Work': 'Energy_or_Work',
    'Fuel Economy': 'Fuel_Economy',
    'GED Practice': 'GED_Practice',
    'Imperial to Imperial': 'Imperial_to_Imperial',
    'Imperial to Metric': 'Imperial_to_Metric',
    'Light': 'Light',
    'Maritime Measurements': 'Maritime_Measurements',
    'Mass': 'Mass',
    'Metric To Imperial': 'Metric_to_Imperial',
    'Ohms Law': 'OhmsLaw',
    'Physical Fitness': 'Physical_Fitness',
    'Plane Angle': 'PlaneAngle',
    'Power': 'Power',
    'Pressure': 'Pressure',
    'Resistive Capacitance (Parallel)': 'Resistive_Capacitive_Parallel',
    'Resistive Capacitance (Series)': 'Resistive_Capacitive_Series',
    'Resistive Inductance (Parallel)': 'Resistive_Inductive_Parallel',
    'Resistive Inductance (Series)': 'Resistive_Inductive_Series',
    'Torque': 'Torque',
    'Velocity': 'Velocity',
}

objects = {}
menu = {}
list_category = sorted(list_category.items())
list_category = OrderedDict(list_category)

# log function


def logme(msg):
    if not os.path.exists("Log"):
        os.makedirs("Log")
    fp = open('Log/my.log', 'a')
    fp.write('\n'+str(msg)+'\n\n')
    fp.close()

allowances = allowances()

#  Prints the Menus
def print_menu(list_category):
    os.system('clear')
    print strings['mainmenutitle']
    cnt = 1
    for line in list_category.keys():
        print '{}. {}'.format(cnt, line)
        cnt += 1
        allowances.cat_allowances.append(line)

# Prints the help message
def print_help():
    print strings['cathelpstring']
    raw_input(prompts['continueprompt'])

# Category Selection
def category_prompt():

    loading_screen(.1)
    # Loops until a proper selection is made
    while True:
        print_menu(list_category)
        prompt = raw_input(prompts['categoryprompt'])

        # checks to make sure that the input is allowed
        logme(prompt)
        if prompt.isalpha():

            if prompt in allowances.quit_allowances:
                print(strings['endnote'])
                exit()

            if prompt in allowances.help_allowances:
                print_help()
                continue

            print 'try again'
            continue

        elif not prompt.isdigit():
            print 'try again'
            continue

        # prompt could be a number or a letter
        # call won't work if it's a letter
        category = int(prompt) - 1

        logme(category)
        if category in range(len(list_category.values())):
        # key is a category name string
        # list_category is an ordered dictionary
        # dynamically imports the selected category
            key = list_category.keys()[category]
            logme(key)
            try:
                if objects[list_category[key]] is None:
                        throw(NameError)
            except(NameError, KeyError) as e:
                subkey = list_category[key]
                logme(subkey)

                ret = import_module("modules."+list_category[key])
                logme(ret)
                try:
                    ret = import_module("modules."+list_category[key])
                    logme(ret)
                except(Exception) as e:
                    logme(e)
                    print e; exit()

                submod = getattr(ret, subkey)
                logme(submod)

                objects[key] = submod(subkey)
                logme(objects[key])
            finally:
                cnt = 0
                for funct in objects[key].function_list:
                    print '\n{} {}'.format(cnt, funct)
                    cnt += 1
                formula_prompt(objects[key])

        else:
            print 'try again'
            continue

# Formula Selection of Associated Category
def formula_prompt(cat):
    cat.function_list = sorted(cat.function_list.items())
    cat.function_list = OrderedDict(cat.function_list)

    while True:
    # Loops until proper input is taken in
        print_menu(cat.function_list)
        prompt = raw_input(prompts['formulaprompt'])
        logme(prompt)

        # checks input against letters and special characters
        if prompt.isalpha():

            if prompt in allowances.quit_allowances:
                logme(prompt)
                print(strings['endnote'])
                exit()

            if prompt in allowances.back_allowances:
                logme(prompt)
                category_prompt()

            logme(prompt)
            print 'try again'
            continue

        elif not prompt.isdigit():
            logme(prompt)
            print 'try again'
            continue


        # If prompt is equal to a string number convert to integer and
        # subtract 1 to handle array offset for formula selection
        runFormula = int(prompt) - 1
        # checks to make sure that the selection is within range of the
        # formula list
        if runFormula in range(len(cat.function_list)):
            promptstr = cat.function_list.keys()[runFormula]
            logme(promptstr)
            try:
                if isinstance(cat.function_list[promptstr], OrderedDict):
                    logme(formula_prompt(cat.function_list[promptstr]))
                    formula_prompt(cat.function_list[promptstr])
                else:
                    # takes in numbers needed for calculation and returns answer
                    try:
                        retval = cat.function_list[promptstr]()
                        logme(retval)
                        print "\nAnswer: {} {}\n".format(retval[0], retval[1])
                        prompt = raw_input(prompts['continueprompt'])
                    # catches errors that are most likely not in the array for the
                    # for loop in the FormulaBase.py
                    except(Exception) as e:
                        logme(e)
                        print "\nThere was an error, please see my.log file"
                        raw_input(prompts['continueprompt'])
            except(Exception) as e:
                logme(e)
                raw_input(prompts['continueprompt'])


# Starts the Category Menu Selection
category_prompt()

print strings['endnote']

#!/usr/bin/python

import os
from collections import OrderedDict
from FormulaBase import *
from importlib import import_module
from allowances import *



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
    'Resistive Capacitance (Parallel)': 'Resistive_Capacitance_Parallel',
    'Resistive Capacitance (Series)': 'Resistive_Capacitive_Series',
    'Resistive Inductance (Parallel)': 'Resistive_Inductive_parallel',
    'Resistive Inductance (Series)': 'Resistive_Inductive_series',
    'Torque': 'Torque',
    'Velocity': 'Velocity',
}

objects = {}
menu = {}
list_category = sorted(list_category.items())
list_category = OrderedDict(list_category)
#print list_category.items()
#exit()

# log function 
def logme(msg):
	fp = open('Log/my.log', 'a')
	fp.write('\n'+msg+'\n\n')
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

    # Loops until a proper selection is made 	
    while True:
        print_menu(list_category)
        prompt = raw_input(prompts['categoryprompt'])
        logme('user input ' + prompt)

        # checks to make sure that the input is allowed 
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

        if category in range(len(list_category.values())):
        # key is a category name string
        # list_category is an ordered dictionary
        # dianamically inmports the selected category 
            key = list_category.keys()[category]
            try:
                if objects[list_category[key]] is None:
                        throw(NameError)
            except(NameError, KeyError) as e:
                subkey = list_category[key]
                
                ret = import_module("modules."+subkey)
                try:
                        ret = import_module("modules."+subkey)
                except(Exception) as e:
                        print e; exit()
                
                submod = getattr(ret, subkey)
                
                objects[key] = submod(subkey)
            finally:
                #print objects[key].functions_list.keys(); exit()
                cnt = 0
                objects[key].function_list = sorted(objects[key].function_list.items())
                objects[key].function_list = OrderedDict(objects[key].function_list)
                for funct in objects[key].function_list.keys():
                    print '\n{} {}'.format(cnt,funct)
                    cnt += 1
    #formula_prompt(objects[key].function_list[key])
                    formula_prompt(objects[key])
                        
        else:
            print 'try again'
            continue
		
# Formula Selection of Associated Category 
def formula_prompt(cat):

    # Loops until proper input is taken in 
    while True:
        print_menu(cat.function_list)
        prompt = raw_input(prompts['formulaprompt'])

        # checks input against letters and special characters 
        if prompt.isalpha():

            if prompt in allowances.quit_allowances:
                print(strings['endnote'])
                exit()

            if prompt in allowances.back_allowances:
                category_prompt()

            print 'try again'
            continue

        elif not prompt.isdigit():
            print 'try again'
            continue
        

        # If prompt is equal to a string number convert to integer and  
        # subtract 1 to handle array offset for formula selection 
        runFormula = int(prompt) - 1
        # checks to make sure that the selection is within range of the 
        # formula list
        if runFormula in range(len(cat.function_list)):
            promptstr = cat.function_list.keys()[runFormula]
            logme('I got the Function List: ' + str(cat.function_list[promptstr]))
            try:
                if isinstance(cat.function_list[promptstr], OrderedDict):
                    formula_prompt(cat.function_list[promptstr])
                else:
                    # takes in numbers needed for calculation and returns answer 
                    try:
                        logme('I got the PromptStr ' + str(cat.function_list[promptstr]))
                        retval = cat.function_list[promptstr]()
                        #logme('I got the RetVal ' + str(retval))
                        print "\nAnswer: {} {}\n".format(retval[0], retval[1])
                        logme('After Print cat.function_list')
                        prompt = raw_input(prompts['continueprompt'])
                    # catches errors that are most likely not in the array for the 
                    # for loop in the FormulaBase.py
                    except(Exception) as e:
                        print "\nThere was an error, please see my.log file"
                        raw_input(prompts['continueprompt'])
                        logme("Error: {}".format(e))
            except(Exception) as e:
                print "Error: {}".format(e)
                raw_input(prompts['continueprompt'])

		
# Starts the Category Menu Selection 
category_prompt()

print strings['endnote']

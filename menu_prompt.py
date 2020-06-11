#!/usr/bin/env python

import os
from collections import OrderedDict
from FormulaBase import *
from importlib import import_module


prompts = {
	'categoryprompt' : "\nEnter Category - 'h' for Help or 'q' to Quit: ",
	'formulaprompt' : "\nEnter Formula or 'b' to go back, or 'q' to Quit: ",
	'continueprompt' : 'Press Enter to Continue'
		}
		
strings = {
	'mainmenutitle' : '\nThe Massive Calculator\n',
	'endnote' : '\nThank you for using the Massive Calculator\n',
	'cathelpstring' : '\nPress the number of the formula or conversion you want\n',
	'tryagain' : 'Please Try Again'
		}

list_category = OrderedDict(
	[
            ('Metric To Imperial', 'Metric_to_Imperial'),
            ('Imperial To Metric', 'Imperial_to_Metric'),
            ('Imperial To Imperial', 'Imperial_to_Imperial'),
            ('Torque', 'Torque'),
            ('Power', 'Power'),
            ('Energy or Work', 'Energy_or_Work'),
            ('Plane Angle', 'PlaneAngle'),
            ('Ohms Law', 'OhmsLaw'),
            ('Resistive Inductance Series', 'ResistiveInductance_Series'),
            ('Budgeting', 'Budgeting')
	]
)

objects = {}
menu = {}

def logme(msg):
	fp = open('my.log', 'a')
	fp.write('\n'+msg+'\n\n')
	fp.close()

class allowances(object):

    def __init__(self):
        self.quit_allowances()
        self.back_allowances()
        self.help_allowances()
        self.cat_allowances()
        self.form_allowances()

    def quit_allowances(self):
        self.quit_allowances = ['q', 'Q']

    def back_allowances(self):
        self.back_allowances = ['b', 'B']

    def help_allowances(self):
        self.help_allowances = ['h', 'H']

    def cat_allowances(self):
        self.cat_allowances = []

    def form_allowances(self):
        self.form_allowances = []

allowances = allowances()

def print_menu(list_category):
    os.system('clear')
    print strings['mainmenutitle']
    cnt = 1
    for line in list_category.keys():
        print '{}. {}'.format(cnt, line)
        cnt += 1

def print_help():
    print strings['cathelpstring']
    raw_input(prompts['continueprompt'])
        
def category_prompt():

	
    while True:
        print_menu(list_category)
        prompt = raw_input(prompts['categoryprompt'])
        #logme('user input ' + prompt)


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
            key = list_category.keys()[category]
            try:
                if objects[list_category[key]] is None:
                        throw(NameError)
            except(NameError, KeyError) as e:
                subkey = list_category[key]
                
                ret = import_module(list_category[key])
                try:
                        ret = import_module(list_category[key])
                except(Exception) as e:
                        print e; exit()
                
                submod = getattr(ret, subkey)
                
                objects[key] = submod(subkey)
            finally:
                #print objects[key].functions_list.keys(); exit()
                #logme(repr(objects[key].functions_list.keys()))
                cnt = 0
                for funct in objects[key].function_list.keys():
                    print '\n{} {}'.format(cnt, funct)
                    cnt += 1
    #formula_prompt(objects[key].function_list[key])
                    formula_prompt(objects[key])
                        
        else:
            print 'try again'
            continue
		
def formula_prompt(cat):


    while True:
        print_menu(cat.function_list)
        prompt = raw_input(prompts['formulaprompt'])

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
        

        runFormula = int(prompt) -1
        #for c in cat.function_list:
        #	print c
        #exit()
        if runFormula in range(len(cat.function_list)):
            promptstr = cat.function_list.keys()[runFormula]
        #logme('I got the Function List: ' + str(cat.function_list[promptstr]))
            try:
                if isinstance (cat.function_list[promptstr], OrderedDict):
                         formula_prompt(cat.function_list[promptstr])
                else:
                #logme('I got the PromptStr ' + cat.function_list[promptstr])
                    retval = cat.function_list[promptstr]()
                #logme('I got the RetVal ' + retval)
                    print "\nAnswer: {} {}\n".format(retval[0], retval[1])
                #logme('After Print cat.function_list')
                    prompt = raw_input(prompts['continueprompt'])
            except(Exception) as e:
                    print e

		
#os.system('clear')
category_prompt()

#os.system('clear')

print strings['endnote']

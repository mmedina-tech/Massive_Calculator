#!/usr/bin/python
# SYNOPSIS: loading screen using python
# 
# load_screen.py
#
# Author: Marcus Medina
# Date: Sat 02 Oct 2021 12:43:04 AM PDT
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
# This is a git push/pull test
#
#
#

import os
import time
import random
import sys


def loading_bar(seconds, timing):
    for loading in range(0, seconds+1):
        precent = (loading * 5)
        print "Loading...["+("#" * loading*2)+"] " + str(precent) + "%"
        print "\n"
        time.sleep(timing)
        os.system('cls' if os.name == 'nt' else 'clear')


def loading_screen(seconds):
    cwd = os.getcwd()
    screens = open(cwd+"/screens.txt", 'r')
    for lines in screens:
        print lines
        time.sleep(seconds)
        os.system('clear')
    screens.close()


os.system('cls' if os.name == 'nt' else 'clear')

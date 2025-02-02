#!/usr/bin/python
# SYNOPSIS: class for allowable strings
#
# allowances.py
#
# Author: Marcus Medina,,,
# Date: Wed 08 Sep 2021 04:50:29 PM PDT
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
#
#

# Allowances class for allowable inputs other than numbers
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

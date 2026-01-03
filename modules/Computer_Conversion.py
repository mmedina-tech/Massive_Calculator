#!/usr/bin/env python3
#
# Computer_Conversion.py
#
# Computer unit conversions.
#

from .FormulaBase import *


class Computer_Conversion(FormulaBase):
    def __init__(self, name):
        super(Computer_Conversion, self).__init__(name)
        self.name = name

        self.function_strings = {
            1: 'Bits to Bytes',
            2: 'Bytes to Bits',
            3: 'Bytes to Kilobytes',
            4: 'Kilobytes to Bytes',
            5: 'Kilobytes to Megabytes',
            6: 'Megabytes to Kilobytes',
            7: 'Megabytes to Gigabytes',
            8: 'Gigabytes to Megabytes',
            9: 'Gigabytes to Terabytes',
            10: 'Terabytes to Gigabytes',
        }

        self.function_list = OrderedDict(
            [
                (self.function_strings[1], self.bits_to_bytes),
                (self.function_strings[2], self.bytes_to_bits),
                (self.function_strings[3], self.bytes_to_kilobytes),
                (self.function_strings[4], self.kilobytes_to_bytes),
                (self.function_strings[5], self.kilobytes_to_megabytes),
                (self.function_strings[6], self.megabytes_to_kilobytes),
                (self.function_strings[7], self.megabytes_to_gigabytes),
                (self.function_strings[8], self.gigabytes_to_megabytes),
                (self.function_strings[9], self.gigabytes_to_terabytes),
                (self.function_strings[10], self.terabytes_to_gigabytes),
            ]
        )

        self.functionInputs = {
            self.function_strings[1]: {'number_input': 'Bits (input): '},
            self.function_strings[2]: {'number_input': 'Bytes (input): '},
            self.function_strings[3]: {'number_input': 'Bytes (input): '},
            self.function_strings[4]: {'number_input': 'Kilobytes (input): '},
            self.function_strings[5]: {'number_input': 'Kilobytes (input): '},
            self.function_strings[6]: {'number_input': 'Megabytes (input): '},
            self.function_strings[7]: {'number_input': 'Megabytes (input): '},
            self.function_strings[8]: {'number_input': 'Gigabytes (input): '},
            self.function_strings[9]: {'number_input': 'Gigabytes (input): '},
            self.function_strings[10]: {'number_input': 'Terabytes (input): '},
        }

        self.formula_list = {
            self.function_strings[1]: {'Formula:<br>': 'Bits / 8'},
            self.function_strings[2]: {'Formula:<br>': 'Bytes * 8'},
            self.function_strings[3]: {'Formula:<br>': 'Bytes / 1024'},
            self.function_strings[4]: {'Formula:<br>': 'Kilobytes * 1024'},
            self.function_strings[5]: {'Formula:<br>': 'Kilobytes / 1024'},
            self.function_strings[6]: {'Formula:<br>': 'Megabytes * 1024'},
            self.function_strings[7]: {'Formula:<br>': 'Megabytes / 1024'},
            self.function_strings[8]: {'Formula:<br>': 'Gigabytes * 1024'},
            self.function_strings[9]: {'Formula:<br>': 'Gigabytes / 1024'},
            self.function_strings[10]: {'Formula:<br>': 'Terabytes * 1024'},
        }

    def bits_to_bytes(self):
        args_out = [self.function_strings[1], 'Bits']
        args_in = self.prompt(args_out)
        result = args_in[0] / 8.0
        return (result, self.pluralize(result, 'Byte'))

    def bytes_to_bits(self):
        args_out = [self.function_strings[2], 'Bytes']
        args_in = self.prompt(args_out)
        result = args_in[0] * 8.0
        return (result, self.pluralize(result, 'Bit'))

    def bytes_to_kilobytes(self):
        args_out = [self.function_strings[3], 'Bytes']
        args_in = self.prompt(args_out)
        result = args_in[0] / 1024.0
        return (result, self.pluralize(result, 'Kilobyte'))

    def kilobytes_to_bytes(self):
        args_out = [self.function_strings[4], 'Kilobytes']
        args_in = self.prompt(args_out)
        result = args_in[0] * 1024.0
        return (result, self.pluralize(result, 'Byte'))

    def kilobytes_to_megabytes(self):
        args_out = [self.function_strings[5], 'Kilobytes']
        args_in = self.prompt(args_out)
        result = args_in[0] / 1024.0
        return (result, self.pluralize(result, 'Megabyte'))

    def megabytes_to_kilobytes(self):
        args_out = [self.function_strings[6], 'Megabytes']
        args_in = self.prompt(args_out)
        result = args_in[0] * 1024.0
        return (result, self.pluralize(result, 'Kilobyte'))

    def megabytes_to_gigabytes(self):
        args_out = [self.function_strings[7], 'Megabytes']
        args_in = self.prompt(args_out)
        result = args_in[0] / 1024.0
        return (result, self.pluralize(result, 'Gigabyte'))

    def gigabytes_to_megabytes(self):
        args_out = [self.function_strings[8], 'Gigabytes']
        args_in = self.prompt(args_out)
        result = args_in[0] * 1024.0
        return (result, self.pluralize(result, 'Megabyte'))

    def gigabytes_to_terabytes(self):
        args_out = [self.function_strings[9], 'Gigabytes']
        args_in = self.prompt(args_out)
        result = args_in[0] / 1024.0
        return (result, self.pluralize(result, 'Terabyte'))

    def terabytes_to_gigabytes(self):
        args_out = [self.function_strings[10], 'Terabytes']
        args_in = self.prompt(args_out)
        result = args_in[0] * 1024.0
        return (result, self.pluralize(result, 'Gigabyte'))

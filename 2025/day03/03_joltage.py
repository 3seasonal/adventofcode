#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes_03 import JoltageCalculator
from classes_03 import BatteryBank
"""
Advent of Code 2025 - Day 03

- Project: adventofcode
- Year: 2025
- Day: 03
- File: 03_joltage.py
- Description: calulate the combined maximum joltage from a list of power banks
- Author: 3seasonal
- Created: 2025-12-03
- License: MIT (SPDX: MIT)

Notes:
- By no means is this a good example of clean code structure. It is intended to be a quick-and-dirty
  solution to the puzzle, with minimal dependencies.
- If you are reading this. Sorry.

Solution approach:
- use a JoltageCalculator class to manage the input data and provide easy access to parsed instructions
- use a BatteryBank class to track valid and invalid product IDs
- main function to tie everything together and output the result 
"""

__author__ = "3seasonal"
__created__ = "2025-12-03"


def main():
    """
    Main function to execute pid parsing.
    """
    
    # config
    #input_path = os.path.join(os.path.dirname(__file__), '03_sample_input.txt')
    input_path = os.path.join(os.path.dirname(__file__), '03_input.txt')
    sample_output_01 = 357
    sample_output_02 = 3121910778619

    voltage_digits = 12

    # initialize parser and processor
    bb = BatteryBank(input_path)
    jc = JoltageCalculator()

    # process Banks

    while bb.has_banks():
        bank = bb.get_next_bank()
        max_voltage, p = jc.get_max_joltage_from_subbank(voltage_digits, bank)
        jc.accumulate_joltage(int(max_voltage))
        print(f"Bank: {bank}  Max Joltage: {max_voltage}")
    print("Total joltage from all banks:", jc.get_total_joltage()) 
          



if __name__ == "__main__":
    main()
    
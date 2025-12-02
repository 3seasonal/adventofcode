#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes02 import ValidatePIDs as ValidatePIDs
from classes02 import PidParser as PidParser
"""

01_elf_safe.py
Advent of Code 2025 - Day 02

- Project: adventofcode
- Year: 2025
- Day: 02
- File: 02_giftshop_productids.py
- Description: find all of the invalid IDs that appear in the given ranges
- Author: 3seasonal
- Created: 2025-12-02
- License: MIT (SPDX: MIT)

Notes:
- By no means is this a good example of clean code structure. It is intended to be a quick-and-dirty
  solution to the puzzle, with minimal dependencies.
- If you are reading this. Sorry.

Solution approach:
- use a pid_parser class to manage the input data and provide easy access to parsed instructions
- use a pidchecker class to track valid and invalid product IDs
- main function to tie everything together and output the result 
"""

__author__ = "3seasonal"
__created__ = "2025-12-02"


def main():
    """
    Main function to execute pid parsing.
    """
    
    # config
    input_path = os.path.join(os.path.dirname(__file__), '02_sample_input.txt')
    #input_path = os.path.join(os.path.dirname(__file__), '02_input.txt')
    sample_output = 1227775554

    # initialize parser and processor
    pp = PidParser(input_path)
    vpid = ValidatePIDs()

    # process instructions
    print(pp.get_all_ranges())



if __name__ == "__main__":
    main()
    
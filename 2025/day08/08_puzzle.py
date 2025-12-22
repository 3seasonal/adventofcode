#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes_08 import DoTheThing 
from classes_08 import InputParser
"""

- Project: adventofcode
- Year: 2025
- Day: 08
- File: 08_puzzle.py
- Description: {Do all the things for day 08 puzzle.}
- Author: 3seasonal
- Created: 2025-12-22
- License: MIT (SPDX: MIT)

Notes:
- By no means is this a good example of clean code structure. It is intended to be a quick-and-dirty
  solution to the puzzle, with minimal dependencies. Most likely while drunkenly coding at 3am.
- If you are reading this... Sorry.

General solution structure:
- use a parser class to manage the input data and provide easy access to parsed instructions
- use a {DoTheThing} solve the problem logic
- main function to tie everything together and output the result 
"""

__title__ = "Advent of Code 2025 Day 08 Puzzle"
__author__ = "3seasonal"
__created__ = "2025-12-22"


def main():
    """
    Main function to execute pid parsing.
    """
    
    # config
    input_path = os.path.join(os.path.dirname(__file__), '08_sample_input.txt')
    #input_path = os.path.join(os.path.dirname(__file__), '08_input.txt')
    
 
    # initialize parser and processor construtors
    iparse = InputParser(input_path)
    doit = DoTheThing()

    doit.visualise_coords(iparse.get_matrix())

    # process instructions
    
    
    # report results
    
    # validate against sample output if available
        



if __name__ == "__main__":
    main()
    
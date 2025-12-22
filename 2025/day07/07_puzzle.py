#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes_07 import DoTheThing 
from classes_07 import InputParser
"""

- Project: adventofcode
- Year: 2025
- Day: 07
- File: 07_puzzle.py
- Description: Tacheon Beam Simulation Puzzle
- Author: 3seasonal
- Created: 2025-12-07
- License: MIT (SPDX: MIT)

Notes:
- By no means is this a good example of clean code structure. It is intended to be a quick-and-dirty
  solution to the puzzle, with minimal dependencies.
- If you are reading this... Sorry.

General solution structure:
- use a parser class to manage the input data and provide easy access to parsed instructions
- use a {DoTheThing} solve the problem logic
- main function to tie everything together and output the result 
"""

__title__ = "Advent of Code 2025 Day 07 Puzzle"
__author__ = "3seasonal"
__created__ = "2025-12-07"


def main():
    """
    Main function to execute pid parsing.
    """
        
    # config
    #input_path = os.path.join(os.path.dirname(__file__), '07_sample_input.txt')
    input_path = os.path.join(os.path.dirname(__file__), '07_input.txt')
    
    tach = DoTheThing()
    parser = InputParser(input_path)

    print (f"total beams hit: {tach.simulate_tacheon_beams(parser.get_map())}")

    #print (f"total traversals: {tach.start_traverse(parser.get_map())}")
    #print (f"total traversals: {tach.start_calc_values(parser.get_map())}")
    print (f"total traversals: {tach.row_scan(parser.get_map())}")

    



if __name__ == "__main__":
    main()
    
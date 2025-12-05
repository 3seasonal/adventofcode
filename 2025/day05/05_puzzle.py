#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes_05 import InputParser
"""

- Project: adventofcode
- Year: 2025
- Day: 05
- File: 05_puzzle.py
- Description: {Do all the things for day 05 puzzle.}
- Author: 3seasonal
- Created: 2025-12-05
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

__title__ = "Advent of Code 2025 Day 05 Puzzle"
__author__ = "3seasonal"
__created__ = "2025-12-05"


def main():
    """
    Main function to execute pid parsing.
    """
    
    # config
    #input_path = os.path.join(os.path.dirname(__file__), '05_sample_input.txt')
    input_path = os.path.join(os.path.dirname(__file__), '05_input.txt')
    
    #sample input
    sample_output_01 = None
    sample_output_02 = None
    
    # initialize parser and processor construtors
    iparse = InputParser(input_path)

    fresh_count = 0
    spoint_count = 0
    fresh_unique_count = 0
    spoint_unique_count = 0

    while iparse.more_items(unique=False):
        item = iparse.get_next_item(unique=False)
        if iparse.item_is_fresh(item, unique=False):
            fresh_count += 1
        else:
            spoint_count += 1

    while iparse.more_items(unique=True):
        item = iparse.get_next_item(unique=True)
        if iparse.item_is_fresh(item, unique=True):
            fresh_unique_count += 1
        else:
            spoint_unique_count += 1
        
    print(f"Part 1: Fresh items: {fresh_count}, Spoiled items: {spoint_count}")
    print(f"Part 2: Fresh unique items: {fresh_unique_count}, Spoiled unique items: {spoint_unique_count}")
  

    # get consolidated list
    iparse.consolidate_fresh_items()
    consolidated_fresh = iparse.get_consolidated_fresh_items()

    total_fresh_range_count = 0
    for start, end in consolidated_fresh:
        total_fresh_range_count += (end - start + 1)

    print(f"Total fresh range count: {total_fresh_range_count}")


if __name__ == "__main__":
    main()
    
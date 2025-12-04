#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from classes_04 import ParseAndProcess
"""

- Project: adventofcode
- Year: 2025
- Day: 04
- File: 04_papper_count.py
- Description: Count adjacent paper roles
- Author: 3seasonal
- Created: 2025-12-04
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

__title__ = "Advent of Code 2025 Day 04 Puzzle"
__author__ = "3seasonal"
__created__ = "2025-12-04"


def main():
    """
    Main function to execute pid parsing.
    """
    
    # config
    #input_path = os.path.join(os.path.dirname(__file__), '04_sample_input.txt')
    input_path = os.path.join(os.path.dirname(__file__), '04_input.txt')
    
    max_adjacent_paper_rolls = 3

    #sample input
    sample_output_01 = None
    sample_output_02 = None
    
    # initialize parser and processor construtors
    pp = ParseAndProcess(input_path)
    rows = pp.get_rows()
    cols = pp.get_cols()
    
    # iterate over each cell in the paper grid and count adjacent paper rolls
    for r in range(rows):
        for c in range(cols):
            
            count = pp.get_count_adjacent_paper_rolls(r, c)
            pp.set_df_proximity_grid(r, c, count)

    # report results
    print (f"rows: {rows}, cols: {cols}")
    print (r"\nPaper Grid:")
    print (pp.df_paper_grid)
    print (r"\nProximity Grid:")
    print (pp.df_proximity_grid)
    print (r"\nProximity Counts:")
    dcc = pp.get_dict_proximity_count()
    for k in dcc.keys():
        print (dcc[k])
    print (f"calc sum: {pp.get_count_of_cells_with_min_adjacent_rolls(max_adjacent_paper_rolls)}")
    


if __name__ == "__main__":
    main()
    